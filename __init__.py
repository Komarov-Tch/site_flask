# В app.py уже создаётся приложение Flask. После переноса настройки базы
# в app.py этот файл можно оставить пустым.
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
