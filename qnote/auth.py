from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import User
from bcrypt import hashpw, checkpw, gensalt

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    if request.method == 'POST':
        name = request.form.get('name').strip()
        email = request.form.get('email').strip()
        password = request.form.get('password').strip()
        confirm_password = request.form.get('c-password').strip()

        if password != confirm_password:
            return redirect(url_for('signup'))

        exists = User.query.filter_by(email=email).first()
        if exists:
            return redirect(url_for('signup'))

        password_hash = hashpw(password.encode('utf-8'), gensalt())
        new_user = User(
            name=name,
            email=email,
            password=password_hash.decode()
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('views.home'))

    return render_template('signup.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))

    if request.method == 'POST':
        email = request.form.get('email').strip()
        password = request.form.get('password').strip()

        user = User.query.filter_by(email=email).first()

        if user and checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            login_user(user)
            return redirect(url_for('views.home'))
        else:
            return redirect(url_for('auth.login'))

    return render_template('login.html')


@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
