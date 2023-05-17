from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from dotenv import load_dotenv

db = SQLAlchemy()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.secret_key = getenv('SECRET_KEY')
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

    db.init_app(app)

    from .models import User

    with app.app_context():
        db.create_all()

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.session_protection = 'strong'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @app.errorhandler(404)
    def invalid_route(e):
        return render_template('error.html', msg="404 Page not found")

    return app
