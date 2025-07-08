# Syllabus Generator

An AI-powered Flask web application that generates comprehensive course syllabuses for various degree programs using Google's Gemini AI and LangChain.

## Features

- **AI-Powered Syllabus Generation**: Uses Google Gemini AI to create detailed, structured syllabuses
- **Multiple Degree Programs**: Supports Computer Science, AI/ML, Electronics & Communication, and custom programs
- **Dependency Graph Generation**: Creates visual dependency graphs showing prerequisite relationships
- **Web Interface**: Clean, responsive Flask web application for viewing generated syllabuses
- **Batch Processing**: Generate entire curricula for degree programs
- **Docker Support**: Containerized deployment with Docker and Docker Compose
- **Modular Architecture**: Separate agents for subject generation and syllabus creation

## Quick Start

### Prerequisites

- Python 3.11+
- Google API Key for Gemini AI
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd syllabusGen
   ```

2. **Set up environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

   Visit `http://localhost:5000` to access the web interface.

   **Note**: If port 5000 is already in use (common on macOS), the Docker setup uses alternative ports:
   - Docker single container: `http://localhost:5001`
   - Docker Compose production: `http://localhost:5001`
   - Docker Compose development: `http://localhost:5002`

## Docker Deployment

### Using Docker Helper Script (Recommended)

```bash
# Make script executable
chmod +x docker.sh

# Build and run
./docker.sh build
./docker.sh compose-up
```

### Available Docker Commands

- `./docker.sh build` - Build the Docker image
- `./docker.sh run` - Run container (production mode)
- `./docker.sh run-dev` - Run container (development mode)
- `./docker.sh compose-up` - Start with docker-compose (production)
- `./docker.sh compose-up-dev` - Start with docker-compose (development)
- `./docker.sh compose-down` - Stop services
- `./docker.sh clean` - Clean up Docker images and containers

### Manual Docker Commands

```bash
# Build image
docker build -t syllabus-generator .

# Run container
docker run -p 5001:5000 -v $(pwd)/syllabuses:/app/syllabuses syllabus-generator

# Using docker-compose
docker-compose up
```

**Access the application:**
- Direct Docker run: `http://localhost:5001`
- Docker Compose (production): `http://localhost:5001`  
- Docker Compose (development): `http://localhost:5002`

## Project Structure

```
syllabusGen/
├── app.py                          # Main Flask web application
├── batch_syllabus_generator.py     # Batch syllabus generation
├── subject_generator_agent.py      # AI agent for generating subjects
├── syllabus_agent.py              # AI agent for creating syllabuses
├── generate_dependency_graph.py    # Creates prerequisite dependency graphs
├── generate_full_curriculum.py     # End-to-end curriculum generation
├── courses.yaml                    # Sample course configurations
├── my_aiml_subjects.yaml          # AI/ML program structure
├── my_ec_subjects.yaml            # EC program structure
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker configuration
├── docker-compose.yml            # Docker Compose configuration
├── docker.sh                     # Docker helper script
├── .dockerignore                  # Docker ignore file
├── static/                        # CSS and JavaScript files
│   ├── style.css
│   └── script.js
├── templates/                     # HTML templates
│   ├── base.html
│   ├── index.html
│   └── syllabus.html
└── syllabuses/                    # Generated syllabuses
    ├── CSE/                       # Computer Science Engineering
    ├── ec/                        # Electronics & Communication
    └── [other-programs]/
```

## Usage

### Web Interface

1. Start the application using any of the methods above
2. Navigate to `http://localhost:5000`
3. Browse generated syllabuses by degree program and semester
4. Click on any subject to view its detailed syllabus

### Command Line Tools

#### Generate Complete Curriculum

```bash
python generate_full_curriculum.py --degree-program "Bachelor of Technology in Computer Science and Engineering"
```

#### Generate Subjects Only

```bash
python subject_generator_agent.py --degree-program "Bachelor of Technology in Artificial Intelligence and Machine Learning" --output-file aiml_subjects.yaml
```

#### Generate Syllabuses from Existing Subjects

```bash
python batch_syllabus_generator.py --config-file my_aiml_subjects.yaml --degree-program-short-name aiml --base-output-dir ./syllabuses
```

#### Create Dependency Graph

```bash
python generate_dependency_graph.py my_aiml_subjects.yaml --format png
```

## Configuration Files

### Course Configuration (courses.yaml)
```yaml
- subject: "Artificial Intelligence Fundamentals"
  level: "Undergraduate"
  duration_weeks: 14
  focus: "Introduction to AI concepts, problem-solving, and basic machine learning."
  assessments: "Weekly assignments, a midterm, and a final project."
```

### Subject Structure (my_aiml_subjects.yaml)
```yaml
- semester_number: 1
  subjects:
    - subject: "Introduction to Programming"
      level: "Undergraduate"
      assessments: "Coding assignments, quizzes, and a final exam."
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Gemini AI API key | Yes |
| `FLASK_ENV` | Flask environment (development/production) | No |
| `FLASK_DEBUG` | Enable Flask debug mode | No |

## Generated Content

The application generates:

- **Detailed Syllabuses**: Complete course syllabuses with learning objectives, weekly schedules, assessments, and resources
- **Dependency Graphs**: Visual representations of course prerequisites
- **Structured Curricula**: Organized by degree program and semester
- **Markdown Format**: All syllabuses in readable Markdown format

## AI Agents

### Subject Generator Agent
- Generates comprehensive subject lists for degree programs
- Uses web search to research current industry standards
- Creates structured YAML output with subject details

### Syllabus Agent
- Creates detailed syllabuses for individual subjects
- Includes learning objectives, weekly schedules, assessments
- Incorporates current industry practices and resources

## Features

- **Responsive Design**: Modern, clean web interface
- **Real-time Generation**: AI-powered content creation
- **Persistent Storage**: Generated content saved to filesystem
- **Modular Architecture**: Separate components for different functionalities
- **Docker Support**: Easy deployment and scaling

## Troubleshooting

### Common Issues

1. **API Key Issues**
   - Ensure your Google API key is correctly set in `.env`
   - Check that the Gemini AI API is enabled in your Google Cloud project

2. **Dependency Conflicts**
   - Use the provided `requirements.txt` with compatible versions
   - Consider using a virtual environment

3. **Docker Issues**
   - Ensure Docker is running
   - Check port availability (Docker uses ports 5001-5002 to avoid conflicts with macOS Control Center on port 5000)

### Logs and Debugging

- Application logs are printed to console
- For Docker: `docker-compose logs syllabus-generator`
- Enable Flask debug mode for development


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini AI for natural language processing
- LangChain for AI agent framework
- Flask for web framework
- Graphviz for dependency visualization

---
