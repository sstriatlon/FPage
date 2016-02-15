from app import app, db
from app.models import User

def get_users():
    return User.query.all()