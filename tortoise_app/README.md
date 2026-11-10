# Tortoise ORM + aerich Example

## Note

Tortoise is an **async ORM** designed for async frameworks like FastAPI or Quart. It's not the best fit for Flask (which is sync), but this example shows the model definition and migration setup.

## Setup

```bash
pip install -r requirements.txt
```

## Initialize aerich

```bash
aerich init --db-url sqlite://tortoise_app.db
aerich init-db
```

## aerich Commands

```bash
aerich init              # Initialize aerich
aerich init-db           # Create initial tables
aerich migrate           # Auto-generate migration
aerich upgrade           # Apply migration
aerich downgrade         # Rollback migration
aerich history           # Show migration history
```

## Model Definition

```python
from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=80, unique=True)
    email = fields.CharField(max_length=120, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user"
```

## Tortoise vs SQLAlchemy

| Feature | Tortoise | SQLAlchemy |
|---------|----------|------------|
| Async | Native | Via greenlet |
| Migrations | aerich | Flask-Migrate (Alembic) |
| Syntax | Django-like | SQLAlchemy-native |
| Flask Support | Limited | Excellent |
| Best For | Async apps (FastAPI) | Sync apps (Flask) |
