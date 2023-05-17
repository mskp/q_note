from . import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(20), nullable=False)
    email: str = db.Column(db.String(50), unique=True, nullable=False)
    password: str = db.Column(db.String(255), nullable=False)
    created_on: str = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now())

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True if self.id is not None else False

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }


class Notes(db.Model, UserMixin):
    __tablename__ = 'notes'
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False)
    title: str = db.Column(db.String(70), nullable=False)
    description: str = db.Column(db.String(1000), nullable=False)
    created_on: str = db.Column(
        db.DateTime(), nullable=False, default=lambda: datetime.now())

    def to_dict(self):
        return {
            'id': self.title,
            'name': self.description
        }
