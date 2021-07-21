from bizeducateapp import db
from flask_login import UserMixin
from flask import session, abort
from flask_admin.contrib.sqla import ModelView
from bizeducateapp import login
from flask_admin import AdminIndexView

@login.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model,UserMixin):
    __tabelname__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(60))
    password = db.Column(db.String(60))


    def __init__(self,name):
        self.name = name

    def __repr__(self):
        f"User name:{self.name}"


class Courses (db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String,nullable = False)
    country = db.Column(db.String,nullable = False)
    date = db.Column(db.DateTime,nullable = False)

    def __init__(self,title,country,date):
        self.title = title
        self.country = country
        self.date = date

    def __repr__(self):
        return f"Course name:{self.title}, will take place in {self.country} on {self.date}"

class SingleCourse (db.Model):
    __tablename__ = 'singlecourse'
    id = db.Column(db.Integer,primary_key = True)
    paragraph = db.Column(db.String,db.ForeignKey('courses.title'), nullable = False)
    venue = db.Column(db.String,db.ForeignKey('courses.country'), nullable= False)
    dates = db.Column(db.DateTime,db.ForeignKey('courses.date'),nullable = False)
    description = db.Column(db.Text)
    trainer = db.Column(db.Text)
    key_questions = db.Column(db.Text)

    def __init__(self,paragraph,dates):
        self.paragraph = paragraph
        self.dates = dates


class MyAdminIndexView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)



