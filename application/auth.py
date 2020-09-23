from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('We cannot find your email account. Did you sign up yet?')
            return redirect(url_for('auth.login'))
        else:
            if password is not user.password:
                print("pass\n\n\n")
                flash('Your password is incorrect, please try again')
                return redirect(url_for('auth.login'))
            else:
                print("skip\n\n\n")
                login_user(user, remember=remember)
                return redirect(url_for('main.profile'))

    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        fName = request.form.get('fName')
        lName = request.form.get('lName')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Account already exists')
            return redirect(url_for('auth.signup'))  # Redirects to the signup page
        
        else:
            new_user = User(email=email, password=password, firstName=fName, lastName=lName)
            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for('auth.login'))
    
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'