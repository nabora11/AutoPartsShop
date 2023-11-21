from user import *
from db import *

def register(user:BaseUser,db: UserDatabase)->bool:
    found_user=db.search_by_mail(user.email)

    if not found_user:
        db.add(user)
        return True
    else:
        print('User already exist')
        return False

def login(username:str, password:str,db:UserDatabase)->bool :
    found_user=db.search_by_mail(username)
    found_password=False
    if found_user:
        if found_user.password==password:
            found_password=True
            db.set_current_user(found_user)
            return True
    return False

def logout(db:UserDatabase):
    db.set_current_user(None)
