from src import db
from sqlalchemy.orm import backref
from datetime import datetime



class Message(db.Model):
    __tablename__ = 'messages'

    messageid =db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(), nullable=False)
    message_sent = db.Column(db.Datetime(), nullable=False, default=datetime.now)
    profile_id = db.Column(db.Integer, db.ForeignKey("profile.profileid"), nullable=False)
    contract_id = db.Column(db.Integer, db.ForeignKey("contract.contractid"), nullable=False)


    
    
    def __repr__(self):
        return f"<Message {self.title}>"    
