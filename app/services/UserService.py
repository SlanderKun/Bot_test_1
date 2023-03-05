from app.models.User import User, db
from app.models.Shop import Shop
from app.models.Item import Item
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

    @staticmethod
    def create_shop(telegram_id: int):
        try:
            with app.app_context():
                user = User.query.filter_by(telegram_id=str(telegram_id)).first()
                print(user)
            id = user.id
            print(id)
            shop = Shop()
            shop.user_id = id
            with app.app_context():
                db.session.add(shop)
                db.session.commit()
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