"""Tests for example endpoints."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root_endpoint(client: AsyncClient):
    """Test the root endpoint."""
    response = await client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["docs"] == "/api/docs"
    assert data["health"] == "/api/health"


@pytest.mark.asyncio
async def test_create_item(client: AsyncClient):
    """Test creating a new item."""
    response = await client.post(
        "/api/example/",
        json={"name": "Test Item", "description": "A test item", "price": 19.99, "quantity": 5},
    )

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "A test item"
    assert data["price"] == 19.99
    assert data["quantity"] == 5
    assert abs(data["total"] - 99.95) < 0.01  # Use approximate comparison for floats
    assert "id" in data


@pytest.mark.asyncio
async def test_create_item_validation_error(client: AsyncClient):
    """Test creating an item with invalid data."""
    response = await client.post(
        "/api/example/",
        json={
            "name": "",  # Empty name should fail
            "price": -10,  # Negative price should fail
        },
    )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_list_items_empty(client: AsyncClient):
    """Test listing items when none exist."""
    response = await client.get("/api/example/")

    assert response.status_code == 200
    data = response.json()
    assert "items" in data


@pytest.mark.asyncio
async def test_get_item_not_found(client: AsyncClient):
    """Test getting a non-existent item."""
    response = await client.get("/api/example/999")

    assert response.status_code == 404
    data = response.json()
    assert "detail" in data


@pytest.mark.asyncio
async def test_item_crud_operations(client: AsyncClient):
    """Test complete CRUD operations on an item."""
    # Create
    create_response = await client.post(
        "/api/example/",
        json={
            "name": "CRUD Test Item",
            "description": "Testing CRUD",
            "price": 25.00,
            "quantity": 3,
        },
    )
    assert create_response.status_code == 201
    item_id = create_response.json()["id"]

    # Read
    get_response = await client.get(f"/api/example/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "CRUD Test Item"

    # Update
    update_response = await client.put(
        f"/api/example/{item_id}",
        json={
            "name": "Updated Item",
            "description": "Updated description",
            "price": 30.00,
            "quantity": 2,
        },
    )
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Updated Item"
    assert update_response.json()["total"] == 60.00

    # Delete
    delete_response = await client.delete(f"/api/example/{item_id}")
    assert delete_response.status_code == 204

    # Verify deletion
    get_deleted = await client.get(f"/api/example/{item_id}")
    assert get_deleted.status_code == 404
