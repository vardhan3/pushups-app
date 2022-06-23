from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index ():
    return 'Hello World!'

@main.route('/profile')
def profile():
    return "Profile here!"