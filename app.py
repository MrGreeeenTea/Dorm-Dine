from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)


# landing page
@app.route('/')
def index():
    return redirect(url_for('feed'))

# feed von den meals
@app.route('/feed')
def feed():
    return render_template('feed.html')

# einzelne Gerichte
@app.route('/meal/<int:meal_id>')
def meal_detail(meal_id):
    return render_template('meal_detail.html')

# einzelne Gerichte
@app.route('/payment_success_cash')
def payment_success_cash():
    return render_template('payment_success_cash.html')

# einzelne Gerichte
@app.route('/payment_success_paypal')
def payment_success_paypal():
    return render_template('payment_success_paypal.html')

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
    return render_template('order_view.html')

# 
@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500