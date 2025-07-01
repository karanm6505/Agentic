import os
import sys
import re
import yaml
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import tools
from langchain_core.prompts import PromptTemplate
from duckduckgo_search import DDGS
import google.generativeai as genai
import argparse
import json
from google.api_core.exceptions import ResourceExhausted

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file. Please set it.")

genai.configure(api_key=GOOGLE_API_KEY)

# --- Tools ---
def duckduckgo_search(query: str):
    """Searches DuckDuckGo for the given query and returns the top result's snippet."""
    with DDGS() as ddgs:
        results = ddgs.text(keywords=query, max_results=1)
        if results:
            return results[0]['snippet']
        return "No information found."

search_tool = tools.Tool(
    name="DuckDuckGoSearch",
    func=duckduckgo_search,
    description="Useful for searching the web for information about course topics, learning objectives, or resources."
)

tools = [search_tool]

# --- Agent Prompt with your detailed blueprint ---
template = """
You are an expert academic syllabus generator AI. Your task is to create a comprehensive course syllabus based on user requests.

Here's how you should operate:
1.  **Understand the Request:** Carefully read the user's request for the course topic, level, duration, focus, and assessment types.
2.  **Research (if necessary):** If the topic is complex or you need more context (e.g., common topics for an advanced subject), use the 'DuckDuckGoSearch' tool to gather information.
3.  **Syllabus Structure and Content:** Generate the syllabus strictly following the exact Markdown structure and content guidelines provided below. Use realistic academic language and subject-specific details. Ensure the content for each section is well-detailed and relevant to the course topic and parameters.

# Course Syllabus
## Course Title: [Course Name]
**Course Code:** [Course Code]
**Credits:** [Credits]
**Semester:** [Semester]
**Instructor:** [Instructor Name Placeholder]
**Contact:** [instructor.email@university.edu]
**Office Hours:** [Office Hours or By Appointment]

### Course Description:
[1-2 concise paragraphs, 50-150 words]

### Prerequisites:
[Comma-separated list or 'None']

### Learning Objectives:
[Numbered list, 4-7 objectives, each starting with an action verb (e.g., 'Analyze', 'Implement', 'Evaluate').]

### Required Textbooks:
[Bulleted list: - Author, *Title of Book*, Publisher, Year (ISBN: [if available])]

### Recommended Readings:
[Bulleted list: - Article Title, Journal Name, Volume(Issue):Pages, Year. OR 'None']

### Weekly Schedule:
[Detailed breakdown for each week, using the exact format below. Vary topics, readings, activities, and due dates realistically. Adjust the number of weeks based on the 'duration_weeks' input.]
**Week [Number]: [Main Topic Name]**
- Topics: [Specific sub-topics covered]
- Readings: [Specific chapters or articles]
- Activities: [Lab sessions, discussions, guest speakers]
- Due: [Assignment/Quiz due this week, if any, or 'N/A']

### Assessment Breakdown:
[Bulleted list of components with percentages and brief descriptions based on the request.]

### Grading Scale:
A: 90-100%
B: 80-89%
C: 70-79%
D: 60-69%
F: Below 60%


**IMPORTANT:** You must follow this exact format for your responses. When you need to perform an action, use the 'Thought', 'Action', 'Action Input' pattern. When you have the final syllabus, use the 'Final Answer' pattern.

**Thought:** [Your reasoning process here, always start with 'Thought:']
**Action:** [The tool name, e.g., 'DuckDuckGoSearch']
**Action Input:** [The input for the tool, e.g., 'common topics for quantum computing']
**Observation:** [The result from the tool (provided by the system)]

**When you are ready to provide the final syllabus, use this format:**
**Thought:** I have completed the syllabus and it is ready to be presented.
**Final Answer:** [The complete syllabus in Markdown format, following all specified sections and content guidelines]

Begin!

Course Details:
Subject: {subject}
Level: {level}
Duration: {duration_weeks} weeks
Focus: {focus}
Assessment Types: {assessments}

{agent_scratchpad}
"""

prompt = PromptTemplate.from_template(template)
prompt = prompt.partial(tools=tools, tool_names=", ".join([tool.name for tool in tools]))

def clean_generated_text(text):
    # Remove markdown code blocks and bolding
    text = re.sub(r"```[a-zA-Z]*\n|```", "", text)  # Remove ```yaml and ```
    text = text.replace("**", "")  # Remove ** for bolding
    return text.strip()

def get_gemini_model(model_name="gemini-1.5-flash-latest"):
    try:
        llm = ChatGoogleGenerativeAI(model=model_name, temperature=0.3)
        llm.invoke("Hello") # Test if the model is accessible
        return llm
    except ResourceExhausted:
        print(f"Quota exceeded for {model_name}. Trying another model...")
        return None
    except Exception as e:
        print(f"Error initializing model {model_name}: {e}")
        return None

def initialize_agent(model_name="gemini-1.5-flash-latest"):
    tools = [
        DuckDuckGoSearchRun(name="DuckDuckGoSearch", description="Useful for when you need to answer questions about current events or research a topic.")
    ]

    # Initialize LLM with fallback logic
    llm = None
    models_to_try = [model_name, "gemini-pro"]  # Prioritize the specified model, then fallback
    for m in models_to_try:
        llm = get_gemini_model(m)
        if llm:
            print(f"Successfully initialized agent with model: {m}")
            break
    if not llm:
        raise ValueError("Could not initialize any Gemini model.")

    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, max_iterations=50)

    return agent_executor

if __name__ == "__main__":
    try:
        import yaml
    except ImportError:
        yaml = None # Handle optional YAML dependency

    parser = argparse.ArgumentParser(description="Syllabus Generation Agent.")
    parser.add_argument("--config-file", type=str, help="Path to a YAML or JSON configuration file with course parameters.")
    parser.add_argument("--output-file", type=str, help="Optional path to save the generated syllabus to a text file.")
    args = parser.parse_args()

    course_details = {}

    if args.config_file:
        file_path = args.config_file
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Configuration file not found: {file_path}")
        
        print(f"Loading course details from {file_path}...")
        with open(file_path, 'r') as f:
            if file_path.endswith('.json'):
                course_details = json.load(f)
            elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
                if yaml:
                    course_details = yaml.safe_load(f)
                else:
                    raise ImportError("PyYAML is not installed. Please install it with 'pip install pyyaml' to use YAML config files.")
            else:
                raise ValueError("Unsupported config file format. Use .json or .yaml/.yml")
        
        # Validate required keys in config file
        required_keys = ["subject", "level", "duration_weeks", "focus", "assessments"]
        for key in required_keys:
            if key not in course_details:
                raise ValueError(f"Missing required key '{key}' in the configuration file.")
    else:
        print("Syllabus Generation Agent Ready!")
        subject = input("Enter the course subject (e.g., 'Introduction to Python Programming'): ")
        if subject.lower() == 'exit':
            exit()
        level = input("Enter the academic level (e.g., 'Undergraduate', 'Graduate'): ")
        duration_weeks = int(input("Enter the course duration in weeks (e.g., 12): "))
        focus = input("Enter the course's main focus (e.g., 'Foundations of machine learning algorithms and their applications.'): ")
        assessments = input("Enter assessment types (e.g., '3 programming assignments, a midterm, and a final project'): ")
        
        course_details = {
            "subject": subject,
            "level": level,
            "duration_weeks": duration_weeks,
            "focus": focus,
            "assessments": assessments
        }

    print(f"Generating syllabus for: {course_details["subject"]}...")
    result = None # Initialize result to None
    try:
        # Ensure agent_executor is initialized before calling invoke
        agent_executor = initialize_agent(model_name=os.getenv("GEMINI_MODEL", "gemini-1.5-flash-latest"))
        result = agent_executor.invoke({
            "subject": course_details["subject"],
            "level": course_details["level"],
            "duration_weeks": course_details["duration_weeks"],
            "focus": course_details["focus"],
            "assessments": course_details["assessments"],
            "input": f"Generate a {course_details["level"]} course syllabus for '{course_details["subject"]}' lasting {course_details["duration_weeks"]} weeks, focusing on '{course_details["focus"]}', with assessments including {course_details["assessments"]}."
        })

        if result: # Only process if result was successfully obtained
            print("\n--- GENERATED SYLLABUS ---\n")
            print(result["output"])
            print("\n--------------------------\n")

            # Save to file if an output path was provided
            if args.output_file:
                try:
                    with open(args.output_file, "w", encoding="utf-8") as f:
                        f.write(result["output"])
                    print(f"\nSyllabus successfully saved to: {args.output_file}")
                except IOError as e:
                    print(f"\nError: Could not save the file to {args.output_file}. Reason: {e}")

    except ResourceExhausted as e:
        print(f"Failed to generate syllabus for {course_details['subject']} due to quota limits: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during syllabus generation for {course_details['subject']}: {e}")

    # Save to file if an output path was provided
    # This block is redundant and causing the NameError, removing it.
    # if args.output_file:
    #     try:
    #         with open(args.output_file, "w", encoding="utf-8") as f:
    #             f.write(result["output"])
    #         print(f"\nSyllabus successfully saved to: {args.output_file}")
    #     except IOError as e:
    #         print(f"\nError: Could not save the file to {args.output_file}. Reason: {e}") 