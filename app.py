from myproject import app, db 
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user,login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm


@app.route('/index')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are now securely logged out. Thank you for visiting!")
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in Successfully!')
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('welcome_user')
            return redirect(next)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name,
                    last_name=form.last_name,
                    email=form.email.data, 
                    username=form.username.data, 
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registering!")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

