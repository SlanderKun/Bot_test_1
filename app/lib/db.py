from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

class Factory:
    def __init__(self, DATABASE_URI, app):
        self.DATABASE_URI = DATABASE_URI
        self.app = app

    def make(self):
        self.app.config["SQLALCHEMY_DATABASE_URI"] = self.DATABASE_URI
        db.init_app(self.app)
        migrate = Migrate(self.app, db)





