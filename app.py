from flask import Flask

app = Flask(__name__)

# landing page
@app.route('/')
def index():
    return 'Hello, World!'

# feed von den meals
@app.route('/feed')
def feed():
    return 'Hello, World!'

# einzelne Gerichte
@app.route('/meal/<int:meal_id>')
def meal_detail(meal_id):
    return

# Gerichte posten
@app.route('/post', methods=['GET', 'POST'])
def post_meal():
    return

# Profil anzeigen
@app.route('/profile/<int: profil_id>')
def profil():
    return

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    return

# Register
@app.route('/register' , methods=['GET', 'POST'])
def register():
    return

# Bestellübersicht
@app.route('/order_view')
def order_view():
    return

# 
@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500