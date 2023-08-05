from flask import render_template, request, Blueprint, redirect

site = Blueprint('site', __name__)

@site.route('/')
def mainPage():
    return render_template('index.html')