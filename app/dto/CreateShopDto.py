from app.dto.BaseDto import BaseDto


class CreateShopDto(BaseDto):
    name: str

    def __init__(self, config: dict):
        self.name = config['name']