from app.models.User import User, db
from app import app


class UserService:

    @staticmethod
    def find_or_create(telegram_id: int, username: str):
        try:
            with app.app_context():
                user = User.query.filter_by(telegram_id=str(telegram_id)).first()
            if user != None:
                return user
            user = User()
            user.username = username
            user.telegram_id = telegram_id
            with app.app_context():
                db.session.add(user)
                db.session.commit()
            return user
        except Exception as e:
            print(str(e))

    @staticmethod
    def add_display_name(telegram_id: int, display_name: str):
        try:
            with app.app_context():
                user = User.query.filter_by(telegram_id=str(telegram_id)).first()
            print(user.display_name)
            if user == None:
                return user
            user.display_name = display_name
            print(user.display_name)
            with app.app_context():
                db.session.commit()
            return user
        except Exception as e:
            print(str(e))

            