from src import db
from sqlalchemy.orm import backref
from src.models.ProfileImages import ProfileImages


class Profile(db.Model):
    __tablename__ = 'profiles'

    profileid =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    account_active = db.Column(db.Boolean(), default = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    profile_image = db.relationship("ProfileImages", backref="profile", uselist=False)
    
    
    def __repr__(self):
        return f"<Profile {self.username}>"    
