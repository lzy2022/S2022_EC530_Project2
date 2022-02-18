# EC530 Project 2 By Zhiyuan Liu
# This file contains the function that can varify the user with password
from re import U
from db_info import db_addr
import sqlite3
from project2_exceptions import PassWordNotMatch, UserIdNotExist


def varify_user(u_id, pw):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT * FROM user_pw WHERE user_id = ?", (u_id,))
    user = cur.fetchone()
    # check if the id not exist
    if user == None:
        raise UserIdNotExist
    if user['pw'] != pw:
        raise PassWordNotMatch
    return True
    