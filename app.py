from flask import Flask
from login.login_route import login_

app = Flask(__name__)
app.register_blueprint(login_)

if __name__ == "__main__":
    app.run()
