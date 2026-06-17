from flask import Flask, render_template, redirect, url_for, flash
import forms
from forms import RegisterForm, LoginForm
from flask_login import LoginManager, login_user #https://flask-login.readthedocs.io/en/latest/
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select, func
from flask_bootstrap import Bootstrap5


from db import db, insert_sample
from models import *
from models.user import User
from models.dorm import Dorm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'toller-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dormanddine.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()

login_manager = LoginManager() 
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return db.session.get(User, id)

# landing page
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
    if form.validate_on_submit(): #prüft ob POST und ob alle daten valid sind, wenn true 
        user = db.session.execute(
            select(User).filter_by(email=form.email.data)
        ).scalar_one_or_none() #user objekt oder none
        if not user: #wenn user none ist
            flash('Bitte registrieren!', 'error')
            print("Fehler1")
        elif not user.check_password(form.password.data):
            flash('Zugangsdaten falsch!', 'error')
            print("Fehler2")
        else: 
            login_user(user)
            print("Erfolgreich")
            return redirect(url_for('index'))

    return render_template('login.html', title='Login', form=form)
    print("ausgeführt")


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()

    if form.validate_on_submit(): #Flask-WTF
        user = db.session.execute(
            select(User).filter_by(email=form.email.data)
        ).scalars().first()
        if user:
            flash('E-Mail bereits registriert!', 'error')
            print("Fehler4")
            return render_template('register.html', title='Registrieren', form=form)

        user = User(

            email = form.email.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            bio = form.bio.data or None,
            is_cook = form.is_cook.data,
            dorm_id = form.dorm_id.data,
            phone_number = form.phonenumber.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        print("erfolgreich registriert")
        return redirect(url_for('index'))

    return render_template('register.html', title='Registrieren', form=form)
    

# Bestellübersicht
@app.route('/order_view')
def order_view():
    return redirect(url_for('order_view'))

@app.route('/insert/sample')
def run_insert_sample():
    insert_sample()
    return 'Database flushed and populated with some sample data.'
# 
@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500

