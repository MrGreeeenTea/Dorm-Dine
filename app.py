import sqlite3
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# landing page
@app.route('/')
def index():
    return redirect(url_for('index'))

# feed von den meals
@app.route('/feed')
def feed():
    return redirect(url_for('feed'))

# einzelne Gerichte
@app.route('/meal/<int:meal_id>')
def meal_detail(meal_id):
    return redirect(url_for('meal'))

# Gerichte posten
@app.route('/post', methods=['GET', 'POST'])
def post_meal():
    return redirect(url_for('post'))

# Profil anzeigen
@app.route('/profile/<int:profil_id>')
def profil():
    return redirect(url_for('profile'))

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    return redirect(url_for('login'))

# Register
@app.route('/register' , methods=['GET', 'POST'])
def register():
    return redirect(url_for('register'))

# Bestellübersicht
@app.route('/order_view')
def order_view():
    return redirect(url_for('order_view'))

# 
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
    # defaults to the item from create_tables/ insert_sample
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
        # empty list if they select another dorm
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