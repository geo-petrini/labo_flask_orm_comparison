# SQLAlchemy + Flask-Migrate Example

## Setup

```bash
pip install -r requirements.txt
```

## Initialize Migrations

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
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

## Migration Commands

```bash
flask db init          # Initialize migrations folder
flask db migrate       # Auto-generate migration from model changes
flask db upgrade       # Apply pending migrations
flask db downgrade     # Rollback last migration
flask db history       # Show migration history
flask db current       # Show current migration version
```
