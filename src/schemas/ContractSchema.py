from src import ma
from src.models.Contract import Contract
from marshmallow.validate import Length
from src.schemas.ProfileSchema import ProfileSchema


class ContractSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contract
    title = ma.String(required=True, validate=Length(min=1))
    availability = ma.String(required=False, validate=Length(min=1))
    capacity_in_days = ma.Int(required=True)
    hours_of_work = ma.Int(required=True)
    sector = ma.String(required=True, validate=Length(min=1))
    sub_sector = ma.String(required=True, validate=Length(min=1))
    skill_set = ma.String(required=True, validate=Length(min=1))
    location = ma.String(required=True, validate=Length(min=1))
    about = ma.String(required=True, validate=Length(min=1))
    resume = ma.String(required=True, validate=Length(min=1))
    profile = ma.Nested(ProfileSchema)

contract_schema = ContractSchema()
contracts_schema = ContractSchema(many=True)


