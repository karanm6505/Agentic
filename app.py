import os
from flask import Flask, render_template, request, redirect, url_for
import markdown
import yaml
import subprocess

app = Flask(__name__)

SYLLABUS_BASE_DIR = "./syllabuses"

def get_syllabus_structure():
    structure = {}
    if not os.path.exists(SYLLABUS_BASE_DIR):
        return structure

    for degree_program_short_name in sorted(os.listdir(SYLLABUS_BASE_DIR)):
        degree_path = os.path.join(SYLLABUS_BASE_DIR, degree_program_short_name)
        if os.path.isdir(degree_path):
            semesters = {}
            for sem_folder in sorted(os.listdir(degree_path)):
                sem_path = os.path.join(degree_path, sem_folder)
                if os.path.isdir(sem_path) and sem_folder.startswith("Sem_"):
                    subject_files = []
                    for subject_file in sorted(os.listdir(sem_path)):
                        if subject_file.endswith(".md"):
                            subject_files.append(subject_file.replace("_Syllabus.md", "").replace("_", " "))
                    if subject_files:
                        semesters[sem_folder] = sorted(subject_files)
            if semesters:
                structure[degree_program_short_name] = semesters
    return structure

@app.route('/')
def index():
    syllabus_structure = get_syllabus_structure()
    message = request.args.get('message')
    return render_template('index.html', syllabus_structure=syllabus_structure, message=message)

@app.route('/syllabus/<path:syllabus_path>')
def view_syllabus(syllabus_path):
    # Ensure the path is safe and within the SYLLABUS_BASE_DIR
    full_path = os.path.join(SYLLABUS_BASE_DIR, syllabus_path + ".md")
    full_path = os.path.normpath(full_path)

    if not full_path.startswith(os.path.normpath(SYLLABUS_BASE_DIR)):
        return "Invalid syllabus path", 400

    if not os.path.exists(full_path):
        return "Syllabus not found", 404

    with open(full_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    html_content = markdown.markdown(markdown_content)

    # Extract subject title from the filename for display
    subject_title = os.path.basename(syllabus_path).replace("_", " ")

    return render_template('syllabus.html', title=subject_title, content=html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 