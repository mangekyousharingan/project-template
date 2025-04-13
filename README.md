# Project Template

A modern Python project template using FastAPI with ports and adapters (hexagonal) architecture, PostgreSQL, SQLAlchemy, and Alembic.

## Features

- FastAPI web framework
- PostgreSQL database with SQLAlchemy ORM
- Alembic for database migrations
- Docker and Docker Compose setup
- Poetry for dependency management
- Ports and Adapters (Hexagonal) Architecture
- Health check endpoint
- CORS middleware
- Environment-based configuration
- Type hints and modern Python practices

## Prerequisites

- Docker and Docker Compose
- Python 3.12+
- Poetry (for local development)

## Getting Started

1. Clone this template:
```bash
git clone <your-repo-url>
cd project-template
```

2. Create a `.env` file (already provided with default values)

3. Start the application:
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Available Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint

## Project Structure

```
src/
├── adapters/           # External adapters (API, database, etc.)
│   ├── api/           # API endpoints and routers
│   └── database/      # Database configuration and models
├── core/              # Core business logic
│   ├── entities/      # Domain entities
│   ├── ports/         # Port interfaces
│   └── services/      # Business logic services
└── main.py           # Application entry point
```

## Database Migrations

To create a new migration:
```bash
alembic revision --autogenerate -m "description"
```

To apply migrations:
```bash
alembic upgrade head
```

## Development

1. Install dependencies:
```bash
poetry install
```

2. Run tests:
```bash
poetry run pytest
```

3. Format code:
```bash
poetry run black .
poetry run isort .
```

## License

MIT
