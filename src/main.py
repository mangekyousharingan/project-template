from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.adapters.api import health
from src.core.config import settings

app = FastAPI(
    title="Project Template",
    description="A template project using FastAPI with ports and adapters architecture",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router)


@app.get("/")
def root() -> str:
    return "Welcome to Project Template API"
