import yaml
import graphviz
import argparse
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file. Please set it.")

genai.configure(api_key=GOOGLE_API_KEY)

def get_prerequisites_from_gemini(subject_name, subject_focus, subject_level):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.2)
    prompt = f"Given the course: '{subject_name}' (Level: {subject_level}, Focus: {subject_focus}). List any prerequisite courses. If there are no prerequisites, say 'None'. If there are multiple, separate them with commas. Only provide the course names, no other text or explanation."
    try:
        response = llm.invoke(prompt)
        prereqs_text = response.content.strip()
        if prereqs_text.lower() == "none":
            return []
        return [p.strip() for p in prereqs_text.split(',')]
    except Exception as e:
        print(f"Error getting prerequisites for {subject_name} from Gemini: {e}")
        return []

def generate_dependency_graph(yaml_file_path, output_format='png', view_graph=True):
    """
    Generates a dependency graph (Digraph) from a YAML file containing subject data.
    It uses Gemini API to infer prerequisites if not explicitly provided.

    The YAML file is expected to have a structure like:
    - semester_number: 1
      subjects:
        - subject: "Subject Name 1"
          focus: "..."
          level: "..."
          # prerequisites: "Prereq Subject A, Prereq Subject B" (optional)
    Or for electives:
    - elective_name: "Elective Group Name"
      options:
        - subject: "Elective Subject 1"
          focus: "..."pro
          level: "..."
          # prerequisites: "Core Subject C" (optional)

    Args:
        yaml_file_path (str): Path to the input YAML file.
        output_format (str): Desired output format for the graph (e.g., 'png', 'pdf', 'svg').
        view_graph (bool): Whether to automatically open the generated graph.
    """
    if not os.path.exists(yaml_file_path):
        print(f"Error: Input YAML file not found at '{yaml_file_path}'")
        return

    try:
        with open(yaml_file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return

    dot = graphviz.Digraph(comment='Subject Dependency Graph', format=output_format)
    dot.attr(rankdir='LR') # Left to Right graph direction

    all_subjects = {}
    semester_subjects = {}

    # Collect all subjects and map them to a unique ID, and group by semester
    for entry in data:
        if "semester_number" in entry:
            semester_num = entry["semester_number"]
            semester_subjects[semester_num] = []
            for subject_info in entry["subjects"]:
                if "subject" in subject_info: # Ensure it's a subject and not an elective group
                    subject_name = subject_info["subject"]
                    subject_id = f"S{semester_num}_{subject_name.replace(' ', '_').replace('.', '').replace('-', '_').replace('(', '').replace(')', '')}"
                    all_subjects[subject_name] = subject_id
                    semester_subjects[semester_num].append(subject_name)
                    dot.node(subject_id, subject_name)
                elif "elective_name" in subject_info: # Handle electives within semesters if they appear like this
                    elective_group_name = subject_info["elective_name"]
                    for option_info in subject_info["options"]:
                        subject_name = option_info["subject"]
                        subject_id = f"E_{subject_name.replace(' ', '_').replace('.', '').replace('-', '_').replace('(', '').replace(')', '')}"
                        all_subjects[subject_name] = subject_id
                        dot.node(subject_id, subject_name)

        elif "elective_name" in entry: # This is a top-level elective group entry
            elective_group_name = entry["elective_name"]
            for option_info in entry["options"]:
                subject_name = option_info["subject"]
                subject_id = f"E_{subject_name.replace(' ', '_').replace('.', '').replace('-', '_').replace('(', '').replace(')', '')}"
                all_subjects[subject_name] = subject_id
                dot.node(subject_id, subject_name)

    # Add edges based on prerequisites (either explicit or inferred by Gemini)
    for entry in data:
        subjects_to_process = []
        if "semester_number" in entry:
            subjects_to_process = entry["subjects"]
        elif "elective_name" in entry:
            subjects_to_process = entry["options"]

        for subject_info in subjects_to_process:
            if "subject" not in subject_info:
                continue # Skip if not a direct subject entry
            
            current_subject_name = subject_info["subject"]
            current_subject_id = all_subjects.get(current_subject_name)

            prerequisites_str = subject_info.get("prerequisites")
            if not prerequisites_str or prerequisites_str.lower() == "none":
                # If prerequisites are not explicitly given or are 'None', ask Gemini
                print(f"Inferring prerequisites for: {current_subject_name}...")
                inferred_prereqs = get_prerequisites_from_gemini(
                    current_subject_name,
                    subject_info.get("focus", ""),
                    subject_info.get("level", "Undergraduate")
                )
                prereqs_to_use = inferred_prereqs
            else:
                # Use explicit prerequisites if available
                prereqs_to_use = [p.strip() for p in prerequisites_str.split(',')]

            for prereq_name in prereqs_to_use:
                prereq_id = all_subjects.get(prereq_name)
                if prereq_id and current_subject_id:
                    dot.edge(prereq_id, current_subject_id)
                elif not prereq_id:
                    print(f"Warning: Prerequisite '{prereq_name}' for '{current_subject_name}' not found in the subject list or could not be inferred.")
            
    # Define semester clusters and their general flow (visual separation)
    semester_numbers = sorted(semester_subjects.keys())
    for sem_num in semester_numbers:
        with dot.subgraph(name=f"cluster_semester_{sem_num}") as c:
            c.attr(label=f"Semester {sem_num}", style='filled', color='lightgrey')
            for subj_name in semester_subjects[sem_num]:
                c.node(all_subjects[subj_name])

    # Add invisible edges between the last subject of one semester and the first of the next
    # to enforce a left-to-right flow for semesters.
    for i in range(len(semester_numbers) - 1):
        current_sem = semester_numbers[i]
        next_sem = semester_numbers[i+1]
        
        if semester_subjects[current_sem] and semester_subjects[next_sem]:
            last_subj_current_sem_id = all_subjects[semester_subjects[current_sem][-1]]
            first_subj_next_sem_id = all_subjects[semester_subjects[next_sem][0]]
            dot.edge(last_subj_current_sem_id, first_subj_next_sem_id, style="invis")

    output_filename = os.path.splitext(yaml_file_path)[0] + "_dependency_graph"
    try:
        dot.render(output_filename, view=view_graph, cleanup=True)
        print(f"Dependency graph generated and saved to '{output_filename}.{output_format}'")
    except Exception as e:
        print(f"Error rendering graph: {e}. Make sure Graphviz is installed and in your system's PATH.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a subject dependency graph from a YAML file using Graphviz.")
    parser.add_argument("input_yaml_file", type=str, help="Path to the input YAML file containing subject data.")
    parser.add_argument("--format", type=str, default="png", help="Output format for the graph (e.g., 'png', 'pdf', 'svg'). Default is 'png'.")
    parser.add_argument("--no-view", action="store_true", help="Do not open the generated graph automatically.")

    args = parser.parse_args()

    generate_dependency_graph(args.input_yaml_file, output_format=args.format, view_graph=not args.no_view) 