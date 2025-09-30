# API Endpoint Prompt

Use this prompt when creating new API endpoints.

## Template

```python
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter()


class {Resource}Create(BaseModel):
    """Schema for creating a {resource}."""
    
    # Add fields with validation
    name: str = Field(..., description="Resource name", min_length=1)


class {Resource}Response(BaseModel):
    """Schema for {resource} response."""
    
    id: int
    name: str


@router.get("/{id}")
async def get_{resource}({resource}_id: int) -> {Resource}Response:
    """
    Get a {resource} by ID.
    
    Args:
        {resource}_id: The ID of the {resource}
        
    Returns:
        The requested {resource}
        
    Raises:
        HTTPException: If {resource} not found
    """
    # Implementation
    pass


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_{resource}({resource}: {Resource}Create) -> {Resource}Response:
    """
    Create a new {resource}.
    
    Args:
        {resource}: The {resource} to create
        
    Returns:
        The created {resource}
    """
    # Implementation
    pass
```

## Checklist
- [ ] Define input schema with validation
- [ ] Define response schema
- [ ] Add proper HTTP status codes
- [ ] Include comprehensive docstrings
- [ ] Handle errors with HTTPException
- [ ] Add type hints
- [ ] Write tests for the endpoint
