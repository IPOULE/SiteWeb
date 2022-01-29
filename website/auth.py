from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from .models import User, Livre, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from datetime import date

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET','POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user :
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greather than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")

@auth.route('/admin', methods=['GET','POST'])
def admin():
    livre = Livre.query.all()
    user = User.query.all()
    return render_template('admin.html', livre=livre, uesr=user)

#This route is for adding an Product
@auth.route('/add',methods=['GET','POST'])
def add():
    if request.method == "POST":
        title = request.form['title']
        date_added = date.today()
        price = request.form['price']
        link_image = request.form['link_image']

        livre = Livre(title, date_added, price, link_image)
        db.session.add(livre)
        db.session.commit()

        flash('Product Added Successfully', category='success')

        return redirect(url_for('auth.admin'))
    return render_template('admin.html')

#This route is for updating an Product
@auth.route('/update',methods=['GET','POST'])
def update():
    if request.method == 'POST':
        data = Livre.query.get(request.form.get('id'))

        data.title = request.form['title']
        data.price = request.form['price']
        date_update = date.today()
        data.link_image = request.form['link_image']
        db.session.commit()

        flash('Product Updated Successfully', category='success')

        return redirect(url_for('auth.admin'))
    #return render_template('admin.html')

#This route is for deleting an Product
@auth.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    data = Livre.query.get(id)
    db.session.delete(data)
    db.session.commit()

    flash("Product Deleted Successfully!", category='success')

    return redirect(url_for('auth.admin'))

#Get Single Product
@auth.route('/data/<int:id>')
def RetrieveSingleEmployee(id):
    livre = Livre.query.filter_by(employee_id=id).first()
    if livre:
        return render_template('single_product.html', livre = livre)
    return f"Employee with id ={id} Doenst exist"