from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dormanddine.sqlite'

db = SQLAlchemy()
db.init_app(app)
