from app.lib.db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    telegram_id = db.Column(db.String)
    display_name = db.Column(db.String)

