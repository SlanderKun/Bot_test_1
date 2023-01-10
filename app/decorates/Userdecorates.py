from app.models import User
from app import app
from flask import request, render_template


@app.route('/')
def type():
    hello = 'Hello'
    return hello


@app.route('/users/<int:id>')
def types(id):
    hello = 'Hello'
    return hello + str(id)


@app.route('/users/create')
def create():
    return render_template('menu.html')

