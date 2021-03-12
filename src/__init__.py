from dotenv import load_dotenv

load_dotenv()

from flask import Flask, jsonify
from marshmallow.exceptions import ValidationError
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager


db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()
# csrf = CSRFProtect()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("src.default_settings.app_config")

    # if app.config["ENV"] == "production":
    #     from log_handlers import file_handler
    #     app.logger.addHandler(file_handler)

    # from database import init_db
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    # csrf.init_app(app)

    from src.models.User import get_user

    @login_manager.user_loader
    def load_user(user_id):
        return get_user(user_id)
   

    from src.commands import db_commands
    app.register_blueprint(db_commands)

    from src.controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    from src.routes import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400)

    return app

