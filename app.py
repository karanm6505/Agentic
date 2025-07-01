import os
from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import markdown
import subprocess # Import subprocess for running external scripts

app = Flask(__name__)

SYLLABUS_BASE_DIR = os.path.join(os.getcwd(), 'syllabuses')

def _get_syllabus_data():
    degree_programs = []
    if os.path.exists(SYLLABUS_BASE_DIR):
        for degree_name in os.listdir(SYLLABUS_BASE_DIR):
            degree_path = os.path.join(SYLLABUS_BASE_DIR, degree_name)
            if os.path.isdir(degree_path):
                semesters = []
                for sem_name in os.listdir(degree_path):
                    sem_path = os.path.join(degree_path, sem_name)
                    if os.path.isdir(sem_path) and sem_name.startswith('Sem_'):
                        subjects = []
                        for syllabus_file in os.listdir(sem_path):
                            if syllabus_file.endswith('.md'):
                                subject_name = os.path.splitext(syllabus_file)[0].replace('_Syllabus', '').replace('_', ' ')
                                subjects.append({
                                    'name': subject_name,
                                    'file': os.path.join(degree_name, sem_name, syllabus_file)
                                })
                        subjects.sort(key=lambda x: x['name'])
                        semesters.append({'name': sem_name, 'subjects': subjects})
                semesters.sort(key=lambda x: int(x['name'].replace('Sem_', '')))
                degree_programs.append({'name': degree_name, 'semesters': semesters})
    degree_programs.sort(key=lambda x: x['name'])
    return degree_programs

@app.context_processor
def inject_syllabus_data():
    return dict(degree_programs=_get_syllabus_data())

@app.route('/')
def index():
    message = request.args.get('message')
    return render_template('index.html', message=message)

@app.route('/generate_curriculum', methods=['POST'])
def generate_curriculum():
    degree_program = request.form.get('degree_program')
    if not degree_program:
        return redirect(url_for('index', message="Please provide a degree program."))

    # Run the generate_full_curriculum.py script as a subprocess
    try:
        # Start the process in the background. Do not wait for it to complete.
        subprocess.Popen([
            "python3", "generate_full_curriculum.py",
            "--degree-program", degree_program
        ])
        message = f"Generation for \'{degree_program}\' started in the background. It may take some time." \
                  f" Refresh the page to see updates in the sidebar navigation or main list."
    except Exception as e:
        message = f"Error starting generation: {e}"

    return redirect(url_for('index', message=message))

@app.route('/syllabus/<path:syllabus_path>')
def view_syllabus(syllabus_path):
    full_path = os.path.join(SYLLABUS_BASE_DIR, syllabus_path)
    if os.path.exists(full_path) and full_path.startswith(SYLLABUS_BASE_DIR):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        html_content = markdown.markdown(content)
        # Extract subject name from path for title
        subject_name = os.path.splitext(os.path.basename(syllabus_path))[0].replace('_Syllabus', '').replace('_', ' ')
        return render_template('syllabus.html', syllabus_content=html_content, subject_name=subject_name)
    return "Syllabus not found", 404

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    # Ensure markdown package is installed
    try:
        import markdown
    except ImportError:
        print("Markdown package not found. Installing now...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'markdown'])
        print("Markdown installed.")

    app.run(debug=True) 