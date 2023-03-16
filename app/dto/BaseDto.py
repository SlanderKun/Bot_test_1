class BaseDto:
    @classmethod
    def load_from_string(cls, data: str):
        params = data.split(' ')
        result = {}
        for param in params:
            end = param.find('=')
            name = param[:end]
            value = param[end + 1:]
            result[name] = value
        dto = cls(result)
        return dto

    def __init__(self, config: dict):
        pass
