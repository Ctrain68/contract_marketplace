from src import ma
from src.models.Engagement import Engagement
from marshmallow.validate import Length
from src.schemas.ContractSchema import ContractSchema


class EngagementSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Engagement
    title = ma.String(required=True, validate=Length(min=1))
    capacity_in_days = ma.Int(required=True, validate=Length(min=1))
    hours_of_work = ma.Int(required=True, validate=Length(min=1))
    start_date = ma.DateTime(required = True)
    end_date = ma.DateTime(required = True)
    contract = ma.Nested(ContractSchema)

engagement_schema = ProfileSchema()
engagements_schema = ProfileSchema(many=True)


