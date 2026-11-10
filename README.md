# ORM Comparison

Complete Flask applications demonstrating each ORM with migrations.

## Examples

| Directory | ORM | Migration Tool | Flask Integration |
|-----------|-----|----------------|-------------------|
| `sqlalchemy_app/` | SQLAlchemy | Flask-Migrate (Alembic) | Flask-SQLAlchemy |
| `peewee_app/` | Peewee | playhouse.migrate | Manual |
| `sqlmodel_app/` | SQLModel | Alembic | Manual |
| `tortoise_app/` | Tortoise ORM | aerich | Limited (async) |

## Quick Start

### SQLAlchemy + Flask-Migrate

```bash
cd sqlalchemy_app
pip install -r requirements.txt
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python app.py
```

### Peewee + playhouse.migrate

```bash
cd peewee_app
pip install -r requirements.txt
python app.py

# Run migration example
python migrate_example.py
```

### SQLModel + Alembic

```bash
cd sqlmodel_app
pip install -r requirements.txt
alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
python app.py
```

### Tortoise ORM + aerich

```bash
cd tortoise_app
pip install -r requirements.txt
aerich init --db-url sqlite://tortoise_app.db
aerich init-db
```

## Migration Comparison

| Feature | Flask-Migrate | playhouse.migrate | Alembic | aerich |
|---------|---------------|-------------------|---------|--------|
| Auto-generate | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Versioning | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| CLI commands | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Rollback | ✅ Yes | Manual | ✅ Yes | ✅ Yes |
| Complexity | Low | Low | Medium | Medium |

## ORM Comparison

| Feature | SQLAlchemy | Peewee | SQLModel | Tortoise |
|---------|------------|--------|----------|----------|
| Syntax | `db.session.execute()` | `Model.select()` | `session.exec()` | `await Model.all()` |
| Learning Curve | Moderate | Easy | Easy | Easy |
| Async Support | Via greenlet | aiopewee | Native | Native |
| Performance | High | Medium | High | High |
| Flask Integration | Excellent | Manual | Manual | Limited |
| Best For | Complex apps | Simple apps | FastAPI | Async apps |
