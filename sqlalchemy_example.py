# SQLAlchemy Example

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'

# Create tables
with app.app_context():
    db.create_all()

# CRUD Operations
def create_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user

def get_user(username):
    stmt = db.select(User).filter_by(username=username)
    return db.session.execute(stmt).scalar_one_or_none()

def get_all_users():
    stmt = db.select(User)
    return db.session.execute(stmt).scalars().all()

def update_user_email(username, new_email):
    user = get_user(username)
    if user:
        user.email = new_email
        db.session.commit()
    return user

def delete_user(username):
    user = get_user(username)
    if user:
        db.session.delete(user)
        db.session.commit()
    return user

if __name__ == '__main__':
    with app.app_context():
        # Example usage
        user1 = create_user('john', 'john@example.com')
        user2 = create_user('jane', 'jane@example.com')
        
        print("All users:", get_all_users())
        print("John:", get_user('john'))
        
        update_user_email('john', 'john.doe@example.com')
        print("Updated John:", get_user('john'))
        
        delete_user('jane')
        print("After delete:", get_all_users())
