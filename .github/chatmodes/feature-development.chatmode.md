# Feature Development Mode

## Purpose
This chat mode guides development of new features following best practices for AI-driven development.

## Workflow

### 1. Planning Phase
- Understand requirements clearly
- Break down into small, testable units
- Identify dependencies and impacts
- Plan API contracts (if applicable)

### 2. Implementation Phase
- Write tests first (TDD approach)
- Implement minimal working code
- Follow existing patterns in codebase
- Add type hints and documentation

### 3. Validation Phase
- Run tests and ensure they pass
- Check linting and formatting
- Verify API documentation
- Test edge cases manually

## Code Standards

### Python/FastAPI Best Practices
```python
# Use type hints
async def get_user(user_id: int) -> User | None:
    """Retrieve a user by ID."""
    pass

# Use Pydantic models for validation
class UserCreate(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=100)

# Proper error handling
from fastapi import HTTPException, status

if not user:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )
```

### Project Structure
```
src/app/
├── main.py              # FastAPI app initialization
├── core/
│   ├── config.py        # Configuration
│   └── security.py      # Security utilities
├── api/
│   └── routes/          # API endpoints
├── models/              # Database models
├── schemas/             # Pydantic schemas
└── services/            # Business logic
```

## Commit Messages
Follow conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `refactor:` Code refactoring
- `test:` Test additions/changes
- `chore:` Maintenance tasks
