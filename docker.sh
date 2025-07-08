#!/bin/bash

# Syllabus Generator Docker Helper Script

case "$1" in
    "build")
        echo "Building Docker image..."
        docker build -t syllabus-generator .
        ;;
    "run")
        echo "Running container on port 8080..."
        docker run -p 8080:5000 -v $(pwd)/syllabuses:/app/syllabuses syllabus-generator
        ;;
    "run-dev")
        echo "Running in development mode on port 8080..."
        docker run -p 8080:5000 -v $(pwd):/app -e FLASK_DEBUG=1 syllabus-generator
        ;;
    "compose-up")
        echo "Starting with docker-compose..."
        docker-compose up
        ;;
    "compose-up-dev")
        echo "Starting development environment with docker-compose..."
        docker-compose up syllabus-generator-dev
        ;;
    "compose-down")
        echo "Stopping docker-compose services..."
        docker-compose down
        ;;
    "clean")
        echo "Cleaning up Docker images and containers..."
        docker-compose down
        docker rmi syllabus-generator 2>/dev/null || true
        docker system prune -f
        ;;
    *)
        echo "Usage: $0 {build|run|run-dev|compose-up|compose-up-dev|compose-down|clean}"
        echo ""
        echo "Commands:"
        echo "  build         - Build the Docker image"
        echo "  run           - Run the container on port 8080 (production mode)"
        echo "  run-dev       - Run the container on port 8080 (development mode)"
        echo "  compose-up    - Start services with docker-compose (production)"
        echo "  compose-up-dev - Start services with docker-compose (development)"
        echo "  compose-down  - Stop docker-compose services"
        echo "  clean         - Clean up Docker images and containers"
        exit 1
        ;;
esac
