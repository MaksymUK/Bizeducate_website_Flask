import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager


app = Flask (__name__)
app.config['SECRET_KEY'] = 'mysecret'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login = LoginManager(app)
Migrate(app,db)
from bizeducateapp.models import Courses,Users,MyAdminIndexView,SingleCourse

admin = Admin(app)
admin.add_view(MyAdminIndexView(Users,db.session))
admin.add_view(MyAdminIndexView(Courses,db.session))
admin.add_view(MyAdminIndexView(SingleCourse,db.session))






