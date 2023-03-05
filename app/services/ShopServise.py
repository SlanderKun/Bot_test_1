from app.models.Shop import Shop, db
from app.services.UserService import UserService
from app import app


class ShopService:
    @staticmethod
    def create_shop(telegram_id: int):
        try:
            user = UserService.find_or_create(telegram_id)
            id = user.id
            print(id)
            shop = Shop()
            shop.user_id = id
            with app.app_context():
                db.session.add(shop)
                db.session.commit()
        except Exception as e:
            print(str(e))
