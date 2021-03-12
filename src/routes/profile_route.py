from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for, flash
from src.models.User import User
from src.models.Profile import Profile
from src import bcrypt, db
from datetime import timedelta
from src.forms.ProfileForm import ProfileForm
from flask_login import login_user, current_user, logout_user, login_required, logout_user

profile_route = Blueprint('profile_route', __name__,)

@profile_route.route("/account", methods=["GET", "POST"])
@login_required
def profile_route_create():
    form = ProfileForm()

  

    print(current_user.id)

    if form.validate_on_submit():
        profile = Profile(username=form.username.data, fname=form.fname.data, lname=form.lname.data, 
                            employer=form.employer.data, contractor=form.contractor.data, user_id=current_user.id )
        db.session.add(profile)
        db.session.commit()
        flash('Your Profile has been has been created!', 'success')
        return redirect(url_for('user.user_home'))
    return render_template('create_profile.html', title='Profile',
                           form=form, legend='Profile')


@profile_route.route("/profile/<string:username>", methods=["GET"])
@login_required
def profile_route_profile(username):
    profile = Profile.query.filter_by(username = username).first()
    print("*****")
    print(profile)
    return render_template('profile.html', title=profile.fname, profile=profile)
    





