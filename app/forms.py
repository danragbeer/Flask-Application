from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class UserForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])

class AccountForm(FlaskForm):
    '''The form needed for caputuring the first name, last name, nickname,
       and email'''
    first_name = StringField('First Name', validators = [InputRequired()])
    last_name = StringField('Last Name', validators = [InputRequired()])
    nickname = StringField('Nickname', validators = [InputRequired()])
    email = StringField('Email', validators = [InputRequired()])
