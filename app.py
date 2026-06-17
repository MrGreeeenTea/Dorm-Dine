from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap5

#for userauth
import forms
from forms import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user #https://flask-login.readthedocs.io/en/latest/
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)

from db import db, insert_sample
from models import *
from models.user import User
from models.dorm import Dorm


bootstrap = Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dormanddine.db"

db.init_app(app)

with app.app_context():
    db.create_all()

login_manager = LoginManager() 
login_manager.init_app(app)

@login_manager.user_loader #für profiles später Login
def load_user(id): #Erklärt die DB für LoginManaager
    return db.session.get(User, id) #SQL Alchemy fswd

# landing page
@app.route('/')
def index():
    return "Coming soon", 200

# feed von den meals
@app.route('/feed')
def feed():
    dishes = db.session.execute(db.select(Dish).order_by(Dish.id)).scalars()
    return render_template('feed.html', dishes=dishes)

# einzelne Gerichte
@app.route('/dishes/<int:dish_id>')
def get_dish(dish_id):
    dish = Dish.query.get_or_404(dish_id)
    return jsonify({"id": dish.id, "name": dish.name, "description": dish.description, "price": dish.price, "left_portions": dish.left_portions, "status": dish.status})

# Gerichte posten
@app.route('/post', methods=['GET', 'POST'])
def post_meal():
    return "Coming soon", 200

# Profil anzeigen
@app.route('/profile/<username>')
def profile(username):
    profile_user = db.session.execute(
            select(User).filter_by(username=username)  
        ).scalar_one_or_none()
    
    if not profile_user:
        print("existiert nicht")
        return render_template('404.html'), 404
    
    #für die Edit Logik
    #is_my_profile = (
        #current_user.is_authenticated and
        #current_user.id == profile_user.id
    #)
    
    return render_template('profile.html', profile_user=profile_user)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('feed'))

    form = forms.LoginForm()

    if form.validate_on_submit(): #prüft ob POST und ob alle daten valid sind, Flask WTF
        user = db.session.execute(
            select(User).filter_by(email=form.email.data)  
        ).scalar_one_or_none()  #SQL Alchemy fswd 
        if not user: #wenn user none ist
            print("Noch nicht registriert")
        elif not user.check_password(form.password.data):
            print("password falsch")
        else: 
            login_user(user)
            print("Erfolgreich")
            return redirect(url_for('feed'))

    return render_template('login.html', title='Login', form=form)

# Register
@app.route('/register' , methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('feed'))

    form = forms.RegisterForm()

    if form.validate_on_submit(): 
        user = db.session.execute(
            select(User).filter_by(email=form.email.data)
        ).scalars().first()
        if user:
            print('E-Mail bereits registriert!')
            return render_template('register.html', title='Registrieren', form=form)
        
        user = db.session.execute(
            select(User).filter_by(username=form.username.data)
        ).scalars().first()
        if user:
            print('Username existiert bereits!')
            return render_template('register.html', title='Registrieren', form=form)
        
        user = db.session.execute(
           select(User).filter_by(phone_number=form.phonenumber.data)
        ).scalars().first()
        if user:
            print('Username existiert bereits!')
            return render_template('register.html', title='Registrieren', form=form)


        user = User(

            email = form.email.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
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
        return redirect(url_for('feed'))

    return render_template('register.html', title='Registrieren', form=form)

# Bestellübersicht
@app.route('/order_view')
def order_view():
    return "Coming soon", 200

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()   #Flask Login
    print("ausgeloggt")
    return redirect(url_for('index'))

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