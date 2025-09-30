"""Example routes demonstrating FastAPI features."""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter()


class Item(BaseModel):
    """Example item model."""

    name: str = Field(..., description="Name of the item", min_length=1)
    description: str | None = Field(None, description="Optional description")
    price: float = Field(..., gt=0, description="Price must be greater than 0")
    quantity: int = Field(default=1, ge=1, description="Quantity must be at least 1")


class ItemResponse(BaseModel):
    """Example item response."""

    id: int
    name: str
    description: str | None
    price: float
    quantity: int
    total: float


# In-memory storage for demonstration
items_db: dict[int, Item] = {}
next_id = 1


@router.get("/")
async def list_items() -> dict[str, list[ItemResponse]]:
    """
    List all items.

    Returns a list of all stored items.
    """
    items = [
        ItemResponse(
            id=item_id,
            name=item.name,
            description=item.description,
            price=item.price,
            quantity=item.quantity,
            total=item.price * item.quantity,
        )
        for item_id, item in items_db.items()
    ]
    return {"items": items}


@router.get("/{item_id}")
async def get_item(item_id: int) -> ItemResponse:
    """
    Get a specific item by ID.

    Args:
        item_id: The ID of the item to retrieve

    Returns:
        The requested item

    Raises:
        HTTPException: If the item is not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

    item = items_db[item_id]
    return ItemResponse(
        id=item_id,
        name=item.name,
        description=item.description,
        price=item.price,
        quantity=item.quantity,
        total=item.price * item.quantity,
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item) -> ItemResponse:
    """
    Create a new item.

    Args:
        item: The item to create

    Returns:
        The created item with its assigned ID
    """
    global next_id
    item_id = next_id
    items_db[item_id] = item
    next_id += 1

    return ItemResponse(
        id=item_id,
        name=item.name,
        description=item.description,
        price=item.price,
        quantity=item.quantity,
        total=item.price * item.quantity,
    )


@router.put("/{item_id}")
async def update_item(item_id: int, item: Item) -> ItemResponse:
    """
    Update an existing item.

    Args:
        item_id: The ID of the item to update
        item: The updated item data

    Returns:
        The updated item

    Raises:
        HTTPException: If the item is not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

    items_db[item_id] = item

    return ItemResponse(
        id=item_id,
        name=item.name,
        description=item.description,
        price=item.price,
        quantity=item.quantity,
        total=item.price * item.quantity,
    )


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int) -> None:
    """
    Delete an item.

    Args:
        item_id: The ID of the item to delete

    Raises:
        HTTPException: If the item is not found
    """
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

    del items_db[item_id]
