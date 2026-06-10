from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
from app import app

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dormanddine.sqlite'

db = SQLAlchemy()
db.init_app(app)