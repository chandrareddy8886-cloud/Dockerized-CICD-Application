from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timezone
import os

app = FastAPI(
    title="Dockerized CI/CD Application",
    version=os.getenv("APP_VERSION", "1.0.0")
)

class HealthResponse(BaseModel):
    status: str
    version: str
    environment: str
    timestamp: str

@app.get("/")
def root():
    return {
        "message": "Dockerized CI/CD application is running",
        "docs": "/docs"
    }

@app.get("/health", response_model=HealthResponse)
def health():
    return {
        "status": "healthy",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("APP_ENV", "development"),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/version")
def version():
    return {
        "application": "dockerized-cicd-application",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "commit": os.getenv("GIT_COMMIT", "local")
    }
