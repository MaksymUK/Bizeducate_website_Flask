from bizeducateapp import app
from flask import render_template,flash,redirect,url_for,session,request
from bizeducateapp.models import Users
from flask_login import login_user,current_user,logout_user,login_required
from bizeducateapp.forms import LoginForm

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method =='POST':
        if request.form.get('username')=='Maksym' and request.form.get('password')=='123456':
            session['logged_in'] = True
            return redirect('/admin')
        else:
            return render_template('login.html',failed = True)
    return render_template('login.html',form = form)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/course')
def single_course():
    return render_template('course.html')




if __name__=='__main__':
    app.run(debug=True)
