# Peewee + playhouse.migrate Example

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Migration Example

```bash
python migrate_example.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /users | List all users |
| GET | /users/1 | Get user by ID |
| POST | /users | Create user |
| PUT | /users/1 | Update user |
| DELETE | /users/1 | Delete user |

## Migration Commands (Manual)

Peewee migrations are written as Python scripts, not CLI commands:

```python
from playhouse.migrate import SchemaMigrator, migrate

migrator = SchemaMigrator.from_database(db)

# Add column
with db.atomic():
    migrate(
        migrator.add_column('user', 'bio', TextField(default='')),
    )

# Rename column
with db.atomic():
    migrate(
        migrator.rename_column('user', 'bio', 'biography'),
    )

# Drop column
with db.atomic():
    migrate(
        migrator.drop_column('user', 'biography'),
    )
```

## Supported Operations

- Add, rename, or drop columns
- Make columns nullable or not nullable
- Change column type
- Rename table
- Add/drop indexes and constraints
- Add/drop column defaults
