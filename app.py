from flask import Flask, render_template, redirect, request, url_for, flash, jsonify
from flask_bootstrap import Bootstrap5
from datetime import datetime

#for userauth
import forms
from forms import *
from flask_login import LoginManager, login_user, logout_user, login_required, current_user #Flask-Login
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select


app = Flask(__name__)


# configuration environment
app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)

from db import db, insert_sample
from models import *

bootstrap = Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dormanddine.db"
db.init_app(app)

# Sucht nach Keywords, ansonsten wird ein Others Bild angezeigt
ICON_KEYWORDS = {
    "pizza":   ["pizza", "margherita", "salami pizza", "flammkuchen"],
    "burger":  ["burger", "hamburger", "cheeseburger", "patty", "bun"],
    "burrito": ["burrito", "wrap", "taco", "tacos", "quesadilla", "fajita",
                "tortilla", "mexican", "mexikanisch"],
    "pasta":   ["pasta", "spaghetti", "nudel", "nudeln", "noodle", "noodles",
                "lasagne", "lasagna", "penne", "tagliatelle", "carbonara",
                "bolognese", "ravioli", "gnocchi", "mac and cheese",
                "maccheroni", "makkaroni", "farfalle", "fusilli"],
    "rice":    ["rice", "reis", "reispfanne", "fried rice", "gebratener reis",
                "risotto", "paella", "wok", "stir fry", "stir-fry",
                "bibimbap", "sushi", "jollof"],
    "curry":   ["curry", "masala", "tikka", "dal", "daal", "korma",
                "vindaloo", "thai curry", "green curry", "red curry",
                "butter chicken"],
    "soup":    ["soup", "suppe", "eintopf", "stew", "broth", "bruehe",
                "ramen", "pho", "minestrone", "chili", "chilli", "goulash",
                "gulasch", "linsensuppe", "tomatensuppe"],
    "salad":   ["salad", "salat", "bowl", "buddha bowl", "caesar",
                "coleslaw", "greek salad", "griechischer salat", "rohkost"],
    "pancakes":["pancake", "pancakes", "pfannkuchen", "crepe", "crepes",
                "waffle", "waffel", "waffeln", "breakfast", "fruehstueck",
                "eierkuchen", "porridge", "oatmeal", "haferbrei"],
    "dessert": ["dessert", "cake", "kuchen", "muffin", "cupcake", "cookie",
                "keks", "brownie", "eis", "ice cream", "pudding", "tiramisu",
                "sweet", "suess", "nachtisch", "torte", "donut", "doughnut"],
}
DEFAULT_ICON = "other"
ICON_DIR = "images"

def icon_for_dish(dish):
    icon_obj = getattr(dish, "icon", None)
    if icon_obj is not None:
        manual = (getattr(icon_obj, "name", "") or "").strip().lower()
        if manual in ICON_KEYWORDS or manual == DEFAULT_ICON:
            return f"{ICON_DIR}/{manual}.png"

    # Alle Textfelder + Tags zu einem durchsuchbaren String zusammenfassen
    parts = [
        getattr(dish, "name", "") or "",
        getattr(dish, "description", "") or "",
        getattr(dish, "ingredients", "") or "",
    ]
    tags = getattr(dish, "tags", None)
    if tags:
        parts.extend(getattr(t, "name", "") or "" for t in tags)
    haystack = " ".join(parts).lower()

    for key, keywords in ICON_KEYWORDS.items():
        if any(kw in haystack for kw in keywords):
            return f"{ICON_DIR}/{key}.png"

    return f"{ICON_DIR}/{DEFAULT_ICON}.png"


# Funktion in allen Templates verfuegbar machen
app.jinja_env.globals["icon_for_dish"] = icon_for_dish

login_manager = LoginManager() 
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Please log in to access this page."

@login_manager.user_loader #callback to reload the user object from the user ID stored in the session; Source: Flask-Login
def load_user(id):
    return db.session.get(User, id) #FSWD: SQL Alchemy 

with app.app_context():
    db.create_all()

# landing page
@app.route('/')
def index():
    return render_template('landingpage.html')


# feed von den meals
@app.route('/feed')
def feed():
    dishes = db.session.execute(
        db.select(Dish).filter(Dish.left_portions != 0).order_by(Dish.id)).scalars().all() #ergänzt dass ausgebuchtes essen nicht angezeigt wird
    return render_template('feed.html', dishes=dishes)

# Details zum aufgewählten Gericht
@app.route('/dishes/<int:dish_id>')
def get_dish(dish_id):
    dish = db.session.get(Dish, dish_id)
    #return jsonify({"id": dish.id, "name": dish.name, "description": dish.description, "price": dish.price, "left_portions": dish.left_portions, "status": dish.status})
    return render_template('meal_detail.html', dish=dish)

# Übersicht der Menge und der Bestellung
@app.route('/order_view/<int:dish_id>')
@login_required
def order_view(dish_id):
    dish = db.session.get(Dish, dish_id)

    if current_user.id == dish.cook_id:
        flash("You can not order your own dish")
        return redirect(url_for('feed'))

    return render_template('order_view.html', dish = dish)

# Payment Success Cash
@app.route('/payment_success_cash/<int:dish_id>', methods=['POST'])
def payment_success_cash(dish_id):
    return complete_order(dish_id, "Cash")

# Payment Success PayPal
@app.route('/payment_success_paypal/<int:dish_id>', methods=['POST'])
def payment_success_paypal(dish_id):
    return complete_order(dish_id, "PayPal")

def complete_order(dish_id, payment_method):
    dish = db.session.get(Dish, dish_id)

    portions = request.form.get("portions", 1, type = int)

    if portions < 1:
        return render_template( 'order_view.html', dish = dish, error = "Please select at least one portion.")

    if portions > dish.left_portions:
        return render_template( 'order_view.html', dish = dish, error = "Not enough portions available.")
    
    # Save order in database so it appears under "My Orders"
    new_order = DishOrder(
        dish_id = dish.id,
        buyer_id = current_user.id,
        portions = portions,
        status = "confirmed"
    )

    db.session.add(new_order)

    dish.left_portions = dish.left_portions - portions
    db.session.commit()

    return render_template( 'payment_success.html', cook_name=f"{dish.cook.first_name} {dish.cook.last_name}", cook_telephone=dish.cook.phone_number, dish = dish, portions = portions, payment_method = payment_method, 
                           pickup_date=dish.pickup_time.strftime("%Y-%m-%d"), pickup_time=dish.pickup_time.strftime("%H:%M"), pickup_timeend=dish.pickup_timeend.strftime("%H:%M"), pickup_location=dish.cook.dorm.name)


# post meals
@app.route('/post', methods=['GET', 'POST'])
@login_required
def post_meal():

    # CATCH: Only cooks can post meals
    if not current_user.is_cook:
        flash('Only registered cooks can offer dishes!', 'danger')
        return redirect(url_for('dashboard'))
    
    form = MealForm() #form object erstellen, html template frontend tool
   
    if form.validate_on_submit():
        # combine day + start time to a single datetime object
        start_datetime = datetime.combine(form.pickup_day.data, form.time_start.data)
        # combine day + end time to a single datetime object
        end_datetime = datetime.combine(form.pickup_day.data, form.time_end.data)
        # build Dish/ Meal using form data and database table format
        new_dish = Dish( #database model Dish, siehe models/dish.py
            cook_id = current_user.id,
            name = form.name.data,
            description = form.description.data,
            price = form.price.data,
            total_portions = form.portions.data,
            left_portions = form.portions.data,
            pickup_time = start_datetime,  
            pickup_timeend = end_datetime,
            status = form.status.data,
            ingredients = form.ingredients.data
        )
       
        db.session.add(new_dish)
        db.session.commit()
       
        flash('Dish was successfully added!', 'success') #success turns box green yay
        return redirect(url_for('dashboard'))
       
    return render_template('post_meal.html', form=form)


# Profil anzeigen
@app.route('/profile/<username>')
def profile(username):
    profile_user = db.session.execute(
            select(User).filter_by(username=username)  
        ).scalar_one_or_none() #return one user object or none Source: SQL Alchemy
    
    if not profile_user: #if none
        flash("Username doesn't exist")
        return render_template('404.html'), 404
    
    return render_template('profile.html', profile_user=profile_user)

# Edit Profile

@app.route('/profile/<username>/edit', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    if current_user.username != username: #checks that you can only edit your own profile
        flash("You can only edit your own profile")
        return redirect(url_for('index'))
    
    form = forms.EditProfileForm()

    if request.method == 'GET':
        form.new_bio.data = current_user.bio
        form.new_phonenumber.data = current_user.phone_number
        form.new_dorm_id.data = current_user.dorm_id
        form.new_cook.data = current_user.is_cook

    if form.validate_on_submit():

        #wird nur aktualisiert, wenn etwas eingegeben wurde; AI Prompt 1 Julia
        if form.new_bio.data: 
            current_user.bio = form.new_bio.data

        if form.new_phonenumber.data: #prüft ob Telefonnummer bereits genutzt wird
            existing_user = db.session.execute(
                select(User).filter_by(phone_number=form.new_phonenumber.data)  
            ).scalar_one_or_none()
            if existing_user != current_user: 
                flash('Phone Number is already in use')
                return render_template('edit_profile.html', title='Edit_Profile', form=form)
            else:
                current_user.phone_number = form.new_phonenumber.data

        if form.new_dorm_id.data != 0: #SelectField wählt immer automatisch das erste Feld aus, auch wenn keine Entscheidung getroffen wurde, deswegen dem ersten Field Wert Null gegeben; AI Prompt 2 Julia
            current_user.dorm_id = form.new_dorm_id.data

        current_user.is_cook = form.new_cook.data

        db.session.commit()
        flash('Profile updated!')
        return redirect(url_for('profile', username=current_user.username))

    return render_template('edit_profile.html', title='Edit_Profile', form=form)

#Logout
@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()   #Flask Login
    flash('You are logged out')
    return redirect(url_for('index'))



# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('feed'))

    form = forms.LoginForm()

    if form.validate_on_submit(): #prüft ob POST-Request und ob alle Daten gültig sind, Source: Flask-WTF
        user = db.session.execute(
            select(User).filter_by(email=form.email.data)  
        ).scalar_one_or_none()  #Source: SQL Alchemy 
        if not user: #wenn user none ist
            flash('This E-Mail is not registered yet')
        elif not user.check_password(form.password.data):
            flash('The password is wrong')
        else: 
            login_user(user)
            flash('You were successfully logged in')
            return redirect(url_for('feed'))

    return render_template('login.html', title='Login', form=form)


# Register
@app.route('/register' , methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated: #Source: Login-Manager
        return redirect(url_for('feed'))

    form = forms.RegisterForm()

    if form.validate_on_submit(): 
        user = db.session.execute(
            select(User).filter_by(email=form.email.data)
        ).scalar_one_or_none()
        if user:
            flash('E-Mail is already registered!')
            return render_template('register.html', title='Registrieren', form=form)
        
        user = db.session.execute(
            select(User).filter_by(username=form.username.data)
        ).scalar_one_or_none()
        if user:
            flash('Username already exists!')
            return render_template('register.html', title='Registrieren', form=form)
        
        user = db.session.execute(
           select(User).filter_by(phone_number=form.phonenumber.data)
        ).scalar_one_or_none()
        if user:
            print('Phone Number is already registered!')
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
        flash('Successfully signed up!')
        return redirect(url_for('feed'))

    return render_template('register.html', title='Registrieren', form=form)

#JSON API 
@app.route('/api/dorms')
def api_dorms():
    dorms = db.session.execute(db.select(Dorm)).scalars().all()
    return jsonify([{"id": d.id,"name": d.name, "address": d.address,"district": d.district, "postcode": d.postcode,"place": d.place} for d in dorms])


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
    dorm_list = [{"id": d.id, "name": d.name, "address": d.address} for d in dorms]

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
            "status": o.status,
            "pickup_date": o.dish.pickup_time.strftime("%d.%m.%Y") if o.dish.pickup_time else None,
            "pickup_time": o.dish.pickup_time.strftime("%H:%M") if o.dish.pickup_time else None,
            "pickup_timeend": o.dish.pickup_timeend.strftime("%H:%M") if o.dish.pickup_timeend else None,
            "pickup_location": o.dish.cook.dorm.name if o.dish.cook and o.dish.cook.dorm else None,
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
        "left_portions": d.left_portions,
        "status": d.status
    } for d in my_dishes]

    # show meals in selected dorm
    offers = db.session.execute(
        select(Dish)
        .join(User, Dish.cook_id == User.id)
        .filter(User.dorm_id == selected_dorm_id)
        .filter(Dish.left_portions != 0) #not showing dishes that are booked out
        .filter(Dish.status.in_(['scheduled', 'active'])) #so it wont show meals that are already completed
    ).scalars().all()

    # build list of meals
    current_offers = [{
        "id": o.id,
        "name": o.name,
        "cook": o.cook.first_name,
        "cook_username": o.cook.username,
        "description": o.description,
        "price": float(o.price),
        "left_portions": o.left_portions,
        "status": o.status
    } for o in offers]

    # render dashboard template with all the data
    return render_template(
        'dashboard.html',
        selected_dorm_id=selected_dorm_id,
        dorm_list=dorm_list,
        my_orders=my_orders,
        current_offers=current_offers,
        my_dishes=my_dishes #call all dishes objects 
    )

# edit meal
@app.route('/dishes/<int:dish_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_meal(dish_id):
    dish = db.session.get(Dish, dish_id)
    
    # does the dish exist?
    if not dish:
        flash("Dish not found.", "danger")
        return redirect(url_for('dashboard'))
        
    # only the cook who created the dish can edit it
    if dish.cook_id != current_user.id:
        flash("You are not authorized to edit this dish.", "danger")
        return redirect(url_for('dashboard'))

    form = MealForm()

    # pre-fill the form with existing dish data when the page is loaded
    if request.method == 'GET':
        form.name.data = dish.name
        form.description.data = dish.description
        form.price.data = dish.price
        form.portions.data = dish.total_portions
        form.status.data = dish.status
        form.ingredients.data = dish.ingredients
        if dish.pickup_time:
            form.pickup_day.data = dish.pickup_time.date()
            form.time_start.data = dish.pickup_time.time()
        if dish.pickup_timeend:
            form.time_end.data = dish.pickup_timeend.time()

    if form.validate_on_submit():
        # combine day + start time to a single datetime object
        start_datetime = datetime.combine(form.pickup_day.data, form.time_start.data)
        end_datetime = datetime.combine(form.pickup_day.data, form.time_end.data)
        
        # update the dish with the new data from the form
        dish.name = form.name.data
        dish.description = form.description.data
        dish.price = form.price.data
        # very important: update left_portions to match total_portions if the total_portions has changed
        if dish.total_portions != form.portions.data:
            dish.left_portions = form.portions.data
        dish.total_portions = form.portions.data
        dish.pickup_time = start_datetime
        dish.pickup_timeend = end_datetime
        dish.status = form.status.data
        dish.ingredients = form.ingredients.data

        db.session.commit()
        flash('Dish updated successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('post_meal.html', form=form, title="Edit Dish")

# delete meal
@app.route('/dishes/<int:dish_id>/delete', methods=['POST'])
@login_required
def delete_meal(dish_id):
    dish = db.session.get(Dish, dish_id)
    
    # does the dish exist?
    if not dish:
        flash("Dish not found.", "danger")
        return redirect(url_for('dashboard'))
        
    # only the cook who created the dish can delete it
    if dish.cook_id != current_user.id:
        flash("You are not authorized to delete this dish.", "danger")
        return redirect(url_for('dashboard'))

    # check if the dish has already been ordered
    already_ordered = db.session.execute(
        select(DishOrder).filter_by(dish_id=dish_id)
    ).scalars().first()

    if already_ordered:
        # if there are any orders for this dish, prevent deletion and show a message
        flash("This dish cannot be deleted because it has already been ordered by students!", "danger")
        return redirect(url_for('dashboard'))

    # if no orders exist, proceed with deletion
    db.session.delete(dish)
    db.session.commit()
    
    flash('Dish deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

# run app
if __name__ == '__main__':
    app.run(debug=True)
