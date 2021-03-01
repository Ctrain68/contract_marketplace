from flask import Blueprint
from src.schemas.UserSchema import user_schema, users_schema
from flask import Blueprint, request, jsonify, abort
from src.models.User import User
from src import bcrypt, db
from flask_jwt_extended import create_access_token
from datetime import timedelta
from src.forms.UserForm import RegistrationForm, LoginForm

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def auth_register():
    user_fields = user_schema.load(request.json)

    user = User.query.filter_by(email=user_fields["email"]).first()

    if user:
        return abort(400, description="User already")
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.password = bcrypt.generate_password_hash(form.data.password).decode("utf-8")

        db.session.add(user)
        db.session.commit()

    return jsonify(user_schema.dump(user))


@auth.route("/login", methods=["POST"])
def auth_login():
    user_fields = user_schema.load(request.json)
    form = LoginForm()
    if form.validate_on_submit

        user = User.query.filter_by(email=user_fields["email"]).first()

    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username or password")

    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)

    return jsonify({ "token": access_token })