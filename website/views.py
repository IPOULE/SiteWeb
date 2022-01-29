from flask import Blueprint, render_template
from flask_login import login_required, current_user

from . import db
from .models import User, Livre

views = Blueprint('views', __name__)

@views.route('/')
def home():
    livre = Livre.query.all()
    '''user = User.query.all()'''
    return render_template('home.html', livre = livre)

# @views.route('home/admin')
# def admin():
#     livre = Livre.query.all()
#     return render_template('admin.html', livre = livre)
#







'''@login_required
    test=User('test')
    db.session.add(test)
    db.session.commit()
'''