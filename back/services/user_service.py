from ..models.note import User
from ..extensions import db
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def create_user(data):
    hashed_password = generate_password_hash(data.get('password'))
    user = User(
        username = data.get('username'),
        email = data.get('email'),
        password=hashed_password,
        created_at=datetime.now(timezone.utc)
    )
    
    db.session.add(user)
    db.session.commit()
    return user

def update_user(user_id, data):
    user = User.query.get(user_id)
    if user:
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        if data.get('password'):
            user.password = generate_password_hash(data.get('password'))
        db.session.commit()
    return user

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return user

def check_password(user, password):
    return check_password_hash(user.password, password)