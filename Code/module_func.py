# EC530 Project 2 By Zhiyuan Liu
# This file contains the module functions
from asyncio.windows_events import NULL
import sqlite3
from project2_exceptions import PassWordNotMatch, UserIdNotExist

def new_user(db_addr, f_n, l_n, b_y, b_m, b_d, pw):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("INSERT INTO users(first_name, last_name, birthday_year, birthday_month, birthday_date, create_date_year, create_date_month, create_date_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (f_n, l_n, b_y, b_m, b_d, 0, 0, 0,))
    cur.execute("INSERT INTO user_pw(user_id, pw) VALUES (?, ?)", (cur.lastrowid, pw,))
    con.commit()
    cur.execute
    con.close()

def admin_add_user(db_addr):
    new_user_first_name = input("Please Enter the First Name of the New User:\n")
    new_user_last_name = input("Please Enter the Last Name of the New User:\n")
    new_user_pw = input("Please Enter the Password of the New User:\n")
    new_user(db_addr, new_user_first_name, new_user_last_name, 0, 0, 0, new_user_pw)

def call_func(db_addr, module_name, func_name, func_args):
    if module_name == 'Administrative' and func_name == 'Add User':
        admin_add_user(db_addr)
                    

