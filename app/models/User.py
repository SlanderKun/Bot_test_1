import json
from app.lib.db import db
from app.models.BaseModel import BaseModel


class User(db.Model, BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128))
    telegram_id = db.Column(db.String(128))
    display_name = db.Column(db.String(128))
    token = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    shops = db.relationship("Shop", backref="users")

    def to_dict(self):
        return {"id": self.id, "username": self.username}


