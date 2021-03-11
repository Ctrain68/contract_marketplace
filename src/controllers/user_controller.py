from src.schemas.UserSchema import user_schema, users_schema
from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for
from src.models.User import User
from src import bcrypt, db
from flask_jwt_extended import create_access_token
from datetime import timedelta
# from src.forms.UserForm import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

auth = Blueprint('auth', __name__,)

#auth = Blueprint('auth', __name__, url_prefix="/auth")

# @auth.route("/register", methods=["GET", "POST"])
# def auth_register():
#     user_fields = user_schema.load(request.json)

#     user = User.query.filter_by(email=user_fields["email"]).first()

#     if user:
#         return abort(400, description="User already")
#     form = RegistrationForm()
# #     if form.validate_on_submit():
# #         user = User()
# #         user.email = form.email.data
# #         user.password = bcrypt.generate_password_hash(form.data.password).decode("utf-8")

# #         db.session.add(user)
# #         db.session.commit()
# #         return redirect(url_for('auth.login'))
# #     return render_template('register.html', title='Register', form=form)
# #     # return jsonify(user_schema.dump(user))


# @auth.route("/auth/register", methods=["POST"])
# def auth_register():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     #print(username)
#     #print(password)

#     #user_fields = user_schema.load(request.json)

#     #avoid to create a user that already exists
#     #user = User.query.filter_by(username=user_fields["username"]).first()
#     user = User.query.filter_by(email=email).first()
#     if user:
#         return abort(400, description="user already exists")

#     user = User()
#     #user.username = user_fields["username"]
#     #user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
#     user.email = email
#     user.password = bcrypt.generate_password_hash(password).decode("utf-8")

#     db.session.add(user)
#     db.session.commit()

#     #return jsonify(user_schema.dump(user))
#     return redirect(url_for('auth.login'))

# @auth.route("/auth/login", methods=["POST"])
# def auth_login():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     # print(username)
#     # print(password)
#     # user_fields = user_schema.load(request.json)

    
#     # user = User.query.filter_by(username=user_fields["username"]).first()
#     user = User.query.filter_by(email=email).first()
#     # don't login if the user doesn't exist
#     if not user: 
#         return abort(401, description="Incorrect email")
#     if not bcrypt.check_password_hash(user.password, password):
#         return abort(401, description="Incorrect password")
#     #print(current_user.username)
#     login_user(user)
#     print(current_user.email)
#     #expiry = timedelta(days=1)
#     #access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
#     #return jsonify({"token": access_token})
#     return redirect(url_for('profile.profile_sparkles'))


# # @auth.route("/login", methods=["POST"])
# # def auth_login():
# #     user_fields = user_schema.load(request.json)
# #     form = LoginForm()
# #     if form.validate_on_submit():

# #         user = User.query.filter_by(email=form.email.data).first()

# #     if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
# #         return abort(401, description="Incorrect username or password")

# #     expiry = timedelta(days=1)
# #     access_token = create_access_token(identity=str(user.id), expires_delta=expiry)

# #     return jsonify({ "token": access_token })



# @auth.route('/signup', methods=['GET'])
# def signup():
#     return render_template('signup.html')

# @auth.route('/login', methods=['GET'])
# def login():
#     return render_template('login.html')

# @auth.route('/logout', methods=['GET'])
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('profiles.home'))


@auth.route("/", methods=["GET", "POST"])
def auth_home():
    return render_template('home.html')




@auth.route("/register", methods=["POST"])
def auth_register():
    user_fields = user_schema.load(request.json)

    user = User.query.filter_by(email=user_fields["email"]).first()

    if user:
        return abort(400, description="User already")
    
    user = User()
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))


@auth.route("/login", methods=["POST"])
def auth_login():
    user_fields = user_schema.load(request.json)

    user = User.query.filter_by(email=user_fields["email"]).first()

    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username or password")

    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)

    return jsonify({ "token": access_token })