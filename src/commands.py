from src import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from src.models.User import User
    from src.models.Profile import Profile
    from faker import Faker
    from src import bcrypt
    import random
    from random import seed
    from random import randint

    faker = Faker()
    profiles = []

    

    for i in range(10):
        user = User()
        user.email = f"test{i}@test.com"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        
    db.session.commit()

    for i in range(10):
        profile = Profile()
        profile.username = faker.name()
        profile.fname = faker.first_name()
        profile.lname = faker.last_name()
        profile.account_active=faker.boolean()
        profile.employer=faker.boolean()
        profile.contractor=faker.boolean()
        profile.user_id = i+1
        profiles.append(profile)
        db.session.add(profile)

    db.session.commit()

    print("Tables seeded")