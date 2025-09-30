# Debugging Mode

## Purpose
Systematic approach to identifying and fixing bugs.

## Debugging Process

### 1. Reproduce the Issue
- Understand the exact steps to reproduce
- Identify expected vs actual behavior
- Check error messages and stack traces
- Review recent changes

### 2. Gather Information
- Check application logs
- Review relevant code sections
- Examine test failures
- Check dependency versions

### 3. Isolate the Problem
- Use minimal reproduction case
- Add debug logging
- Use debugger breakpoints
- Test hypotheses systematically

### 4. Fix and Validate
- Implement the fix
- Add regression tests
- Verify fix doesn't break other functionality
- Update documentation if needed

## Common FastAPI Issues

### Issue: CORS Errors
```python
# Solution: Configure CORS middleware
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Issue: Async/Await Errors
```python
# Wrong: Calling async function without await
result = async_function()

# Correct: Await async functions
result = await async_function()
```

### Issue: Pydantic Validation
```python
# Check model definition matches input
class User(BaseModel):
    email: str  # Should be EmailStr?
    age: int = Field(ge=0)  # Add validation
```

## Debugging Tools
- Use `uvicorn --log-level debug` for verbose output
- Add `import pdb; pdb.set_trace()` for breakpoints
- Use VS Code debugger (see .vscode/launch.json)
- Check FastAPI's automatic docs at `/api/docs`
