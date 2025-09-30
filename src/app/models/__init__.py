"""Database models package.

This package contains database models (e.g., SQLAlchemy, Tortoise ORM).
Add your database models here when integrating a database.

Example structure:
- user.py: User model
- item.py: Item model
- base.py: Base model with common fields

For SQLAlchemy example:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
```

For Tortoise ORM example:
```python
from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    name = fields.CharField(max_length=255)

    class Meta:
        table = "users"
```
"""
