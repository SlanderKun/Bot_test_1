from app.dto.BaseDto import BaseDto


class CreateShopDto(BaseDto):
    name: str

    def __init__(self, config: dict):
        self.name = config['name']
        self.user_id = config['user_id']
