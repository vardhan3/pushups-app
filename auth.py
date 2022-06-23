from flask import Blueprint, render_template, url_for

auth = Blueprint('auth', __name__)

@auth.route ('/signup')
def signup():
    return "This page is used for sign up"

@auth.route('/login')
def login():
    return "This page is used for log in"

@auth.route('/logout')
def logout():
    return "Use this to log out"