from flask import Flask, render_template, redirect, url_for
import forms
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'toller-secret-key'

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
#@login_required
def post_meal():
    return redirect(url_for('post'))

# Profil anzeigen /<int: profil_id>
@app.route('/profile')
#wenn nicht angemeldet dann zu login weiterleiten
def profil():
    return redirect(url_for('profile'))

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    return render_template('login.html', title='Login', form=form)


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    return render_template('register.html', title='Registrieren', form=form)

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