from src import db
from sqlalchemy.orm import backref
from datetime import datetime



class Contract(db.Model):
    __tablename__ = 'contracts'

    contractid =db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    availability = db.Column(db.Datetime(), nullable=False, default=datetime.now)
    capacity_in_days = db.Column(db.Integer, nullable=False)
    hours_of_work = db.Column(db.Integer, nullable=False)
    sector = db.Column(db.String(), nullable=False)
    sub-sector = db.Column(db.String(), nullable=False)
    skill_set = db.Column(db.String(), nullable=False)
    location = db.Column(db.String(), nullable=False)
    about = db.Column(db.String(), nullable=False)
    resume = db.Column(filename = db.Column(db.String()))
    profile_id = db.Column(db.Integer, db.ForeignKey("profile.profileid"), nullable=False)
    message = db.relationship("Message", backref="message")
    engagement = db.relationship("Engagement", backref="engagement")

    
    
    def __repr__(self):
        return f"<Contract {self.title}>"    
