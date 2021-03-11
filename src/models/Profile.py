from src import db
from sqlalchemy.orm import backref
from src.models.ProfileImages import ProfileImages
from src.models.Message import Messages
from src.models.Contract import Contract
from src.models.Engagement import Engagement


class Profile(db.Model):
    __tablename__ = 'profiles'

    profileid =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    fname = db.Column(db.String(), nullable=False)
    lname = db.Column(db.String(), nullable=False)
    account_active = db.Column(db.Boolean(), default = True)
    employer = db.Column(db.Boolean(), default = False)
    contractor = db.Column(db.Boolean(), default = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    profile_image = db.relationship("ProfileImages", backref="profile", uselist=False)
    contract = db.relationship("Contract", backref="contract")
    message = db.relationship("Message", backref="message")
    engagement = db.relationship("Engagement", backref="engagement")
    
    
    def __repr__(self):
        return f"<Profile {self.username}>"    
