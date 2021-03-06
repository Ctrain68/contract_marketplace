from flask import Blueprint, request, jsonify, abort, render_template
from src.schemas.MessageSchema import message_schema, messages_schema
from src.models.Message import Message
from src.models.Profile import Profile
from src.models.User import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.services.auth_services import verify_user
from sqlalchemy.sql import func, label
from src import db
import os
import json



message = Blueprint("message", __name__, url_prefix="/contract/message")
    

   


@message.route("/all", methods=["GET"])
def message_index():
    query = db.session.query(Message)

    return jsonify(messages_schema.dump(query))


# @messag.route("/active", methods=["GET"])
# def messag_index_active():
 
#     query = db.session.query(Profile).filter(Profile.account_active).order_by(Profile.fname)
#     return jsonify(profiles_schema.dump(query))




# @messag.route("/", methods=["POST"])
# @jwt_required
# @verify_user
# def messag_create(user=None):
    

#     user_id = get_jwt_identity()

    
#     profile_fields = profile_schema.load(request.json)

#     profile = Profile.query.get(user_id)

#     if not profile:
    
#         new_profile = Profile()
#         new_profile.username = profile_fields["username"]
#         new_profile.fname = profile_fields["fname"]
#         new_profile.lname = profile_fields["lname"]
#         new_profile.account_active=profile_fields["account_active"]
#         new_profile.employer=profile_fields["employer"]
#         new_profile.employer=profile_fields["contractor"]
        
#         user.profile.append(new_profile)
        
#         db.session.add(new_profile)
#         db.session.commit()
        
#         return jsonify(profile_schema.dump(new_profile))
    
#     else:
#         return abort(401, description='User Profile already exists')

# @messag.route("/<string:username>", methods=["GET"])

# def messag_show(username):
#     #Return a single user
#     profile = Profile.query.filter_by(username = username).first()
#     return jsonify(profile_schema.dump(profile))

# @messag.route("/<int:id>", methods=["PUT", "PATCH"])
# @jwt_required
# @verify_user
# def messag_update(user, id):


#     profile = Profile.query.filter_by(profileid = id, user_id=user.id)
    
#     profile_fields = profile_schema.load(request.json)

#     if not profile:
#         return abort(401, description="Unauthorised to update this user")
    
    
#     profile.update(profile_fields)
#     db.session.commit()
    
#     return jsonify(profile_schema.dump(profile[0]))

# @messag.route("/<int:id>", methods=["DELETE"])
# @jwt_required
# @verify_user
# def messag_delete(user, id):


#     profile = Profile.query.filter_by(profileid = id, user_id=user.id).first()


#     if not profile:
#         return abort(400, description="Unauthorised to delete user")
#     db.session.delete(profile)
#     db.session.commit()

#     return jsonify(profile_schema.dump(profile))





