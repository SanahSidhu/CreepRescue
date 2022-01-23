import sqlite3 as s

def user(path: str):

    conn = s.connect(path)
    cur = conn.cursor()

    tbl = "CREATE TABLE IF NOT EXISTS user(User_Name TEXT,Email TEXT UNIQUE, Mob_No TEXT UNIQUE, Password TEXT)"

    cur.execute(tbl)
    conn.commit()


def add_user(path: str, data: tuple):
    conn = s.connect(path)
    cur = conn.cursor()

    add_user = f"insert into user values{data}" 

    cur.execute(add_user)
    conn.commit()


def chk_user_exist(path:str, user_email: str):
    conn = s.connect(path)
    cur = conn.cursor()

    user_chk = f"select * from user where Email='{user_email}'"

    cur.execute(user_chk)
    user_chk_res = cur.fetchone()

    if user_chk_res is None:
        return False
    else:
        return True


def chk_user_pwd(path:str, user_email: str, pwd: str):
    conn = s.connect(path)
    cur = conn.cursor()

    chk_pwd = f"select Password from user where Email='{user_email}'"

    cur.execute(chk_pwd)
    chk_pwd_res = cur.fetchall()

    if chk_pwd_res[0][0] == pwd:
        return True
    else:
        return False


def get_email(path: str):
    conn = s.connect(path)
    cur = conn.cursor()

    get_mail = "select Email from user"

    cur.execute(get_mail)
    emails = cur.fetchall()

    return emails


def get_mob_no(path:str, user_email:str):
    conn = s.connect(path)
    cur = conn.cursor()

    mob_no_query = f"select Mob_No from user where Email='{user_email[0]}'"

    cur.execute(mob_no_query)
    mob_no_res = cur.fetchone()

    return mob_no_res[0]