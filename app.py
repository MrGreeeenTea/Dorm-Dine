from flask import Flask, render_template, redirect, url_for
import db, forms
from forms import LoginForm, RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

# landing page return redirect(url_for('index'))
@app.route('/')
def index():
    return render_template('index.html')
    
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

# Login return redirect(url_for('login'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    #db_con = db.get_db_con()
    form = forms.LoginForm()
    return render_template('login.html', title='Login', form=form)

# Register return redirect(url_for('register'))
@app.route('/register' , methods=['GET', 'POST'])
def register():
    #db_con = db.get_db_con()
    form = forms.RegisterForm()
    return render_template('register.html', title='Registrieren', form=form)

# Bestellübersicht
@app.route('/order_view')
def order_view():
    return redirect(url_for('order_view'))

# Fehlermeldungen
@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500