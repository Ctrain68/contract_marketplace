from flask import Blueprint, request, jsonify, abort, render_template
from src.schemas.EngagementSchema import engagement_schema, engagements_schema
from src.models.Engagement import Engagement
from src.models.Profile import Profile
from src.models.User import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.services.auth_services import verify_user
from sqlalchemy.sql import func, label
from sqlalchemy.orm import joinedload
from src import db
import os
import json



engagement = Blueprint("engagement", __name__, url_prefix="/contract/engagement")
    

   


# @engagement.route("/all", methods=["GET"])
# def engagement_index():
#     query = db.session.query(Engagement)

#     return jsonify(engagements_schema.dump(query))






# @engagement.route("/", methods=["POST"])
# @jwt_required
# @verify_user
# def engagement_create(user=None):
    

#     user_id = get_jwt_identity()

    
#     engagement_fields = engagement_schema.load(request.json)

#     contract = Contract.query.get(profile_id)

#     if not engagement:
    
#         new_engagement = Engagement()
#         new_engagement.capacity_in_days = engagement_fields["capacity_in_days"]
#         new_engagement.hours_of_work = engagement_fields["hours_of_work"]
#         new_engagement.start_date = engagement_fields["start_date"]
#         new_engagement.end_date=engagement_fields["end_date"]
#         new_engagement.contract_rate=engagement_fields["contract_rate"]
        
        
#         contract.engagement.append(new_engagement)
        
#         db.session.add(new_engagement)
#         db.session.commit()
        
#         return jsonify(profile_schema.dump(new_profile))
    
#     else:
#         return abort(401, description='User Profile already exists')

# @engagement.route("/<string:username>", methods=["GET"])

# def engagement_show(username):
#     #Return a single user
#     profile = Profile.query.filter_by(username = username).first()
#     return jsonify(profile_schema.dump(profile))

# @engagement.route("/<int:id>", methods=["PUT", "PATCH"])
# @jwt_required
# @verify_user
# def engagment_update(user, id):


#     profile = Profile.query.filter_by(profileid = id, user_id=user.id)
    
#     profile_fields = profile_schema.load(request.json)

#     if not profile:
#         return abort(401, description="Unauthorised to update this user")
    
    
#     profile.update(profile_fields)
#     db.session.commit()
    
#     return jsonify(profile_schema.dump(profile[0]))

# @engagement.route("/<int:id>", methods=["DELETE"])
# @jwt_required
# @verify_user
# def engagement_delete(user, id):


#     profile = Profile.query.filter_by(profileid = id, user_id=user.id).first()


#     if not profile:
#         return abort(400, description="Unauthorised to delete user")
#     db.session.delete(profile)
#     db.session.commit()

#     return jsonify(profile_schema.dump(profile))





