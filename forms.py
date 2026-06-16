from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, EqualTo

#https://flask-wtf.readthedocs.io/en/1.2.x/

class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired()])
    password = StringField(validators=[InputRequired()])
    login = SubmitField('Login')


class RegisterForm(FlaskForm):
    id = HiddenField()
    first_name = StringField('Vorname', validators=[InputRequired(), Length(min=3)])
    last_name = StringField('Nachname', validators=[InputRequired(), Length(min=3)])
    email = StringField('E-Mail-Adresse', validators=[InputRequired()])
    password = StringField('Passwort', validators=[InputRequired(), Length(min=8)])
    passwordagain = StringField('Wiederhole Passwort', validators=[InputRequired(), Length(min=8), EqualTo('password')]) 
    phonenumber = StringField('Telefonnummer', validators=[InputRequired(), Length(min=5)])
    is_cook = BooleanField('Ich habe Interesse für Dorm&Dine zu kochen')
    dorm_id = SelectField('Wähle dein Wohnheim aus', choices=[('1', 'Haus1'), ('2', 'Haus2'), ('3', 'Haus3')], validators=[InputRequired()])
    bio = StringField('Schreibe etwas über dich')
    created_at = HiddenField()
    register = SubmitField('Registrieren')

