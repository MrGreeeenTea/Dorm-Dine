from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired()])
    password = StringField(validators=[InputRequired()])
    login = SubmitField('Login')

class RegisterForm(FlaskForm):
    id = HiddenField()
    name = StringField('Name', validators=[InputRequired(), Length(min=5)])
    email = StringField(validators=[InputRequired()])
    password = StringField('Passwort', validators=[InputRequired(), Length(min=8)])
    passwordagain = StringField('Wiederhole Passwort', validators=[InputRequired(), Length(min=8), EqualTo('password')]) 
    phonenumber = StringField('Telefonnummer', validators=[InputRequired(), Length(min=5)])
    register = SubmitField('Registrieren')