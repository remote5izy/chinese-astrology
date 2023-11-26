# website/home.py
from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template("z.html")

@home.route('/group')
def index2():
    return render_template("z2.html")

@home.route('/about')
def about():
    return 'About'
