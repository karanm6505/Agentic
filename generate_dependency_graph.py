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
          focus: "..."
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

    # Create a cleaner, more visually appealing graph
    dot = graphviz.Digraph(comment='Subject Dependency Graph', format=output_format)
    
    # Enhanced graph attributes for cleaner appearance
    dot.attr(
        rankdir='TB',  # Top to Bottom for better semester flow
        size='20,16',   # Larger canvas
        dpi='300',      # High resolution
        splines='ortho', # Orthogonal edge routing for cleaner lines
        nodesep='0.8',  # More space between nodes
        ranksep='1.2',  # More space between ranks/levels
        bgcolor='white',
        fontname='Arial',
        fontsize='14'
    )
    
    # Define color scheme for different categories
    colors = {
        'math': '#E8F4FD',      # Light blue for math courses
        'programming': '#E8F8E8', # Light green for programming
        'ai_ml': '#FFE8E8',     # Light red for AI/ML courses
        'theory': '#FFF8E8',    # Light yellow for theoretical courses
        'project': '#F0E8FF',   # Light purple for projects
        'elective': '#F8F8F8'   # Light gray for electives
    }
    
    # Enhanced node styling
    dot.attr('node', 
             shape='box',
             style='filled,rounded',
             fontname='Arial',
             fontsize='11',
             margin='0.3,0.1',
             width='2.5',
             height='0.8'
    )
    
    # Enhanced edge styling
    dot.attr('edge',
             fontname='Arial',
             fontsize='9',
             arrowsize='0.8',
             penwidth='1.5'
    )

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
                    
                    # Enhanced node creation with categorization and styling
                    category = categorize_subject(subject_name, subject_info.get("focus", ""))
                    shortened_name = shorten_subject_name(subject_name)
                    
                    dot.node(subject_id, shortened_name, 
                            fillcolor=colors[category],
                            tooltip=subject_name)  # Full name on hover
                            
                elif "elective_name" in subject_info: # Handle electives within semesters if they appear like this
                    elective_group_name = subject_info["elective_name"]
                    for option_info in subject_info["options"]:
                        subject_name = option_info["subject"]
                        clean_name = subject_name.replace(' ', '_').replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
                        subject_id = f"E_{clean_name}"
                        all_subjects[subject_name] = subject_id
                        
                        # Style elective nodes
                        shortened_name = shorten_subject_name(subject_name)
                        dot.node(subject_id, shortened_name,
                                fillcolor=colors['elective'],
                                style='filled,rounded,dashed',
                                tooltip=subject_name)

        elif "elective_name" in entry: # This is a top-level elective group entry
            elective_group_name = entry["elective_name"]
            for option_info in entry["options"]:
                subject_name = option_info["subject"]
                clean_name = subject_name.replace(' ', '_').replace('.', '').replace('-', '_').replace('(', '').replace(')', '')
                subject_id = f"E_{clean_name}"
                all_subjects[subject_name] = subject_id
                
                # Style elective nodes
                shortened_name = shorten_subject_name(subject_name)
                dot.node(subject_id, shortened_name,
                        fillcolor=colors['elective'],
                        style='filled,rounded,dashed',
                        tooltip=subject_name)

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
                # Enhanced fuzzy matching for prerequisite names
                prereq_name_matched = find_best_match(prereq_name, all_subjects)
                prereq_id = all_subjects.get(prereq_name_matched) if prereq_name_matched else None
                if prereq_id and current_subject_id:
                    # Enhanced edge styling based on relationship strength
                    dot.edge(prereq_id, current_subject_id, 
                            color='#555555',
                            arrowhead='vee')
                elif not prereq_id:
                    print(f"Warning: Prerequisite '{prereq_name}' for '{current_subject_name}' not found in the subject list or could not be inferred.")
            
    # Enhanced semester clustering with better visual separation
    semester_numbers = sorted(semester_subjects.keys())
    
    # Create a legend for color coding
    with dot.subgraph(name='cluster_legend') as legend:
        legend.attr(label='Subject Categories', 
                   style='filled',
                   color='#f0f0f0',
                   fontsize='12',
                   fontname='Arial Bold')
        
        # Add legend nodes
        legend.node('legend_math', 'Mathematics', fillcolor=colors['math'], shape='box', style='filled')
        legend.node('legend_prog', 'Programming', fillcolor=colors['programming'], shape='box', style='filled')
        legend.node('legend_ai', 'AI/ML', fillcolor=colors['ai_ml'], shape='box', style='filled')
        legend.node('legend_theory', 'Theory', fillcolor=colors['theory'], shape='box', style='filled')
        legend.node('legend_project', 'Projects', fillcolor=colors['project'], shape='box', style='filled')
        legend.node('legend_elective', 'Electives', fillcolor=colors['elective'], shape='box', style='filled,dashed')
        
        # Arrange legend horizontally
        legend.attr(rank='same')
    
    # Create semester clusters with enhanced styling
    for sem_num in semester_numbers:
        if semester_subjects[sem_num]:  # Only create cluster if there are subjects
            with dot.subgraph(name=f"cluster_semester_{sem_num}") as c:
                c.attr(
                    label=f"Semester {sem_num}",
                    style='filled,rounded',
                    color='#e6f2ff',
                    fontsize='14',
                    fontname='Arial Bold',
                    penwidth='2'
                )
                
                # Add subjects to cluster with proper ranking
                for subj_name in semester_subjects[sem_num]:
                    c.node(all_subjects[subj_name])
    
    # Improve semester flow with better invisible edges
    for i in range(len(semester_numbers) - 1):
        current_sem = semester_numbers[i]
        next_sem = semester_numbers[i+1]
        
        if semester_subjects[current_sem] and semester_subjects[next_sem]:
            # Create invisible edges between all subjects of consecutive semesters
            # to maintain proper ranking
            for curr_subj in semester_subjects[current_sem]:
                for next_subj in semester_subjects[next_sem][:1]:  # Just to first subject
                    dot.edge(all_subjects[curr_subj], all_subjects[next_subj], 
                            style="invis", 
                            weight='1')

    output_filename = os.path.splitext(yaml_file_path)[0] + "_dependency_graph"
    try:
        dot.render(output_filename, view=view_graph, cleanup=True)
        print(f"Dependency graph generated and saved to '{output_filename}.{output_format}'")
    except Exception as e:
        print(f"Error rendering graph: {e}. Make sure Graphviz is installed and in your system's PATH.")


def categorize_subject(subject_name, subject_focus=""):
    """Categorize subjects for color coding"""
    subject_lower = subject_name.lower()
    focus_lower = subject_focus.lower()
    
    # Math-related courses
    if any(term in subject_lower for term in ['calculus', 'linear algebra', 'discrete mathematics', 'probability', 'statistics']):
        return 'math'
    
    # Programming courses
    elif any(term in subject_lower for term in ['programming', 'data structures', 'algorithms', 'software engineering', 'database']):
        return 'programming'
    
    # AI/ML courses
    elif any(term in subject_lower for term in ['machine learning', 'artificial intelligence', 'deep learning', 'neural', 'nlp', 'computer vision', 'reinforcement']):
        return 'ai_ml'
    
    # Project/Practical courses
    elif any(term in subject_lower for term in ['project', 'research', 'thesis', 'capstone', 'entrepreneurship']):
        return 'project'
    
    # Theoretical courses
    elif any(term in subject_lower for term in ['theory', 'ethics', 'reasoning', 'planning']):
        return 'theory'
    
    # Default to elective
    else:
        return 'elective'

def shorten_subject_name(subject_name):
    """Shorten long subject names for better visualization"""
    # Common abbreviations
    abbreviations = {
        'Introduction to': 'Intro to',
        'Artificial Intelligence': 'AI',
        'Machine Learning': 'ML',
        'Natural Language Processing': 'NLP',
        'Object-Oriented Programming': 'OOP',
        'Data Structures and Algorithms': 'DSA',
        'Database Management Systems': 'DBMS',
        'Software Engineering': 'Software Eng',
        'Computer Vision': 'CV',
        'Reinforcement Learning': 'RL',
        'Deep Learning': 'DL',
        'Big Data Analytics': 'Big Data',
        'Probability and Statistics': 'Prob & Stats',
        'Linear Algebra': 'Linear Alg',
        'Discrete Mathematics': 'Discrete Math'
    }
    
    shortened = subject_name
    for full, abbrev in abbreviations.items():
        shortened = shortened.replace(full, abbrev)
    
    # If still too long, truncate and add ellipsis
    if len(shortened) > 25:
        shortened = shortened[:22] + "..."
    
    return shortened

def find_best_match(prereq_name, all_subjects):
    """Find the best matching subject name using fuzzy matching"""
    prereq_lower = prereq_name.lower()
    
    # Direct mapping for common variations
    name_mappings = {
        'introduction to programming': 'Introduction to Programming',
        'programming': 'Introduction to Programming',
        'intro to programming': 'Introduction to Programming',
        'calculus': 'Calculus I',
        'calculus 1': 'Calculus I',
        'multivariable calculus': 'Calculus II',
        'calculus 2': 'Calculus II',
        'machine learning': 'Machine Learning Fundamentals',
        'intro to machine learning': 'Machine Learning Fundamentals',
        'introduction to machine learning': 'Machine Learning Fundamentals',
        'artificial intelligence': 'Artificial Intelligence',
        'intro to ai': 'Introduction to AI and ML',
        'introduction to artificial intelligence': 'Introduction to AI and ML',
        'statistics': 'Probability and Statistics',
        'probability': 'Probability and Statistics',
        'data structures': 'Data Structures and Algorithms',
        'algorithms': 'Data Structures and Algorithms',
        'databases': 'Database Management Systems',
        'introduction to databases': 'Database Management Systems',
        'oop': 'Object-Oriented Programming',
        'object oriented programming': 'Object-Oriented Programming'
    }
    
    # Check direct mapping first
    if prereq_lower in name_mappings:
        mapped_name = name_mappings[prereq_lower]
        if mapped_name in all_subjects:
            return mapped_name
    
    # Check for partial matches
    for subject_name in all_subjects.keys():
        subject_lower = subject_name.lower()
        # Check if prerequisite is contained in subject name or vice versa
        if prereq_lower in subject_lower or any(word in subject_lower for word in prereq_lower.split() if len(word) > 3):
            return subject_name
    
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a subject dependency graph from a YAML file using Graphviz.")
    parser.add_argument("input_yaml_file", type=str, help="Path to the input YAML file containing subject data.")
    parser.add_argument("--format", type=str, default="png", help="Output format for the graph (e.g., 'png', 'pdf', 'svg'). Default is 'png'.")
    parser.add_argument("--no-view", action="store_true", help="Do not open the generated graph automatically.")

    args = parser.parse_args()

    generate_dependency_graph(args.input_yaml_file, output_format=args.format, view_graph=not args.no_view)