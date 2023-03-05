from app.models import User
from app import app
from flask import request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def type():
    hello = 'Hello'
    return hello


@app.route('/users/<int:id>')
def types(id):
    hello = 'Hello'
    return hello + str(id)


@app.route('/users/get')
def return_users():
    gf = User.query.all()
    return gf


@app.route("/users/create", methods=["POST", "GET"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form['name'],
            email=request.form['email'],
            password=request.form['psw']
        )

        User.session.add(user)
        User.session.commit()

    return render_template('menu.html')


# @app.route("/register", methods=("POST", "GET"))
# def register():
#     if request.method == "POST":
#         # здесь должна быть проверка корректности введенных данных
#         try:
#             hash = generate_password_hash(request.form['psw'])
#             u = Users(email=request.form['email'], psw=hash)
#             User.session.add(u)
#             User.session.flush()
#         except:
#
#             User.session.rollback()
#             print("Ошибка добавления в БД")
#
#         return redirect(url_for('index'))
#
#     return render_template("register.html", title="Регистрация")
