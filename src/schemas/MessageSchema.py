from src import ma
from src.models.Message import Message
from marshmallow.validate import Length
from src.schemas.ContractSchema import ContractSchema


class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
    message = ma.String(required=True, validate=Length(min=1))
    message_sent = ma.Int(required=True, validate=Length(min=1))
    contract = ma.Nested(ProfileSchema)

message_schema = ProfileSchema()
messsages_schema = ProfileSchema(many=True)


