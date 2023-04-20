from app.models.Shop import Shop, db
from app.services.UserService import UserService
from app.dto.CreateShopDto import CreateShopDto
from app import app


class ShopService:
    @staticmethod
    def find_or_create_shop(telegram_id: int, name: CreateShopDto):
        try:
            user = UserService.find_or_create(telegram_id)
            user_id = user.id
            name = name.name
            # with app.app_context():
            #     shop = Shop.query.filter_by(user_id=str( == user_id)).first()
            #     if shop != None:
            #         return shop
            shop = Shop()
            shop.name = name
            shop.user_id = user_id
            with app.app_context():
                db.session.add(shop)
                db.session.commit()
        except Exception as e:
            print(str(e))

    @staticmethod
    def find_all_shops():
        shops = Shop.query.all()
        print(shops)
        return shops
