from app.models.Shop import Shop, db
from app.services.UserService import UserService
from app import app
from app import app


class ShopService:
    @staticmethod
    def find_or_create_shop(telegram_id: int, name: CreateShopDto):
        try:
            user = UserService.find_or_create(telegram_id)
            user_id = user.id
            # with app.app_context():
            #     shop = Shop.query.filter_by(telegram_id=str(Shop.user_id == user_id, Shop.name == shop_name)).first()
            #     if shop != None:
            #         return shop
            shop = Shop()
            shop.name = shop_name
            shop.user_id = user_id
            with app.app_context():
                db.session.add(shop)
                db.session.commit()
        except Exception as e:
            print(str(e))
