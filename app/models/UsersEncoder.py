import json
from json import JSONEncoder


class UsersEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
