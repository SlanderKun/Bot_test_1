from app.dto.BaseDto import BaseDto


class CreateItemDto(BaseDto):
    name: str

    def __init__(self, config: dict):
        self.shop = config['shop']
        self.name = config['name']
        self.category = config['category']
        self.amount = config['amount']
