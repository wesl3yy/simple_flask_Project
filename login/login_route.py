from login.login_blueprints import login_
from flask import render_template, request
from DAO.data import get_username, get_password


@login_.route("/login", methods=("POST", "GET"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = get_username(username)
        pas = get_password(password)
        if username != user or password != pas:
            return render_template("/login_failed.html")
        if username == user and password == pas:
            return f"Hello, {user}"
    return render_template("/login.html")
