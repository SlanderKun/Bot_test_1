from app import app
from app.services import configService

if __name__ == '__main__':
    app.run(port=configService.get('PORT'))
