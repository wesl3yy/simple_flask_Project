from DAO.login_method import login

def pass_data(data):
    username = data["username"]
    password = data["password"]
    return login(username, password)
