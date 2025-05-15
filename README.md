# To-Do List API 🚀

A FastAPI-based To-Do List application with in-memory storage, following 12-Factor App principles. Perfect for learning modern API development practices!

[![CI/CD](https://github.com/kabitajoc/todo-fastapi/actions/workflows/ci.yml/badge.svg)](https://github.com/kabitajoc/todo-fastapi/actions)
[![Docker](https://img.shields.io/badge/Docker-✓-blue.svg)](https://hub.docker.com/r/kabitajoc/todo-fastapi)

## Features ✨

- **CRUD Operations** for todo items
- Environment-specific configuration
- Docker containerization
- Automated CI/CD with GitHub Actions
- Pre-commit hooks for code quality
- Comprehensive test suite
- Interactive API documentation
- Health check endpoint

## Getting Started 🛠️

### Prerequisites

- Python 3.9+
- Docker 20.10+
- Git

## Project Structure 🗂

todo-fastapi/
├── .github/ # GitHub Actions workflows
├── app/ # Main application package
│ ├── core/ # Routing and core app logic
│ │ └── routes/
│ │ └── todos.py # Todo API routes
│ ├── schemas/ # Pydantic models
│ │ └── todo.py
│ └── **init**.py
├── docker/
│ └── Dockerfile # Docker configuration
├── env/ # Virtual environment
├── tests/ # Test suite
│ └── test_main.py
├── .gitignore
├── docker-compose.yml
├── pre-commit-config.yaml
├── pyproject.toml # Project config
├── README.md
└── requirements.txt

## Local Installation 💻

1. **Clone the repository**
   ```bash
   git clone https://github.com/kabitajoc/todo-fastapi.git
   cd todo-fastapi
   ```

## Running the API 🚀

### With Uvicorn (Locally)

```bash
uvicorn app.main:app --reload
```
