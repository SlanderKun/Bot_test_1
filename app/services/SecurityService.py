from flask import abort
from app.models.User import User, db
from app import app
import secrets
import string


class Security:
    @classmethod
    def generate_token(cls):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(32))
        return password

    @staticmethod
    def authorization(token: str):
        if not token:
            abort(403)
        with app.app_context():
            user = User.query.filter_by(token=str(token)).first()
            if user == None:
                abort(403)

