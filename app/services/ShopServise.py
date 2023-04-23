from app.models.Shop import Shop, db
from app.services.UserService import UserService
from app.dto.CreateShopDto import CreateShopDto
from app import app


class ShopService:
    @staticmethod
    def create(telegram_id: int, dto: CreateShopDto):
        try:
            user = UserService.find_or_create(telegram_id)
            user_id = user.id

            shop = ShopService.find(telegram_id)
            if shop != None:
                return False

            shop = Shop()
            shop.name = dto.name
            shop.user_id = user_id
            with app.app_context():
                db.session.add(shop)
                db.session.commit()
        except Exception as e:
            print(str(e))

    @staticmethod
    def find(telegram_id: int, name: str):
        user = UserService.find_or_create(telegram_id)
        with app.app_context():
            shop = Shop.query.filter_by(user_id=int(user.id), name=str(name)).first()
            return shop

    @staticmethod
    def find_all_shops():
        shops = Shop.query.all()
        shops_name = []
        for name in shops:
            shops_name = shops_name.append(name)
        return shops_name

    @staticmethod
    def find_shops_by_id(telegram_id: int):
        user = UserService.find_or_create(telegram_id)
        with app.app_context():
            shops = Shop.query.filter_by(user_id=int(user.id))
        return shops

