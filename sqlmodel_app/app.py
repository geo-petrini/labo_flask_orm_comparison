from typing import Optional
from flask import Flask, jsonify, request
from sqlmodel import SQLModel, Field, Session, select, create_engine

app = Flask(__name__)

DATABASE_URL = "sqlite:///sqlmodel_app.db"
engine = create_engine(DATABASE_URL)


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str = Field(unique=True, index=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


@app.route('/users', methods=['GET'])
def get_users():
    with Session(engine) as session:
        statement = select(User)
        users = session.exec(statement).all()
        return jsonify([{'id': u.id, 'username': u.username, 'email': u.email} for u in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email})


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    with Session(engine) as session:
        user = User(username=data['username'], email=data['email'])
        session.add(user)
        session.commit()
        session.refresh(user)
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        session.delete(user)
        session.commit()
        return jsonify({'message': 'User deleted'})


if __name__ == '__main__':
    create_db_and_tables()
    app.run(debug=True)
