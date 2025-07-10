import subprocess
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate subjects and syllabuses for a given degree program.")
    parser.add_argument("--degree-program", type=str, required=True, help="The full name of the degree program (e.g., 'Bachelor of Technology in Computer Science and Engineering').")
    parser.add_argument("--output-dir", type=str, default="./syllabuses", help="Base directory to save the generated syllabuses.")
    args = parser.parse_args()

    degree_program = args.degree_program
    base_output_dir = args.output_dir

    # Generate a unique directory name based on the degree program
    # Remove common words and create a meaningful short name
    import re
    
    # Clean the degree program name
    cleaned_name = degree_program.lower()
    
    # Remove common degree words
    common_words = ["bachelor", "master", "doctor", "of", "in", "and", "the", "technology", "science", "arts", "engineering"]
    for word in common_words:
        cleaned_name = cleaned_name.replace(word, "")
    
    # Remove extra spaces and special characters
    cleaned_name = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_name)
    cleaned_name = re.sub(r'\s+', '_', cleaned_name.strip())
    
    # If the cleaned name is too short, use a more descriptive approach
    if len(cleaned_name) < 3:
        # Extract key terms
        key_terms = []
        if "computer science" in degree_program.lower():
            key_terms.append("computer_science")
        if "artificial intelligence" in degree_program.lower():
            key_terms.append("ai")
        if "machine learning" in degree_program.lower():
            key_terms.append("ml")
        if "data science" in degree_program.lower():
            key_terms.append("data_science")
        if "electronics" in degree_program.lower():
            key_terms.append("electronics")
        if "communication" in degree_program.lower():
            key_terms.append("communication")
        if "time travel" in degree_program.lower():
            key_terms.append("time_travel")
        if "cybersecurity" in degree_program.lower():
            key_terms.append("cybersecurity")
        if "robotics" in degree_program.lower():
            key_terms.append("robotics")
        
        degree_short_name = "_".join(key_terms) if key_terms else "custom_degree"
    else:
        degree_short_name = cleaned_name
    
    # Ensure the name is not too long
    if len(degree_short_name) > 50:
        degree_short_name = degree_short_name[:50].rstrip('_')
    
    print(f"Using directory name: {degree_short_name}")

    # --- Step 1: Generate Subjects ---
    subject_output_file = f"{degree_program}_subjects.yaml"
    print(f"\n--- Step 1: Generating subjects for {degree_program} into {subject_output_file} ---")
    try:
        # Ensure python3 is used and pass all arguments correctly
        subject_cmd = [
            "python3", "subject_generator_agent.py",
            "--degree-program", degree_program,
            "--output-file", subject_output_file
        ]
        subprocess.run(subject_cmd, check=True, capture_output=False) # Keep capture_output=False for real-time visibility
        print(f"Subjects generated successfully to {subject_output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating subjects: {e}")
        if e.stderr:
            print(f"Stderr: {e.stderr.decode()}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: python3 command or subject_generator_agent.py not found. Make sure python3 is in your PATH and subject_generator_agent.py is in the current directory.")
        print("Aborting syllabus generation.")
        return

    # --- Step 2: Generate Syllabuses based on generated subjects ---
    print(f"\n--- Step 2: Generating syllabuses for {degree_program} ---")
    try:
        syllabus_cmd = [
            "python3", "batch_syllabus_generator.py",
            "--config-file", subject_output_file,
            "--degree-program-short-name", degree_short_name,
            "--base-output-dir", base_output_dir
        ]
        subprocess.run(syllabus_cmd, check=True, capture_output=False)
        print(f"Syllabuses generated successfully for {degree_program} in {os.path.join(base_output_dir, degree_short_name)}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating syllabuses: {e}")
        if e.stderr:
            print(f"Stderr: {e.stderr.decode()}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during syllabus generation: {e}")
        sys.exit(1)
    finally:
        # --- Cleanup: Remove temporary subject file ---
        pass # No cleanup, temporary file will be retained

if __name__ == "__main__":
    main() 