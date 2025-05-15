from fastapi import FastAPI, Query
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "12Factor Calculator"
    admin_email: str = "admin@example.com"

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI(title=settings.app_name)


@app.get("/calc")
def calculate(
    a: float = Query(..., description="First number"),
    b: float = Query(..., description="Second number"),
    op: str = Query(..., description="Operation: add, sub, mul, div")
):
    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        if b == 0:
            return {"error": "Division by zero"}
        result = a / b
    else:
        return {"error": "Invalid operation"}
    return {"result": result}
