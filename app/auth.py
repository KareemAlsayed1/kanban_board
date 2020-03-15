from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash
from .models import users
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('index.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('pwd1')

    user = users.query.filter_by(email=email).first() 

    if user: 
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = users(email=email.lower(), first_name=first_name,last_name=last_name, 
    password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    
    logged_user = users.query.filter_by(email=email).first()

    login_user(logged_user, remember=False)

    return redirect(url_for('main.board'))

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email').lower()
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = users.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page
    
    login_user(user, remember=remember)
    return redirect(url_for('main.board'))

@auth.route('/signout')
@login_required
def logout():
    
    logout_user()
    return redirect(url_for('main.index'))