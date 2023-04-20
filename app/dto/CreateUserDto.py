from app.dto.BaseDto import BaseDto


class CreateUserDto(BaseDto):
    name: str

    def __init__(self, config: dict):
        self.name = config['name']

