from flask import Blueprint, render_template, request, make_response, jsonify
from login.login_route import pass_data

login_ = Blueprint("login", __name__)

@login_.route('/', methods=["POST","GET"])
def check_login():
    data = request.get_json()
    if pass_data(data) == True:
        return make_response(jsonify({"isValid":True}))
    else:
        return make_response(jsonify({"isValid":False}))


# @login_.route("/success", methods=["POST", "GET"])
# def success():
#     return render_template("/success.html")
#
#
# @login_.route("/failed", methods=["POST", "GET"])
# def failed():
#     return render_template("/login_failed.html")
