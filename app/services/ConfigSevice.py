import os
from dotenv import load_dotenv


class ConfigService:

    def __init__(self):
        load_dotenv()

    def get(self, key):
        result = os.environ.get(key)
        return result


configService = ConfigService()
