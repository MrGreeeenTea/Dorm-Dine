from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, BooleanField, SelectField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo

#https://flask-wtf.readthedocs.io/en/1.2.x/

class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    login = SubmitField('Login')


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=3)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=3)])
    username = StringField('Username', validators=[InputRequired(), Length(min=3)])
    email = StringField('E-Mail-address', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8)])
    passwordagain = PasswordField('Repeat Password', validators=[InputRequired(), Length(min=8), EqualTo('password')]) 
    phonenumber = StringField('Phone Number', validators=[InputRequired(), Length(min=5)])
    is_cook = BooleanField('I am interested in Cooking for Dorm&Dine')
    dorm_id = SelectField('Choose your dormitory', choices=[(1, 'Wohnheim Nollendorfstraße')], coerce=int, validators=[InputRequired()])
    bio = StringField('Write a short Bio about yourself')
    register = SubmitField('Registrate')