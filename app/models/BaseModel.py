from app.models.User import db
from app import app


class BaseModel:
    @staticmethod
    def find_by_key(cls, value: any, key: any):
        with app.app_context():
            search = cls.query.filter_by(key=str(value)).first()
        return search
