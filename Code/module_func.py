# EC530 Project 2 By Zhiyuan Liu
# This file contains the module functions
from asyncio.windows_events import NULL
from re import U
import sqlite3
from project2_exceptions import PassWordNotMatch, RoleNotExist, UserIdNotExist

def new_user(db_addr, f_n, l_n, b_y, b_m, b_d, pw):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("INSERT INTO users(first_name, last_name, birthday_year, birthday_month, birthday_date, create_date_year, create_date_month, create_date_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (f_n, l_n, b_y, b_m, b_d, 0, 0, 0,))
    cur.execute("INSERT INTO user_pw(user_id, pw) VALUES (?, ?)", (cur.lastrowid, pw,))
    con.commit()
    con.close()

def admin_add_user(db_addr):
    new_user_first_name = input("Please Enter the First Name of the New User:\n")
    new_user_last_name = input("Please Enter the Last Name of the New User:\n")
    new_user_pw = input("Please Enter the Password of the New User:\n")
    new_user(db_addr, new_user_first_name, new_user_last_name, 0, 0, 0, new_user_pw)
    
def change_user_role(db_addr, u_id, role_name):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = ?", (u_id,))
    u = cur.fetchone()
    # check if the id not exist
    if u == None:
        raise UserIdNotExist
    cur.execute("SELECT * FROM roles WHERE role_name = ?", (role_name,))
    r = cur.fetchone()
    # check if the ROLE not exist
    if r == None:
        raise RoleNotExist
    # Set the rold
    cur.execute("INSERT INTO user_role(user_id, role) VALUES (?, ?)", (u_id, role_name,))
    con.commit()
    con.close()
    
def admin_change_user_role(db_addr):
    u_id = input("Please Enter the User ID of the User being Changed:\n")
    role_name = input("Please Enter the New Role:\n")
    change_user_role(db_addr, u_id, role_name)
    

def call_func(db_addr, module_name, func_name, func_args):
    if module_name == 'Administrative' and func_name == 'Add User':
        admin_add_user(db_addr)
    if module_name == 'Administrative' and func_name == 'Change User Role':
        admin_change_user_role(db_addr)

                    

