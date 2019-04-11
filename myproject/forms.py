from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from myproject.models import User

class LoginField(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationFor(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), EqualTo('email_confirm', message='Emails must match')])
    email_confirm = StringField('Confirm Emial', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match.')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has already been registered. Please use another email.')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).frist():
            raise ValidationError('Your username has already been registered. Please use another username.')