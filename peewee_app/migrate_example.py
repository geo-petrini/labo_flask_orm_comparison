# Peewee Migration Example
# Run this script to see how playhouse.migrate works

from peewee import *
from playhouse.migrate import SchemaMigrator, migrate

db = SqliteDatabase('peewee_migrate_example.db')


class User(Model):
    username = CharField(unique=True)
    email = CharField()

    class Meta:
        database = db


def main():
    db.connect()
    db.create_tables([User])

    print("=== Initial schema ===")
    print("User table created with: id, username, email")

    # Add a new column
    migrator = SchemaMigrator.from_database(db)
    bio_field = TextField(default='')

    print("\n=== Adding 'bio' column ===")
    with db.atomic():
        migrate(
            migrator.add_column('user', 'bio', bio_field),
        )
    print("Column 'bio' added successfully")

    # Insert a user with the new column
    user = User.create(username='john', email='john@example.com', bio='Hello world!')
    print(f"\nCreated user: {user.username}, bio: {user.bio}")

    # Rename a column
    print("\n=== Renaming 'bio' to 'biography' ===")
    with db.atomic():
        migrate(
            migrator.rename_column('user', 'bio', 'biography'),
        )
    print("Column renamed successfully")

    # Verify
    user = User.get_by_id(user.id)
    print(f"User bio after rename: {user.biography}")

    # Drop a column
    print("\n=== Dropping 'biography' column ===")
    with db.atomic():
        migrate(
            migrator.drop_column('user', 'biography'),
        )
    print("Column dropped successfully")

    db.close()
    print("\n=== Migration example complete ===")


if __name__ == '__main__':
    main()
