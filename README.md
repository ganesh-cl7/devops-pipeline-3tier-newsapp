# Flask React CI/CD

A simple project demonstrating a CI/CD pipeline integrating a Flask backend with a React frontend. This repository includes Docker configuration and GitHub Actions workflows for automated testing and deployment.

## Project Structure

- **backend_flask/**: Contains the Flask API backend.
- **frontend_react/**: Contains the React frontend application.
- **.github/workflows/**: GitHub Actions configuration files for CI/CD.
- **docker-compose.yml**: Orchestrates both the backend and frontend services using Docker Compose.

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

### Installation

Clone the repository and change into the project directory:

```bash
git clone https://github.com/regostar/flask_react_ci_cd.git
cd flask_react_ci_cd
```
## Running the Application

Build and start the services with Docker Compose:

```bash
docker-compose up --build
```

### By Default

- The **React frontend** will be available at [http://localhost:3000](http://localhost:3000)
- The **Flask backend API** will run at [http://localhost:5000](http://localhost:5000)

### CI/CD

This repository is set up with GitHub Actions to automatically run tests and build Docker images on commits and pull requests. The CI/CD configuration can be found in the `.github/workflows` directory.
