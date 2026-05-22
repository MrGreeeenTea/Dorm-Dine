from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

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
@app.route('/profile/<int: profil_id>')
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