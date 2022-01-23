
from server.mainapp.models import add_user, chk_user_exist, chk_user_pwd

def signup(path: str, data: tuple):
    add_user(path, data)

def login(path: str, mob: str, passw: str):
    
    if chk_user_exist(path, mob):
        if chk_user_pwd(path,mob,passw):
            return True
        else:
            return False
    else:
        return False
    
