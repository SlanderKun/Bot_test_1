from app.lib.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    verified = db.Column(db.Boolean)

    # @staticmethod
    # def user_create():