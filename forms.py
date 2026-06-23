from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, EmailField, BooleanField, SelectField, PasswordField, IntegerField, TimeField, DateField
from wtforms.validators import InputRequired, Length, EqualTo, NumberRange

#https://flask-wtf.readthedocs.io/en/1.2.x/

class LoginForm(FlaskForm):
    email = EmailField('E-Mail', validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    login = SubmitField('Login')


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=1)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=1)])
    username = StringField('Username', validators=[InputRequired(), Length(min=3)])
    email = EmailField('E-Mail-address', validators=[InputRequired()])
    password = PasswordField('Password (at least 8 characters)', validators=[InputRequired(), Length(min=8)])
    passwordagain = PasswordField('Repeat Password', validators=[InputRequired(), Length(min=8), EqualTo('password')]) 
    phonenumber = StringField('Phone Number', validators=[InputRequired(), Length(min=5)])
    is_cook = BooleanField('I am interested in Cooking for Dorm&Dine')
    dorm_id = SelectField('Choose your dormitory', choices=[(1, 'Wohnheim Nollendorfstraße'),(2, 'Halbauer Weg 19-21'),(3, 'Franz-Mehring-Platz 2, 3')], coerce=int, validators=[InputRequired()])
    bio = StringField('Write a short Bio about yourself')
    register = SubmitField('Registrate')

class MealForm(FlaskForm):
    name = StringField('Name of the Dish', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])
    price = StringField('Price (€)', validators=[InputRequired()])
    portions = IntegerField('Available Portions', validators=[InputRequired(), NumberRange(min=1)])
    status = SelectField('Status', choices=[('scheduled', 'New'), ('active', 'Ready for Pickup')])
    ingredients = StringField('Ingredients', validators=[InputRequired()])
    pickup_day = DateField('Pickup Day', validators=[InputRequired()])
    time_start = TimeField('Available From', validators=[InputRequired()])
    time_end = TimeField('Available Until', validators=[InputRequired()])
    submit = SubmitField('Offer Dish')

class EditProfileForm(FlaskForm):
    
    new_bio = StringField('Update the short bio about yourself')
    new_phonenumber = StringField('Phone Number')
    new_dorm_id = SelectField('Choose your new dormitory', choices=[(0, 'No dorm change'),(1, 'Wohnheim Nollendorfstraße'),(2, 'Halbauer Weg 19-21'),(3, 'Franz-Mehring-Platz 2, 3')], coerce=int)
    update = SubmitField('Update Profile')

   