
from user import User

users: list = [
    User(1,"bob","abc123"),
    User(2,"alice","345"),
]

#{userName: userObject}
username_mapping: dict = {user.username : user for user in users}

#{userId: userObject}
userid_mapping: dict = {user.id: user for user in users}


def authenticate(username: str, password: str) -> User:
    '''This Function is used to check the User is already register or 
        not by getting username and password and 
        return User object if user exist otherwise None'''

    user =  username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload: dict) -> User:
    '''This Function is handle by JWT to generate token and  
        return User object if user id exist otherwise None'''
    
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)