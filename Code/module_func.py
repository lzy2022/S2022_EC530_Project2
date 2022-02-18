# EC530 Project 2 By Zhiyuan Liu
# This file contains the module functions
from asyncio.windows_events import NULL
from db_info import db_addr
import sqlite3
from project2_exceptions import PassWordNotMatch, UserIdNotExist

def new_user(f_n, l_n, b_y, b_m, b_d, pw):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("INSERT INTO users(first_name, last_name, birthday_year, birthday_month, birthday_date, create_date_year, create_date_month, create_date_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (f_n, l_n, b_y, b_m, b_d, 0, 0, 0,))
    con.commit()
    con.close()

def admin_add_user():
    new_user_first_name = input("Please Enter the First Name of the New User:\n")
    new_user_last_name = input("Please Enter the First Name of the New User:\n")
    new_user_pw = input("Please Enter the Password of the New User:\n")
    new_user(new_user_first_name, new_user_last_name, 0, 0, 0, new_user_pw)

# def call_func(func_name):
    

