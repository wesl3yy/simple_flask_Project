from flask import Blueprint, render_template, request, make_response, jsonify
from login.login_route import pass_data

login_ = Blueprint("login", __name__)


@login_.route("/", methods=["POST", "GET"])
def check_login():
    data = request.get_json()
    if pass_data(data):
        return make_response(jsonify({"isValid": True}))
    else:
        return make_response(jsonify({"isValid": False}))

