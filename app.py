from bizeducateapp import app,mail
from flask import render_template,flash,redirect,url_for,session,request
from bizeducateapp.models import Users
from flask_login import login_user,current_user,logout_user,login_required
from bizeducateapp.forms import LoginForm,ContactUsForm
from flask_mail import Message, Mail

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

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

@app.route('/finances')
def finance():
    return render_template('finance.html')

@app.route('/contact_us', methods = ['GET','POST'])
def contact_us():
    form = ContactUsForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        text = request.form.get('text')
        flash("Your request has been sent")
        msg = Message('Request from bizeducate website', sender='marketalliance18@gmail.com', recipients=['office@bizeducate.com'])
        msg.body = f"Email: {email},\n Name: {name},\n Request text:\n {text}"
        mail.send(msg)
        return redirect(url_for('contact_us'))
    return render_template('contact_us.html', form = form)



if __name__=='__main__':
    app.run(debug=True)
