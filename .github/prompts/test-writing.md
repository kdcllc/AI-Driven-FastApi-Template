# Test Writing Prompt

Use this prompt when writing tests.

## Test Structure

```python
import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_{feature}_success():
    """Test {feature} with valid input."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.{method}("/api/endpoint", json={
            "field": "value"
        })
        
    assert response.status_code == 200
    data = response.json()
    assert data["field"] == "expected_value"


@pytest.mark.asyncio
async def test_{feature}_validation_error():
    """Test {feature} with invalid input."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.{method}("/api/endpoint", json={
            "field": ""  # Invalid empty value
        })
        
    assert response.status_code == 422
    

@pytest.mark.asyncio
async def test_{feature}_not_found():
    """Test {feature} when resource doesn't exist."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/endpoint/999")
        
    assert response.status_code == 404
```

## Test Categories

### 1. Happy Path Tests
- Test expected successful scenarios
- Verify correct data is returned
- Check status codes

### 2. Validation Tests
- Test with invalid data
- Test with missing fields
- Test with out-of-range values

### 3. Error Cases
- Test not found scenarios
- Test permission errors
- Test conflict situations

### 4. Edge Cases
- Test boundary values
- Test empty collections
- Test special characters

## Checklist
- [ ] Test happy path
- [ ] Test validation errors
- [ ] Test not found cases
- [ ] Test edge cases
- [ ] Use descriptive test names
- [ ] Add docstrings to tests
- [ ] Clean up test data
- [ ] Run tests and verify they pass
