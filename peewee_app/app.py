import json
from flask import Flask, jsonify, request
from peewee import *
from playhouse.migrate import SchemaMigrator, migrate

app = Flask(__name__)

db = SqliteDatabase('peewee_app.db')


class User(Model):
    username = CharField(unique=True)
    email = CharField()

    class Meta:
        database = db

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }


def init_db():
    db.connect()
    db.create_tables([User], safe=True)


def migrate_add_column(table, column_name, field):
    migrator = SchemaMigrator.from_database(db)
    with db.atomic():
        migrate(migrator.add_column(table, column_name, field))


@app.route('/users', methods=['GET'])
def get_users():
    users = User.select()
    return jsonify([u.to_dict() for u in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.get_by_id(user_id)
        return jsonify(user.to_dict())
    except User.DoesNotExist:
        return jsonify({'error': 'User not found'}), 404


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User.create(username=data['username'], email=data['email'])
    return jsonify(user.to_dict()), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = User.get_by_id(user_id)
    except User.DoesNotExist:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.save()
    return jsonify(user.to_dict())


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.get_by_id(user_id)
    except User.DoesNotExist:
        return jsonify({'error': 'User not found'}), 404

    user.delete_instance()
    return jsonify({'message': 'User deleted'})


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
