# AI Coding Agent Instructions

## Project Architecture

This is a **UV-managed FastAPI template** optimized for AI-driven development. Key architectural decisions:

- **UV Package Manager**: Use `uv` commands instead of pip/poetry. Core workflow: `uv sync` for dependencies, `uv run` for execution
- **Structured FastAPI App**: Located in `src/app/` with clear separation between API routes, core config, models, and schemas
- **Pydantic-Settings Configuration**: All settings in `src/app/core/config.py` using environment variables via `.env`
- **Router-Based API**: Endpoints organized in `src/app/api/routes/` with separate routers included in `main.py`

## Essential Workflows

### Development Commands (via Makefile)

- `make install` - Install dependencies using UV
- `make dev` - Install with dev dependencies
- `make run` - Start development server on port 1212
- `make test` - Run pytest with async support
- `make lint` - Run ruff + mypy checks
- `make format` - Auto-format code with ruff

### Server Startup Patterns

- **Development**: `cd src && uv run python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 1212`
- **Alternative**: `cd src && uv run python run.py`
- **API Docs**: Available at `/api/docs` and `/api/redoc`

## Code Patterns & Conventions

### FastAPI Route Structure

```python
# In src/app/api/routes/{feature}.py
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter()

class ItemCreate(BaseModel):
    name: str = Field(..., description="Item name", min_length=1)
    price: float = Field(..., gt=0)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate) -> ItemResponse:
    """Create new item with validation and proper status codes."""
```

### Configuration Pattern

- All settings inherit from `BaseSettings` in `src/app/core/config.py`
- Use environment variables with `.env` file support
- Access via global `settings` instance imported from config

### Testing Patterns

- Async test client via `conftest.py` fixture: `async def test_func(client: AsyncClient)`
- In-memory storage for demo endpoints (see `src/app/api/routes/example.py`)
- Comprehensive CRUD testing with proper HTTP status code validation

## Project-Specific Conventions

### Type Hints & Validation

- Use modern Python 3.11+ union syntax: `str | None` instead of `Optional[str]`
- Pydantic Field validation with descriptive messages
- Return type annotations on all endpoints

### Error Handling

- Use `HTTPException` with proper status codes from `fastapi.status`
- Include descriptive error messages in `detail` field
- Example: `HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")`

### API Design

- **All endpoints prefixed**: `/api/{feature}`
- **Health checks**: Available at `/api/health`, `/api/health/ready`, `/api/health/live`
- **Documentation URLs**: Custom paths `/api/docs`, `/api/redoc`, `/api/openapi.json`

## Integration Points

### Core Dependencies

- **FastAPI 0.115+**: Modern async framework with automatic OpenAPI
- **Pydantic 2.9+**: Data validation and settings management
- **UV**: Replaces pip/poetry for faster dependency management
- **Ruff**: Combined linting and formatting (replaces black, isort, flake8)

### Development Tools Integration

- **MyPy**: Strict type checking configured in `pyproject.toml`
- **Pytest**: Async mode enabled with `asyncio_mode = "auto"`
- **VS Code**: Pre-configured with debug launch configurations

## AI-Specific Features

### Chat Modes Available

- **Feature Development**: `.github/chatmodes/feature-development.chatmode.md` - TDD workflow guidance
- **Code Review**: Focus on security and best practices
- **Debugging**: Systematic issue investigation

### Prompt Templates

- **API Endpoint**: `.github/prompts/api-endpoint.prompt.md` - Complete CRUD endpoint template
- **Test Writing**: Comprehensive testing patterns
- **Refactoring**: Safe refactoring practices

## Key Files for Context

- `src/app/main.py` - FastAPI app initialization with CORS and router inclusion
- `src/app/core/config.py` - Pydantic settings with environment variable support
- `src/app/api/routes/example.py` - Complete CRUD example with in-memory storage
- `tests/conftest.py` - Async test client setup
- `pyproject.toml` - UV project configuration with ruff and mypy settings

## Common Gotchas

- **UV Commands**: Always prefix Python execution with `uv run` in this project
- **Working Directory**: API server commands must run from `src/` directory
- **Port 1212**: Default development port, not 8000
- **CORS Configuration**: Pre-configured for localhost development in `config.py`
- **Import Paths**: Use `from app.` for internal imports (app is the package in src/)
