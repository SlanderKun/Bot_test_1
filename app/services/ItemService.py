from app.models.Item import Item, db
from app.models.Shop import Shop
from app.services.ShopServise import ShopService
from app.dto.CreateShopDto import CreateShopDto
from app import app


class ItemService:
    @staticmethod
    def find_or_create(telegram_id: int, dto: CreateShopDto):
        try:
            shop = ShopService.find(telegram_id, dto.name)
            shop_id = shop.id

            item = Item()
            item.name = dto.name
            item.shop_id = shop_id
            item.category = dto.category
            item.amount = dto.amount
            with app.app_context():
                db.session.add(item)
                db.session.commit()
        except Exception as e:
            print(str(e))
