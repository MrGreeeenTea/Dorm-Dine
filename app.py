from flask import Flask, render_template, redirect, url_for, jsonify, request
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
    dishes = db.session.execute(db.select(Dish).order_by(Dish.id)).scalars().all()
    return render_template('feed.html', dishes=dishes)

# einzelne Gerichte
@app.route('/dishes/<int:dish_id>')
def get_dish(dish_id):
    dish = db.get_or_404(Dish, dish_id)
    return render_template('meal_detail.html', dish=dish)

# Bestellübersicht
@app.route('/order_view/<int:dish_id>')
def order_view(dish_id):
    dish = db.get_or_404(Dish, dish_id)
    return render_template('order_view.html', dish = dish)

# Payment Success Cash
@app.route('/payment_success_cash/<int:dish_id>', methods=['POST'])
def payment_success_cash(dish_id):
    return complete_order(dish_id, "Cash")

# Payment Success PayPal
@app.route('/payment_success_paypal/<int:dish_id>', methods=['POST'])
def payment_success_paypal(dish_id):
    return complete_order(dish_id, "PayPal")

# Gerichte posten
@app.route('/post', methods=['GET', 'POST'])
def post_meal():
    return "Coming soon"

def complete_order(dish_id, payment_method):
    dish = db.get_or_404(Dish, dish_id)

    portions = request.form.get("portions", 1, type = int)

    if portions < 1:
        return render_template( 'order_view.html', dish = dish, error = "Please select at least one portion.")

    if portions > dish.left_portions:
        return render_template( 'order_view.html', dish = dish, error = "Not enough portions available.")
    
    dish.left_portions = dish.left_portions - portions
    db.session.commit()

    return render_template( 'payment_success.html', dish = dish, portions = portions, payment_method = payment_method)

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


# Dashboard 
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # Wohnheim wählen + speichern simulation
    # Defaults to the item from create_tables/ insert_sample
    selected_dorm_id = 1 
    if request.method == 'POST' and 'dorm_id' in request.form:
        selected_dorm_id = int(request.form.get('dorm_id'))

    # List of dormitories 
    dorm_list = [
        {"id": 1, "name": "Studentenwohnheim Mitte", "adress": "Musterstraße 12"},
        {"id": 2, "name": "Campus Wohnheim Wedding", "adress": "Amrumer Str. 20"},
        {"id": 3, "name": "Lichtenberg Apartments", "adress": "Einbecker Str. 45"}
    ]

    # meine bestellungen bsp
    meine_bestellungen = [
        {"id": 1, "dish_id": 1, "dish_name": "Lasagne", "portions": 2, "price": 2.00, "status": "pending", "message": "Thank you!"}
    ]

        # gerichte bsp
    meine_gerichte = [
        {"id": 1, "dish_id": 1, "name": "Lasagne", "price": 2.00, "total_portions": 6, "status": "scheduled"}
    ]

    # angebote bsp, angebot only shown if dorm 1 selected
    if selected_dorm_id == 1:
        aktuelle_angebote = [
            {"id": 1, "dish_id": 1, "name": "Lasagne", "description": "Traditional Italian pasta baked with rich meat sauce, layered with creamy béchamel and Gouda cheese.", "price": 2.00, "total_portions": 6, "status": "scheduled"}
        ]
    else:
        # Empty list if they select another dorm block!
        aktuelle_angebote = []


    # so my page opens
    return render_template(
        'dashboard.html',
        selected_dorm_id=selected_dorm_id,
        dorm_list=dorm_list,
        bestellungen=meine_bestellungen,
        angebote=aktuelle_angebote,
        gerichte=meine_gerichte
    )


if __name__ == '__main__':
    app.run(debug=True)