from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email

### Admin page login ###
class LoginForm(FlaskForm):
    username = StringField ('Username',validators=[DataRequired()])
    password = PasswordField ('Password',validators=[DataRequired()])
    submit = SubmitField ('Log in')

### Contact us form ###
class ContactUsForm(FlaskForm):
     name = StringField('Name', validators=[DataRequired()])
     surname = StringField('Surname')
     company = StringField('Company')
     telephone = StringField('Phone_number')
     email = StringField('Email', validators=[DataRequired(),Email()])
     text = TextAreaField('Text', validators =[DataRequired()])
     submit = SubmitField ('Send Now')

### Feed back form ###
class Feed_back(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname')
    company = StringField('Company')


