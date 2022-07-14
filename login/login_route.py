from login.login_blueprints import login_
from flask import request, redirect, render_template
from DAO.data import get_username, get_password


@login_.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = get_username(username)
        pas = get_password(password)
        if username != user or password != pas:
            return redirect('/failed')
        else:
            return redirect('/success')
    return render_template('/login.html')
