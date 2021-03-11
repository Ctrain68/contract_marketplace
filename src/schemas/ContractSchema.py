from src import ma
from src.models.Contract import Contract
from marshmallow.validate import Length
from src.schemas.ProfileSchema import ProfileSchema


class ContractSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contract
    title = ma.String(required=True, validate=Length(min=1))
    availability = ma.String(required=True, validate=Length(min=1))
    capacity_in_days = ma.Int(required=True, validate=Length(min=1))
    hours_of_work = ma.Int(required=True, validate=Length(min=1))
    sector = ma.String(required=True, validate=Length(min=1))
    sub-sector = ma.String(required=True, validate=Length(min=1))
    skill_set = ma.String(required=True, validate=Length(min=1))
    location = ma.String(required=True, validate=Length(min=1))
    about = ma.String(required=True, validate=Length(min=1))
    resume = ma.String(required=True, validate=Length(min=1))
    profile = ma.Nested(ProfileSchema)

contract_schema = ProfileSchema()
contracts_schema = ProfileSchema(many=True)

