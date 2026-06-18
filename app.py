from flask import Flask, render_template, redirect, request, url_for, flash, jsonify
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select


# Forms integration
import forms
from forms import RegisterForm, LoginForm, MealForm


# Database & Models setup
from db import db, insert_sample
from models import *
from models.user import User
from models.dorm import Dorm
from models.dish import Dish
from models.dish_order import DishOrder


app = Flask(__name__)


# configuration environment
app.config.from_mapping(
    SECRET_KEY = 'toller-secret-key',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse', # julia UI theme
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dormanddine.db',
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)


# Initialize extensions
db.init_app(app)
bootstrap = Bootstrap5(app)


login_manager = LoginManager()
login_manager.init_app(app)
# @login_required in front blocks access to routes for non-logged in users and redirects to login page
login_manager.login_view = 'login'


@login_manager.user_loader #für profiles später
def load_user(id):
    return db.session.get(User, id)


# create tables if they don't exist yet
with app.app_context():
    db.create_all()


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
@app.route('/dishes/<int:meal_id>')
def meal_detail(meal_id):
    dish = Dish.query.get_or_404(meal_id)
    return jsonify({
        "id": dish.id,
        "name": dish.name,
        "description": dish.description,
        "price": dish.price,
        "left_portions": dish.left_portions,
        "status": dish.status
    })


# post meals
@app.route('/post', methods=['GET', 'POST'])
@login_required
def post_meal():
    form = MealForm() #form object erstellen, html template frontend tool
   
    if form.validate_on_submit():
        # build Dish/ Meal using form data and database table format
        new_dish = Dish( #database model Dish, siehe models/dish.py
            cook_id = current_user.id,
            name = form.name.data,
            description = form.description.data,
            price = form.price.data,
            total_portions = form.portions.data,
            left_portions = form.portions.data,
            pickup_time = db.func.now(),  # Uses the DB clock, included bc we want to show the pickup time in the future, so that it appears in the feed
            status = form.status.data,
            ingredients = form.ingredients.data
        )
       
        db.session.add(new_dish)
        db.session.commit()
       
        flash('Dish was successfully added!', 'success') #success turns box green yay
        return redirect(url_for('dashboard'))
       
    return render_template('post_meal.html', form=form)


# Profil anzeigen
@app.route('/profile/<int:profil_id>')
def profil(profil_id):
    return "Coming soon", 200


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()


    if form.validate_on_submit(): #prüft ob POST und ob alle daten valid sind, wenn true, Flask WTF
        user = db.session.execute(
            select(User).filter_by(email=form.email.data)
        ).scalar_one_or_none() #user objekt oder none
        if not user: #wenn user none ist
            print("Noch nicht registriert")
        elif not user.check_password(form.password.data):
            print("password falsch")
        else:
            login_user(user)
            print("Erfolgreich")
            return redirect(url_for('dashboard'))


    return render_template('login.html', title='Login', form=form)


# Register
@app.route('/register' , methods=['GET', 'POST'])
def register():
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
        return redirect(url_for('dashboard'))


    return render_template('register.html', title='Registrieren', form=form)


# Bestellübersicht
@app.route('/order_view')
def order_view():
    return "Coming soon", 200


# Logout
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


#
@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500


# Dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    # use users assigned dorm profile, fallback to ID 1 if not set
    selected_dorm_id = current_user.dorm_id or 1 #or 1 to avoid errors for users without dorm assigned
    if request.method == 'POST' and 'dorm_id' in request.form: #this kinda overrides their chosen dorm_id, dunno if thats good
        selected_dorm_id = int(request.form.get('dorm_id'))

    # get dorm list from database
    dorms = db.session.execute(select(Dorm)).scalars().all()
    dorm_list = [{"id": d.id, "name": d.name, "adress": d.adress} for d in dorms]

    # get orders for current user
    orders = db.session.execute(
        select(DishOrder).filter_by(buyer_id=current_user.id)
    ).scalars().all()
   
    # build list of orders 
    my_orders = [] #means empty list
    for o in orders: #runs through orders n adds them
        my_orders.append({
            "id": o.id, #converts complexe to easy for jinja rendering
            "dish_id": o.dish_id,
            "dish_name": o.dish.name,
            "portions": o.portions,
            "price": float(o.dish.price),
            "status": o.status
        })

    # get meals created by this user
    my_dishes = db.session.execute(
        select(Dish).filter_by(cook_id=current_user.id)
    ).scalars().all()
   
   # build list of meals
    my_meals = [{
        "id": d.id,
        "name": d.name,
        "total_portions": d.total_portions,
        "status": d.status
    } for d in my_dishes]

    # show meals in selected dorm
    offers = db.session.execute(
        select(Dish)
        .join(User, Dish.cook_id == User.id)
        .filter(User.dorm_id == selected_dorm_id)
        .filter(Dish.status.in_(['scheduled', 'active'])) #so it wont show meals that are already completed
    ).scalars().all()

    # build list of meals
    current_offers = [{
        "id": o.id,
        "name": o.name,
        "description": o.description,
        "price": float(o.price),
        "total_portions": o.left_portions,
        "status": o.status
    } for o in offers]

    # render dashboard template with all the data
    return render_template(
        'dashboard.html',
        selected_dorm_id=selected_dorm_id,
        dorm_list=dorm_list,
        my_orders=my_orders,
        current_offers=current_offers,
        my_meals=my_meals
    )

# run app
if __name__ == '__main__':
    app.run(debug=True)
