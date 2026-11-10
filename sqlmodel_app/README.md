# SQLModel + Alembic Example

## Setup

```bash
pip install -r requirements.txt
```

## Initialize Alembic

```bash
alembic init migrations
```

## Configure migrations/env.py

Update `migrations/env.py`:

```python
from sqlmodel import SQLModel
from app import User  # Import all models

target_metadata = SQLModel.metadata
```

## Run

```bash
python app.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /users | List all users |
| GET | /users/1 | Get user by ID |
| POST | /users | Create user |
| PUT | /users/1 | Update user |
| DELETE | /users/1 | Delete user |

## Migration Commands (Alembic)

```bash
alembic init migrations                           # Initialize
alembic revision --autogenerate -m "description"  # Auto-generate
alembic upgrade head                              # Apply all
alembic downgrade -1                              # Rollback one
alembic history                                   # Show history
alembic current                                   # Show current version
```
