import sqlite3 as s

def user(path: str):

    conn = s.connect(path)
    cur = conn.cursor()

    tbl = "CREATE TABLE IF NOT EXISTS user(User_Name TEXT, Mob_No TEXT UNIQUE, Password TEXT)"

    cur.execute(tbl)
    conn.commit()


def add_user(path: str, data: tuple):
    conn = s.connect(path)
    cur = conn.cursor()

    add_user = f"insert into member values{data}" 

    cur.execute(add_user)
    conn.commit()


def chk_user_exist(path:str, mob_no: str):
    conn = s.connect(path)
    cur = conn.cursor()

    user_chk = f"select * from user where Mob_No='{mob_no}'"

    cur.execute(user_chk)
    user_chk_res = cur.fetchone()

    if user_chk_res is None:
        return False
    else:
        return True


def chk_user_pwd(path:str, mob_no: str, pwd: str):
    conn = s.connect(path)
    cur = conn.cursor()

    chk_pwd = f"select Password from user where Mob_No='{mob_no}'"

    cur.execute(chk_pwd)
    chk_pwd_res = cur.fetchall()

    if chk_pwd_res[0][0] == pwd:
        return True
    else:
        return False
