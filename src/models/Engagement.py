from src import db
from sqlalchemy.orm import backref
from datetime import datetime




class Engagement(db.Model):
    __tablename__ = 'engagement'

    engagementid =db.Column(db.Integer, primary_key=True)
    capacity_in_days = db.Column(db.Integer, nullable=False)
    hours_of_work = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    end_date = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    contract_rate = db.Column(db.String(), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.profileid"), nullable=False)
    contract_id = db.Column(db.Integer, db.ForeignKey("contracts.contractid"), nullable=False)

    
    
    def __repr__(self):
        return f"<Engagement {self.title}>"    
