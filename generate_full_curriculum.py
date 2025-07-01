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

    # Generate a simple short name for the degree program for folder creation
    degree_short_name = "".join(c for c in degree_program if c.isalnum()).lower()
    if "computer science" in degree_program.lower():
        degree_short_name = "cs"
    elif "artificial intelligence" in degree_program.lower() or "machine learning" in degree_program.lower():
        degree_short_name = "aiml"
    elif "electronics and communication" in degree_program.lower() or "ec" in degree_program.lower():
        degree_short_name = "ec"
    
    if not degree_short_name:
        print(f"Warning: Could not determine a short name for '{degree_program}'. Using a generic name.")
        degree_short_name = "generated_degree"

    # --- Step 1: Generate Subjects ---
    subject_output_file = f"temp_{degree_short_name}_subjects.yaml"
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
        if os.path.exists(subject_output_file):
            os.remove(subject_output_file)
            print(f"Cleaned up temporary file: {subject_output_file}")

if __name__ == "__main__":
    main() 