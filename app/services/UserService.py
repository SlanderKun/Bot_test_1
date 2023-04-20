from app.models.User import User, db
from app.services.SecurityService import Security
from app.models.BaseModel import BaseModel
from app.models.Item import Item
from app import app


class UserService:

    @staticmethod
    def find_or_create(telegram_id: int, username=None):
        with app.app_context():
            user = User.query.filter_by(telegram_id=str(telegram_id)).first()
            print(user)

            if user != None:
                if not user.is_active:
                    user.is_active = True
                    db.session.commit()
                return user

        user = User()
        user.username = username
        user.display_name = username
        user.telegram_id = telegram_id
        with app.app_context():
            db.session.add(user)
            db.session.commit()
        return user

    @staticmethod
    def change_display_name(telegram_id: int, display_name: str):
        try:
            with app.app_context():
                user = User.query.filter_by(telegram_id=str(telegram_id)).first()

                if user == None:
                    return user
                user.display_name = display_name
                db.session.commit()
                return user
        except Exception as e:
            print(str(e))

    @staticmethod
    def find_shops(telegram_id: int):
        try:
            with app.app_context():
                user = User.query.filter_by(telegram_id=str(telegram_id)).first()
            print(user)
            id = user.id

        except Exception as e:
            print(str(e))

    @staticmethod
    def update_token(telegram_id: int):
        with app.app_context():
            user = User.query.filter_by(telegram_id=str(telegram_id)).first()
            token = Security.generate_token()
            user.token = token
            db.session.commit()
        return token

