from fastapi import FastAPI

from .utils import add

app = FastAPI(title="DrBimmer OS API")

@app.get("/")
def read_root():
    """Root endpoint for health check."""
    return {"message": "DrBimmer OS API running"}

@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    """Simple addition endpoint used for testing."""
    return {"result": add(a, b)}
