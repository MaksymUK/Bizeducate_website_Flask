import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_mail import Mail


app = Flask (__name__)
app.config['SECRET_KEY'] = 'mysecret'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_DEBUG'] = app.debug
app.config['MAIL_USERNAME'] = 'marketalliance18@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get("GMAIL_PASS")
#app.config['MAIL_DEFAULT_SENDER'] = None
#app.config['MAIL_MAX_EMAILS'] = None
#app.config['MAIL_SUPPRESS_SEND'] = False
#app.config['MAIL_ASCII_ATTACHMENTS'] = False

###connecting mail###
mail = Mail(app)

db = SQLAlchemy(app)
login = LoginManager(app)
Migrate(app,db)
from bizeducateapp.models import Courses,Users,MyAdminIndexView,SingleCourse

admin = Admin(app)
admin.add_view(MyAdminIndexView(Users,db.session))
admin.add_view(MyAdminIndexView(Courses,db.session))
admin.add_view(MyAdminIndexView(SingleCourse,db.session))






