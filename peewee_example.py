# Peewee Example

from peewee import *

db = SqliteDatabase('peewee_example.db')

class User(Model):
    username = CharField(unique=True)
    email = CharField()
    
    class Meta:
        database = db

# Create tables
db.connect()
db.create_tables([User])

# CRUD Operations
def create_user(username, email):
    return User.create(username=username, email=email)

def get_user(username):
    try:
        return User.get(User.username == username)
    except User.DoesNotExist:
        return None

def get_all_users():
    return list(User.select())

def update_user_email(username, new_email):
    user = get_user(username)
    if user:
        user.email = new_email
        user.save()
    return user

def delete_user(username):
    user = get_user(username)
    if user:
        user.delete_instance()
    return user

if __name__ == '__main__':
    # Example usage
    user1 = create_user('john', 'john@example.com')
    user2 = create_user('jane', 'jane@example.com')
    
    print("All users:", get_all_users())
    print("John:", get_user('john'))
    
    update_user_email('john', 'john.doe@example.com')
    print("Updated John:", get_user('john'))
    
    delete_user('jane')
    print("After delete:", get_all_users())
    
    db.close()
