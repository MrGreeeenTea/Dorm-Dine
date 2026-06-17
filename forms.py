from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, BooleanField, SelectField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length, EqualTo

#https://flask-wtf.readthedocs.io/en/1.2.x/
#User Interface fswd

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
    dorm_id = SelectField('Choose your dormitory', choices=[(1, 'Wohnheim Nollendorfstraße')], coerce=int, validators=[InputRequired()])
    bio = StringField('Write a short Bio about yourself')
    register = SubmitField('Registrate')


class EditProfileForm(FlaskForm):
    
    new_bio = StringField('Update the short bio about yourself')
    update = SubmitField('Update Profile')

    #will be used for later
    #new_first_name = StringField('First Name')
    #new_last_name = StringField('Last Name')
    #username = StringField('Username')
    #new_email = EmailField('E-Mail-address')
    #new_password = PasswordField('Password (at least 8 characters)')
    #new_passwordagain = PasswordField('Repeat Password', validators=[EqualTo('password')]) 
    #new_phonenumber = StringField('Phone Number')
    #change_is_cook = BooleanField('I am interested in Cooking for Dorm&Dine')
    #dorm_id = SelectField('Choose your dormitory', choices=[(1, 'Wohnheim Nollendorfstraße')], coerce=int)


