from src import db
from sqlalchemy.orm import backref
from src.models.Profile import Profile
from flask_login import UserMixin

def get_user(user_id):
    user=User.query.filter_by(id=user_id).first()
    return user


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    profile = db.relationship("Profile", backref=backref("user", uselist=False))
    def __repr__(self):
        return f"<Users {self.email}>"