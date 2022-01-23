from werkzeug.security import safe_str_cmp
from user import User


def authenticate(username, password):
    print("trying to autheticate username")
    user = User.find_by_username(username) 
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload): # payload is content of JWT tokens
    user_id = payload.get('identity')
    return User.find_by_id(user_id)


