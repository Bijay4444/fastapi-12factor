# fastapi-12factor

A simple calculator FastAPI microservice demonstrating 12-Factor principles.

## Features
- Environment-based config
- Dockerized
- Simple test
- MkDocs documentation

## Usage

- Run locally: `uvicorn app.main:app --reload`
- Run with Docker: `docker-compose up --build`
- Test: `pytest`

## Endpoints

- `/health`
- `/calc?a=2&b=3&op=add`
