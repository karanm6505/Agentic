import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import tools
from langchain_core.prompts import PromptTemplate
from duckduckgo_search import DDGS
import google.generativeai as genai
import argparse
import json
import yaml

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

# Use gemini-2.0-flash-lite as requested by the user.
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", google_api_key=GOOGLE_API_KEY)

# --- Create the Agent ---
agent = create_react_agent(llm, tools, prompt)

# --- Agent Executor ---
# Set verbose to False for cleaner batch output
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False, handle_parsing_errors=True, max_iterations=50)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch Syllabus Generation Agent.")
    parser.add_argument("--config-file", type=str, required=True, help="Path to a YAML or JSON file containing course configurations (now expects semester-grouped subjects).")
    parser.add_argument("--degree-program-short-name", type=str, required=True, help="Short name of the degree program (e.g., 'CS', 'AIML', 'EC') for output folder organization.")
    parser.add_argument("--base-output-dir", type=str, default="./syllabuses", help="Base directory to save the generated syllabuses.")
    args = parser.parse_args()

    # Define the output directory structure: base_output_dir/degree_program_short_name/
    degree_output_dir = os.path.join(args.base_output_dir, args.degree_program_short_name)
    os.makedirs(degree_output_dir, exist_ok=True)

    # Load course configurations from the specified file
    semester_data = []
    with open(args.config_file, 'r') as f:
        if args.config_file.endswith('.json'):
            semester_data = json.load(f)
        elif args.config_file.endswith('.yaml') or args.config_file.endswith('.yml'):
            semester_data = yaml.safe_load(f)
        else:
            raise ValueError("Unsupported config file format. Use .json or .yaml/.yml")

    if not isinstance(semester_data, list):
        raise ValueError("Config file must contain a list of semester dictionaries.")

    print("Starting batch syllabus generation...")

    total_syllabuses_generated = 0
    total_syllabuses_to_generate = sum(
        len(sem["subjects"])
        for sem in semester_data
        if isinstance(sem, dict) and "subjects" in sem and isinstance(sem["subjects"], list)
    )

    for semester_entry in semester_data:
        if not isinstance(semester_entry, dict) or "semester_number" not in semester_entry or "subjects" not in semester_entry:
            print(f"Skipping invalid semester entry: {semester_entry}")
            continue

        semester_number = semester_entry["semester_number"]
        subjects_in_semester = semester_entry["subjects"]

        semester_output_dir = os.path.join(degree_output_dir, f"Sem_{semester_number}")
        os.makedirs(semester_output_dir, exist_ok=True)
        print(f"\nProcessing Semester {semester_number}...")

        for course_item in subjects_in_semester:
            if "subject" in course_item:
                # This is a regular subject
                subject = course_item["subject"]
                level = course_item["level"]
                duration_weeks = course_item["duration_weeks"]
                focus = course_item["focus"]
                assessments = course_item["assessments"]

                # Create a clean filename for the syllabus
                safe_subject_name = "".join(c for c in subject if c.isalnum() or c == ' ').replace(' ', '_')
                output_filename = os.path.join(semester_output_dir, f"{safe_subject_name}_Syllabus.md")

                print(f"\nGenerating syllabus for: {subject} (Semester {semester_number})...")
                result = None # Initialize result to None before try block
                try:
                    result = agent_executor.invoke({
                        "subject": subject,
                        "level": level,
                        "duration_weeks": duration_weeks,
                        "focus": focus,
                        "assessments": assessments,
                        "input": f"Generate a {level} course syllabus for '{subject}' lasting {duration_weeks} weeks, focusing on '{focus}', with assessments including {assessments}."
                    })

                    if result:
                        print("\n--- GENERATED SYLLABUS ---\n")
                        print(result["output"])
                        print("\n--------------------------\n")

                        try:
                            with open(output_filename, "w", encoding="utf-8") as f:
                                f.write(result["output"])
                            print(f"Syllabus successfully saved to: {output_filename}")
                            total_syllabuses_generated += 1
                        except IOError as e:
                            print(f"Error: Could not save the file {output_filename}. Reason: {e}")

                except Exception as e:
                    print(f"An error occurred during generation for {subject}: {e}")
                    print("Skipping to the next syllabus.")
            elif "elective_name" in course_item and "options" in course_item:
                # This is an elective group
                elective_name = course_item["elective_name"]
                elective_options = course_item["options"]
                print(f"\nProcessing Elective Group: {elective_name} in Semester {semester_number}...")

                for option_details in elective_options:
                    if "subject" in option_details:
                        subject = option_details["subject"]
                        level = option_details["level"]
                        duration_weeks = option_details["duration_weeks"]
                        focus = option_details["focus"]
                        assessments = option_details["assessments"]

                        # Create a clean filename for the elective syllabus
                        safe_subject_name = "".join(c for c in subject if c.isalnum() or c == ' ').replace(' ', '_')
                        output_filename = os.path.join(semester_output_dir, f"{safe_subject_name}_Syllabus.md")

                        print(f"\nGenerating syllabus for elective option: {subject} (under {elective_name}, Semester {semester_number})...")
                        result = None # Initialize result to None before try block
                        try:
                            result = agent_executor.invoke({
                                "subject": subject,
                                "level": level,
                                "duration_weeks": duration_weeks,
                                "focus": focus,
                                "assessments": assessments,
                                "input": f"Generate a {level} course syllabus for '{subject}' lasting {duration_weeks} weeks, focusing on '{focus}', with assessments including {assessments}."
                            })

                            if result:
                                print("\n--- GENERATED SYLLABUS ---\n")
                                print(result["output"])
                                print("\n--------------------------\n")

                                try:
                                    with open(output_filename, "w", encoding="utf-8") as f:
                                        f.write(result["output"])
                                    print(f"Syllabus successfully saved to: {output_filename}")
                                    total_syllabuses_generated += 1
                                except IOError as e:
                                    print(f"Error: Could not save the file {output_filename}. Reason: {e}")

                        except Exception as e:
                            print(f"An error occurred during generation for elective {subject}: {e}")
                            print("Skipping to the next elective option.")
                    else:
                        print(f"Skipping invalid elective option entry: {option_details}")
            else:
                print(f"Skipping invalid course item in Semester {semester_number}: {course_item}")
    
    print(f"\nBatch syllabus generation complete. Total syllabuses generated: {total_syllabuses_generated}/{total_syllabuses_to_generate}") 