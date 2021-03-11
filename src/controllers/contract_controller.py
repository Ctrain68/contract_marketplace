from flask import Blueprint, request, jsonify, abort, render_template
from src.schemas.ProfileSchema import profile_schema, profiles_schema
from src.schemas.ContractSchema import contract_schema, contracts_schema
from src.models.Contract import Contract
from src.models.Profile import Profile
from src.models.User import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.services.auth_services import verify_user
from sqlalchemy.sql import func, label
from sqlalchemy.orm import joinedload
from src import db
import os
import json



contract = Blueprint("contract", __name__, url_prefix="/contract")
    

   


@contract.route("/all", methods=["GET"])
def contract_index():
    query = db.session.query(Contract)

    return jsonify(contracts_schema.dump(query))





@contract.route("/", methods=["POST"])
@jwt_required
@verify_user
def contract_create(user=None):
    

    user_id = get_jwt_identity()

    profile = Profile.query.get(user_id)

    
    contract_fields = contract_schema.load(request.json)

    
    new_contract = Contract()
    new_contract.title = contract_fields["title"]
    new_contract.capacity_in_days = contract_fields["capacity_in_days"]
    new_contract.hours_of_work=contract_fields["hours_of_work"]
    new_contract.sector=contract_fields["sector"]
    new_contract.sub_sector=contract_fields["sub_sector"]
    new_contract.skill_set=contract_fields["skill_set"]
    new_contract.location=contract_fields["location"]
    new_contract.about=contract_fields["about"]
  

        
    profile.contract.append(new_contract)
        
    db.session.add(new_contract)
    db.session.commit()
        
    return jsonify(contract_schema.dump(new_contract))


@contract.route("/<string:title>", methods=["GET"])

def contract_show(title):
    #Return a singlecontract
    contract = Contract.query.filter_by(title = title).first()
    return jsonify(contract_schema.dump(contract))

@contract.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def contract_update(user, id):


    contract =Contract.query.filter_by(contractid = id, profile_id=user.id)
    
    contract_fields = contract_schema.load(request.json)

    if not contract:
        return abort(401, description="Unauthorised to update this user")
    
    
    contract.update(contract_fields)
    db.session.commit()
    
    return jsonify(contract_schema.dump(contract[0]))

@contract.route("/<int:id>", methods=["DELETE"])
@jwt_required
@verify_user
def contract_delete(user, id):


    contract =Contract.query.options(joinedload("profile")).filter_by(contractid = id, profile_id=user.id).first()
    # equipment = Equipment.query.options(joinedload("profile")).filter_by(id = id, owner_id=user.id).first()


    if not contract:
        return abort(400, description="Unauthorised to delete user")
    db.session.delete(contract)
    db.session.commit()

    return jsonify(contract_schema.dump(contract))





