from app.lib.db import db


class Shop(db.Model):
    __tablename__ = "shops"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    description = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    user = db.relationship("User", backref=db.backref("user", uselist=False))
    items = db.relationship("Item", backref="shops")