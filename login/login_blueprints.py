from flask import Blueprint, render_template

login_ = Blueprint("login", __name__)

@login_.route('/success')
def success():
    return render_template('/success.html')

@login_.route('/failed')
def failed():
    return render_template('/login_failed.html')
