"""Health check routes."""

from datetime import UTC, datetime

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def health_check() -> dict[str, str | datetime]:
    """
    Health check endpoint.

    Returns the current status of the API.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now(UTC),
        "service": "ai-driven-fastapi-template",
    }


@router.get("/ready")
async def readiness_check() -> dict[str, bool]:
    """
    Readiness check endpoint.

    Returns whether the service is ready to accept requests.
    """
    return {
        "ready": True,
    }


@router.get("/live")
async def liveness_check() -> dict[str, bool]:
    """
    Liveness check endpoint.

    Returns whether the service is alive.
    """
    return {
        "alive": True,
    }
