from flask import request, redirect, render_template
from DAO.data import get_username, get_password

def login(username, password):
    if username == get_username(username) and password == get_password(password):
        return True
