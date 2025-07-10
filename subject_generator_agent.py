import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
import google.generativeai as genai
import argparse
import yaml
import requests
import json
import re
from typing import Dict, List, Any

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file. Please set it.")

genai.configure(api_key=GOOGLE_API_KEY)

# --- University Curriculum Lookup Tool ---
def university_curriculum_lookup(query: str) -> str:
    """
    Searches for curriculum information from universities for a given degree program.
    Returns structured information about common subjects, prerequisites, and course sequences.
    """
    try:
        # Normalize the query
        query_lower = query.lower()
        
        # Define curriculum data for common programs
        curriculum_database = {
            "computer science": {
                "universities": ["MIT", "Stanford", "CMU", "UC Berkeley", "Harvard"],
                "core_subjects": [
                    "Introduction to Computer Science",
                    "Data Structures and Algorithms", 
                    "Computer Architecture",
                    "Operating Systems",
                    "Database Systems",
                    "Software Engineering",
                    "Computer Networks",
                    "Theory of Computation",
                    "Discrete Mathematics",
                    "Linear Algebra",
                    "Calculus I & II",
                    "Probability and Statistics"
                ],
                "advanced_subjects": [
                    "Machine Learning",
                    "Artificial Intelligence", 
                    "Computer Graphics",
                    "Distributed Systems",
                    "Cybersecurity",
                    "Compiler Design",
                    "Human-Computer Interaction"
                ],
                "typical_sequence": {
                    "year_1": ["Programming Fundamentals", "Calculus I", "Linear Algebra", "Discrete Mathematics", "Physics I"],
                    "year_2": ["Data Structures", "Computer Architecture", "Calculus II", "Statistics", "Object-Oriented Programming"],
                    "year_3": ["Algorithms", "Operating Systems", "Database Systems", "Software Engineering", "Computer Networks"],
                    "year_4": ["Advanced electives", "Capstone Project", "Internship", "Research Project"]
                }
            },
            "artificial intelligence": {
                "universities": ["MIT", "Stanford", "CMU", "UC Berkeley", "Georgia Tech"],
                "core_subjects": [
                    "Introduction to AI",
                    "Machine Learning Fundamentals",
                    "Deep Learning",
                    "Natural Language Processing",
                    "Computer Vision",
                    "Robotics",
                    "Knowledge Representation",
                    "Statistical Learning Theory",
                    "Neural Networks",
                    "Data Mining",
                    "Pattern Recognition",
                    "Optimization Methods"
                ],
                "advanced_subjects": [
                    "Reinforcement Learning",
                    "Generative AI",
                    "AI Ethics",
                    "Explainable AI",
                    "Multi-Agent Systems",
                    "Cognitive Computing",
                    "AI for Healthcare"
                ],
                "typical_sequence": {
                    "year_1": ["Programming", "Calculus", "Linear Algebra", "Statistics", "Discrete Mathematics"],
                    "year_2": ["Data Structures", "Probability Theory", "Machine Learning Basics", "Computer Vision Intro"],
                    "year_3": ["Deep Learning", "NLP", "AI Algorithms", "Robotics", "Data Science"],
                    "year_4": ["Advanced AI Topics", "AI Ethics", "Research Project", "Industry Internship"]
                }
            },
            "machine learning": {
                "universities": ["Stanford", "MIT", "CMU", "UC Berkeley", "Caltech"],
                "core_subjects": [
                    "Statistical Learning",
                    "Deep Learning",
                    "Supervised Learning",
                    "Unsupervised Learning",
                    "Reinforcement Learning",
                    "Feature Engineering",
                    "Model Evaluation",
                    "Optimization for ML",
                    "Probabilistic Models",
                    "Time Series Analysis",
                    "Bayesian Methods",
                    "Information Theory"
                ],
                "advanced_subjects": [
                    "Advanced Deep Learning",
                    "Generative Models",
                    "Meta-Learning",
                    "Federated Learning",
                    "AutoML",
                    "MLOps",
                    "Quantum Machine Learning"
                ]
            },
            "data science": {
                "universities": ["UC Berkeley", "Harvard", "MIT", "Stanford", "NYU"],
                "core_subjects": [
                    "Statistical Analysis",
                    "Data Mining",
                    "Data Visualization",
                    "Big Data Analytics",
                    "Database Management",
                    "Python for Data Science",
                    "R Programming",
                    "Machine Learning",
                    "Business Intelligence",
                    "Data Ethics",
                    "Experimental Design",
                    "Predictive Analytics"
                ]
            }
        }
        
        # Find matching program
        best_match = None
        best_score = 0
        
        for program, data in curriculum_database.items():
            # Calculate similarity score
            score = 0
            program_words = program.split()
            for word in program_words:
                if word in query_lower:
                    score += 1
            
            # Bonus for exact matches
            if program in query_lower:
                score += 2
                
            if score > best_score:
                best_score = score
                best_match = data
        
        # If no good match, use computer science as default
        if best_match is None or best_score == 0:
            best_match = curriculum_database["computer science"]
        
        # Format the response
        result = {
            "status": "success",
            "query": query,
            "universities_referenced": best_match.get("universities", []),
            "core_subjects": best_match.get("core_subjects", []),
            "advanced_subjects": best_match.get("advanced_subjects", []),
            "typical_sequence": best_match.get("typical_sequence", {}),
            "recommendations": [
                "Include foundational mathematics and programming courses in early semesters",
                "Progress from theoretical concepts to practical applications",
                "Incorporate industry-relevant electives in later semesters",
                "Include capstone projects and internship opportunities",
                "Balance theoretical knowledge with hands-on experience"
            ]
        }
        
        return json.dumps(result, indent=2)
        
    except Exception as e:
        return f"Error looking up curriculum data: {str(e)}"

# Create the tool
curriculum_lookup_tool = Tool(
    name="UniversityCurriculumLookup",
    func=university_curriculum_lookup,
    description="Searches university curriculum databases for relevant degree programs and returns common subjects, course sequences, and academic standards from top institutions."
)

# --- Agent Prompt for Subject Generation ---
template = """
You are an expert academic curriculum designer. Your task is to generate a comprehensive list of subjects for a given degree program.

Here's how you should operate:
1.  Understand the Degree Program: Carefully read the user's request for the degree program (e.g., "Bachelor of Science in Computer Science").
2.  Research University Curricula: Use the 'UniversityCurriculumLookup' tool to research typical subjects, core courses, and common curriculum structures for the specified degree program from top universities.
3.  Use Your Knowledge: Draw upon your extensive knowledge combined with the research data to create a realistic and comprehensive subject list.
4.  Generate Subject List: Create a list of exactly 30 subjects (5 subjects per semester for a 6-semester program). For each subject, provide:
    *   `subject`: A concise and clear subject title.
    *   `level`: The academic level (e.g., "Undergraduate", "Graduate", "Elective").
    *   `duration_weeks`: A reasonable duration for the course in weeks, keeping in mind each semester is 4-5 months long (approximately 16-20 weeks). For example, 10, 12, 14, 16.
    *   `focus`: A brief, 1-2 sentence description of the course's main focus.
    *   `assessments`: A concise summary of typical assessment types (e.g., "Exams, projects, and participation.").
4.  Output Format: Output the subjects in valid YAML, structured by semester. Each semester should have a `semester_number` and a `subjects` list. Semesters 1-4 will have 5 regular subjects. Semesters 5 and 6 will have 3 regular subjects and 2 elective groups. Each elective group should have an `elective_name` and an `options` list containing 5 subject options, formatted like regular subjects. Exactly like this:

- semester_number: 1
  subjects:
    - subject: "Subject 1 for Sem 1"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Introduction to fundamental concepts."
      assessments: "Exams and assignments."
    - subject: "Subject 2 for Sem 1"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Building foundational skills."
      assessments: "Projects and quizzes."
    - subject: "Subject 3 for Sem 1"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Exploring core principles."
      assessments: "Midterm and final exam."
    - subject: "Subject 4 for Sem 1"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Practical application of theories."
      assessments: "Hands-on labs and reports."
    - subject: "Subject 5 for Sem 1"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Developing analytical capabilities."
      assessments: "Problem sets and case studies."
- semester_number: 2
  subjects:
    - subject: "Subject 1 for Sem 2"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Advanced concepts in a core area."
      assessments: "Research paper and presentation."
    - subject: "Subject 2 for Sem 2"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Specialized topics."
      assessments: "Project-based assessment."
    - subject: "Subject 3 for Sem 2"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Interdisciplinary studies."
      assessments: "Group projects and peer review."
    - subject: "Subject 4 for Sem 2"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Critical thinking and problem-solving."
      assessments: "Debates and essays."
    - subject: "Subject 5 for Sem 2"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Applied statistical methods."
      assessments: "Data analysis assignments."
# ... (similarly for Semester 3 and 4, each with 5 regular subjects)
- semester_number: 5
  subjects:
    - subject: "Core Subject for Sem 5 - A"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Integrating previous knowledge."
      assessments: "Comprehensive final exam."
    - subject: "Core Subject for Sem 5 - B"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Advanced topics in the field."
      assessments: "Capstone project proposal."
    - subject: "Core Subject for Sem 5 - C"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Ethical considerations and societal impact."
      assessments: "Reflective journal and discussion."
    - elective_name: "Elective 1"
      options:
        - subject: "Elective 1 Option 1"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Specialized elective topic."
          assessments: "Research project."
        - subject: "Elective 1 Option 2"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Alternative specialized topic."
          assessments: "Presentation and report."
        - subject: "Elective 1 Option 3"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Applied case studies."
          assessments: "Case study analysis."
        - subject: "Elective 1 Option 4"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Emerging trends."
          assessments: "Literature review."
        - subject: "Elective 1 Option 5"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Interdisciplinary applications."
          assessments: "Cross-functional team project."
    - elective_name: "Elective 2"
      options:
        - subject: "Elective 2 Option 1"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Another specialized elective topic."
          assessments: "Practical implementation."
        - subject: "Elective 2 Option 2"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Advanced problem-solving."
          assessments: "Competitive challenge."
        - subject: "Elective 2 Option 3"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Creative and innovative solutions."
          assessments: "Portfolio submission."
        - subject: "Elective 2 Option 4"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Theoretical foundations."
          assessments: "Formal proof and derivation."
        - subject: "Elective 2 Option 5"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Real-world applications."
          assessments: "Industry guest lecture series."
- semester_number: 6
  subjects:
    - subject: "Core Subject for Sem 6 - A"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Advanced research methodologies."
      assessments: "Thesis proposal and defense."
    - subject: "Core Subject for Sem 6 - B"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Professional development and ethics."
      assessments: "Internship report and presentation."
    - subject: "Core Subject for Sem 6 - C"
      level: "Undergraduate"
      duration_weeks: 16
      focus: "Global trends and future directions."
      assessments: "Future studies analysis."
    - elective_name: "Elective 3"
      options:
        - subject: "Elective 3 Option 1"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Highly specialized advanced topic."
          assessments: "Advanced seminar participation."
        - subject: "Elective 3 Option 2"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Cutting-edge research areas."
          assessments: "Journal club and critical review."
        - subject: "Elective 3 Option 3"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Innovative technology exploration."
          assessments: "Proof-of-concept demonstration."
        - subject: "Elective 3 Option 4"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Cross-disciplinary integration."
          assessments: "Collaborative research project."
        - subject: "Elective 3 Option 5"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Emerging paradigms."
          assessments: "Position paper."
    - elective_name: "Elective 4"
      options:
        - subject: "Elective 4 Option 1"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Advanced practical application."
          assessments: "Industry practicum report."
        - subject: "Elective 4 Option 2"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Complex system design."
          assessments: "System architecture design."
        - subject: "Elective 4 Option 3"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Data-driven decision making."
          assessments: "Predictive modeling challenge."
        - subject: "Elective 4 Option 4"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Human-computer interaction principles."
          assessments: "User experience design project."
        - subject: "Elective 4 Option 5"
          level: "Undergraduate"
          duration_weeks: 16
          focus: "Security and privacy concerns."
          assessments: "Security audit and vulnerability assessment."

IMPORTANT: Generate the complete subject list directly in valid YAML format, following the structure exactly as shown above.

You have access to the following tools:
{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Since no tools are available, proceed directly to generating the curriculum.

Begin!

Question: Generate subjects for the degree program: {input}
Thought: I need to generate a comprehensive curriculum for this degree program based on my knowledge of academic standards and typical university curricula.
Final Answer: 

{agent_scratchpad}
"""

prompt = PromptTemplate.from_template(template)

# Use gemini-2.0-flash for subject generation
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GOOGLE_API_KEY)

# --- Create the Agent ---
# Add the curriculum lookup tool
tools = [curriculum_lookup_tool]
prompt = prompt.partial(tools="\n".join([f"{tool.name}: {tool.description}" for tool in tools]), 
                       tool_names=", ".join([tool.name for tool in tools]))
agent = create_react_agent(llm, tools, prompt)

# --- Agent Executor ---
# Set verbose to False for cleaner output, but you can set to True for debugging
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False, handle_parsing_errors=True, max_iterations=50)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a list of subjects for a degree program.")
    parser.add_argument("--degree-program", type=str, required=True, help="The degree program for which to generate subjects (e.g., 'Bachelor of Science in Computer Science').")
    parser.add_argument("--output-file", type=str, default="generated_subjects.yaml", help="The output YAML file to save the generated subjects.")
    args = parser.parse_args()

    print(f"Generating subjects for: {args.degree_program}...")
    result = None # Initialize result to None before try block
    try:
        result = agent_executor.invoke({
            "input": args.degree_program
        })

        if result and result["output"]:
            generated_yaml = result["output"]
            
            # Clean the generated_yaml string to remove markdown and bolding if present
            generated_yaml = generated_yaml.replace("**", "").strip()
            if generated_yaml.startswith("```yaml") and generated_yaml.endswith("```"):
                generated_yaml = generated_yaml[len("```yaml\n"): -len("```")].strip()
            elif generated_yaml.startswith("```") and generated_yaml.endswith("```"):
                generated_yaml = generated_yaml[len("```\n"): -len("```")].strip()

            try:
                # Optional: Validate if the generated output is valid YAML/list
                # This will raise an error if it's not well-formed YAML
                parsed_subjects = yaml.safe_load(generated_yaml)
                if not isinstance(parsed_subjects, list):
                    raise ValueError("Generated YAML is not a list.")

                with open(args.output_file, "w", encoding="utf-8") as f:
                    f.write(generated_yaml)
                print(f"\nSubjects successfully saved to: {args.output_file}")

            except (yaml.YAMLError, ValueError) as e:
                print(f"\nError: Generated output is not valid YAML or not a list of subjects. Reason: {e}")
                print("Generated Output:")
                print(generated_yaml)
        else:
            print("\nNo subjects generated by the agent.")

    except Exception as e:
        print(f"An error occurred during subject generation: {e}")
        print("Please try again or check your API key/quotas.")