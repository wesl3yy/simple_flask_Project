from flask import Blueprint, render_template, request

login_ = Blueprint("login", __name__)

@login_.route('/success',methods=["POST","GET"])
def success():
    return render_template('/success.html')

@login_.route('/failed',methods=["POST","GET"])
def failed():
    return render_template('/login_failed.html')
