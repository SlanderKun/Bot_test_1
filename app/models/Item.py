from app.lib.db import db
from datetime import datetime


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    category = db.Column(db.String(128))
    description = db.Column(db.String(128))
    amount = db.Column(db.String(128))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))
    user = db.relationship("Shop", backref=db.backref("shop", uselist=False))
