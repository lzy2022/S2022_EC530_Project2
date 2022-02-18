# EC530 Project 2 By Zhiyuan Liu
# This file contains the function and constants about the data base
from os.path import exists
from sre_parse import State
from project2_exceptions import UserIdNotExist, PassWordNotMatch
import sqlite3
from module_func import call_func


db_addr = './DB/Project_2.db'

class DB_acc_info:
    
    # initialize the empty dict
    def __init__(self, addr):
        global db_addr
        db_addr = 'null'
        self.state = False
        self.current_uid = 0
        self.current_uname_f = ''
        self.current_uname_l = ''
        self.current_urole = ''
        self.module_list = []
        self.function_dic = {}
        if exists(addr):
            db_addr = addr
        else:
            print("db file not exist\n")
            
    def varify_user(self, u_id, pw):
        con = sqlite3.connect(db_addr)
        cur = con.cursor()
        cur.execute("SELECT * FROM user_pw WHERE user_id = ?", (u_id,))
        user = cur.fetchone()
        # check if the id not exist
        if user == None:
            raise UserIdNotExist
        if user[1] != pw:
            raise PassWordNotMatch
        con.close()
        return True
            
    def user_login(self, user_id, pw):
        self.state = False
        # ==================quick fix
        try:
            self.state = self.varify_user(user_id, pw)
        except UserIdNotExist:
            print('id not exist')
        except PassWordNotMatch:
            print('incorrect pw')
        # ==================quick fix
        if self.state == True:
            self.current_uid = user_id
            con = sqlite3.connect(db_addr)
            cur = con.cursor()
            # get the user's name
            cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            user_info = cur.fetchone()
            self.current_uname_f = user_info[1]
            self.current_uname_l = user_info[2]
            #get the user's role
            self.current_urole = []
            cur.execute("SELECT * FROM user_role WHERE user_id = ?", (user_id,))
            role_info = cur.fetchone()
            # ==================quick fix
            if role_info == None:
                print("no role assigned yet\n")
            # ==================quick fix
            else:
                self.current_urole = role_info[1]
            # get the role's module
            if self.current_urole != []:
                cur.execute("SELECT module_name FROM role_module WHERE role_name = ?", (self.current_urole,))
                m_list = cur.fetchall()
                for row in m_list:
                    self.module_list.append(row[0])
            # set up module-func dictionary
            for module_name in self.module_list:
                self.function_dic[module_name] = []
                cur.execute("SELECT func_name FROM role_module_func WHERE role_name = ? AND module_name = ?", (self.current_urole, module_name,))
                f_list = cur.fetchall()
                for row in f_list:
                    (self.function_dic[module_name]).append(row[0])
            con.close()
            
    def run_module_func(self, module_name, func_name):
        # ==================quick fix
        if self.state == False:
            print("Please Login First")
        # ==================quick fix
        else:
            if module_name not in self.module_list:
                # ==================quick fix
                print("No Access to the module")
                # ==================quick 
            elif func_name not in self.function_dic.get(module_name):
                # ==================quick fix
                print("No Access to the function")
                # ==================quick 
            else:
                call_func(db_addr, module_name, func_name, [])
            