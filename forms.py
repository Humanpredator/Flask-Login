from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email,Regexp


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=6, max=12, message='Username length must be between %(min)d - %(max)dcharacters'),Regexp(('^[\w](?!.*?\.{2})[\w.]{5,12}[\w]$'), message="Enter username Like Instagram") ])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    # confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired()])

class ResetEmailForm(FlaskForm):
    email = StringField('Provide your registered Email Address', validators=[DataRequired(), Email(), Length(min=6, max=40)])


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
