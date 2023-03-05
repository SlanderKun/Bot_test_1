from app.lib.db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128))
    telegram_id = db.Column(db.String(128))
    display_name = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    shops = db.relationship("Shop", backref="users")
