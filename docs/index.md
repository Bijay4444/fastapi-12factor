# fastapi-12factor

A simple 12-Factor-compliant FastAPI calculator microservice.

## Endpoints

- `/health` - Health check
- `/calc?a=2&b=3&op=add` - Calculator (add, sub, mul, div)

## How to Run

docker-compose up --build


## Or locally:

uvicorn app.main:app --reload

