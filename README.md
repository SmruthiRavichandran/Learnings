
# Learnings

## Overview
This repository contains various projects and exercises for learning and mastering essential tools and frameworks used in Machine Learning (ML) and MLOps. It covers topics such as **Flask**, **Git**, **MLFlow**, and other important components for building and deploying machine learning models.

### Key Features:
- **Flask**: Learn to build web applications and APIs for ML model deployment.
- **Git**: Version control and collaboration workflows.
- **MLFlow**: Experiment tracking, model management, and deployment for machine learning projects.
- **MLOps Concepts**: Understanding the necessary tools and practices for maintaining machine learning models in production.

## Setup and Requirements

### Prerequisites:
The prerequirements for each project is individualy added but if you want to run all the projects in one environment the below list is needed
1. Python 3.x
2. Required libraries:
   - `flask`
   - `mlflow`
   - `gitpython`
   - `numpy`
   - `pandas`

Install the dependencies using:
```bash
pip install -r requirements.txt
```

### Structure:
- **Flask**: A basic application using Flask to deploy ML models.
- **Git**: Includes tips and examples for using Git in ML projects.
- **MLFlow**: Contains examples on how to use MLFlow for tracking experiments and managing models.

## Example Usage:

### Running the Flask App:
To run the Flask application locally:
```bash
python app.py
```

### Using MLFlow:
Track experiments with MLFlow using the following commands:
```bash
mlflow run <project-directory>
```

---

## Detailed Documentation

### 1. Flask Integration
The Flask section contains examples on how to deploy machine learning models as RESTful APIs. Learn how to set up a basic Flask app, integrate it with model inference, and expose endpoints for prediction.

### 2. Git Workflow
This section covers the usage of **Git** for version control and collaboration in machine learning projects. It includes a guide on setting up a repository, committing changes, and managing branches.

### 3. MLFlow Integration
MLFlow is used here for managing machine learning experiments. This section demonstrates how to log model parameters, track metrics, and save models for future use. MLFlow provides a simple interface to track experiments and visualize results.

### 4. MLOps Pipeline
This section outlines the steps involved in building an MLOps pipeline, from model training to deployment. It includes tools and practices for continuous integration and deployment (CI/CD) in machine learning projects.

### Future Improvements
- Incorporate **Docker** for containerized deployments.
- Add more **real-world ML workflows** and **automated pipelines**.

---

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments
- Flask for building web APIs.
- MLFlow for managing experiments and models.
- Git for version control.

---
