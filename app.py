from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)

from db import db, insert_sample
from models import *

bootstrap = Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dormanddine.db"

db.init_app(app)

with app.app_context():
    db.create_all()

# landing page
@app.route('/')
def index():
    return "Coming soon"

# feed von den meals
@app.route('/feed')
def feed():
    dishes = db.session.execute(db.select(Dish).order_by(Dish.id)).scalars()
    return render_template('feed.html', dishes=dishes)

# einzelne Gerichte
@app.route('/dishes/<int:dish_id>')
def get_dish(dish_id):
    dish = db.session.execute(Dish, dish.id).scalars()
    return jsonify({"id": dish.id, "name": dish.name, "description": dish.description, "price": dish.price, "left_portions": dish.left_portions, "status": dish.status})

# Gerichte posten
@app.route('/post', methods=['GET', 'POST'])
def post_meal():
    return "Coming soon"

# Profil anzeigen
@app.route('/profile/<int:profil_id>')
def profil(profil_id):
    return "Coming soon"

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    return "Coming soon"

# Register
@app.route('/register' , methods=['GET', 'POST'])
def register():
    return "Coming soon"

# Bestellübersicht
@app.route('/order_view')
def order_view():
    return "Coming soon"

@app.route('/insert/sample')
def run_insert_sample():
    insert_sample()
    return 'Database flushed and populated with some sample data.'

@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500