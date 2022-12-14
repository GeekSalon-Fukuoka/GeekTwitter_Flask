from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import Config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)