"""Tests for health check endpoints."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    """Test the health check endpoint."""
    response = await client.get("/api/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert data["service"] == "ai-driven-fastapi-template"


@pytest.mark.asyncio
async def test_readiness_check(client: AsyncClient):
    """Test the readiness check endpoint."""
    response = await client.get("/api/health/ready")

    assert response.status_code == 200
    data = response.json()
    assert data["ready"] is True


@pytest.mark.asyncio
async def test_liveness_check(client: AsyncClient):
    """Test the liveness check endpoint."""
    response = await client.get("/api/health/live")

    assert response.status_code == 200
    data = response.json()
    assert data["alive"] is True
