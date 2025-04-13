from fastapi import FastAPI

from src.adapters.api import health
from src.core.config import settings

app = FastAPI(
    title="Project Template",
    description="A template project using FastAPI with ports and adapters architecture",
    version="0.1.0",
    docs_url=None if settings.environment == "production" else "/docs",
    redoc_url=None if settings.environment == "production" else "/redoc",
)

# Include routers
app.include_router(health.router)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "status": "ok",
        "environment": settings.environment,
        "message": "Welcome to Project Template API",
    }
