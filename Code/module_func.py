# EC530 Project 2 By Zhiyuan Liu
# This file contains the module functions
from copy import deepcopy
import sqlite3
from project2_exceptions import NoAccessToChatGroup
from project2_exceptions import DeviceIdNotExist, NoAdmissionToAccessDevice, PassWordNotMatch, RoleNotExist, UserIdNotExist
import datetime

def new_user(db_addr, f_n, l_n, b_y, b_m, b_d, pw):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("INSERT INTO users(first_name, last_name, birthday_year, birthday_month, birthday_date, create_date_year, create_date_month, create_date_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (f_n, l_n, b_y, b_m, b_d, 0, 0, 0,))
    cur.execute("INSERT INTO user_pw(user_id, pw) VALUES (?, ?)", (cur.lastrowid, pw,))
    con.commit()
    con.close()
    return {'message':'New User Added'}
    
def check_user(db_addr, u_id):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    # check if the user not exist
    cur.execute("SELECT * FROM users WHERE user_id = ?", (u_id,))
    u = cur.fetchone()
    con.close()
    # check if the id not exist
    if u == None:
        return False
    return True

def check_device(db_addr, d_id):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    # check if the user not exist
    cur.execute("SELECT * FROM device WHERE device_id = ?", (d_id,))
    u = cur.fetchone()
    con.close()
    # check if the id not exist
    if u == None:
        return False
    return True    
    
def change_user_role(db_addr, u_id, role_name):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE user_id = ?", (u_id,))
    u = cur.fetchone()
    # check if the id not exist
    if u == None:
        con.close()
        raise UserIdNotExist
    cur.execute("SELECT * FROM roles WHERE role_name = ?", (role_name,))
    r = cur.fetchone()
    # check if the ROLE not exist
    if r == None:
        con.close()
        raise RoleNotExist
    # Set the rold
    cur.execute("INSERT INTO user_role(user_id, role) VALUES (?, ?)", (u_id, role_name,))
    con.commit()
    con.close()
    return {'message':'Role Changed'}

def delete_user(db_addr, u_id):
    if check_user(db_addr, u_id) == False:
        raise UserIdNotExist
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE user_id = ?", (u_id,))
    con.commit()
    con.close()
    return {'message':'User Deleted'}

def get_user_list(db_addr):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT user_id, first_name, last_name FROM users")
    u = cur.fetchall()
    con.close()
    user_list = []
    for row in u:
        user_list.append({'user_id':row[0],
                      'first_name':row[1],
                      'last_name':row[2]})
    return user_list
    
def add_device(db_addr, d_name, m_name, state):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    # Check if the maker already exist
    cur.execute("SELECT * FROM device_maker WHERE maker_name = ?", (m_name,))
    r = cur.fetchone()
    if r == None:
        cur.execute("INSERT INTO device_maker (maker_name) VALUES (?)",(m_name,))
    # insert the device
    cur.execute("INSERT INTO device (device_name, create_date_year, create_date_month, create_date_date, maker_name, device_state) VALUES (?, ?, ?, ?, ?, ?)",
                (d_name, 0, 0, 0, m_name, state,))
    con.commit()
    con.close()
    return {'message':'Device Added'}

def assign_device(db_addr, d_id, u_id, comment):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    # check if the user not exist
    cur.execute("SELECT * FROM users WHERE user_id = ?", (u_id,))
    u = cur.fetchone()
    # check if the id not exist
    if u == None:
        con.close()
        raise UserIdNotExist
    #check if the device not exist
    cur.execute("SELECT * FROM device WHERE device_id = ?", (d_id,))
    u = cur.fetchone()
    # check if the id not exist
    if u == None:
        con.close()
        raise DeviceIdNotExist
    # check if already exist
    cur.execute("SELECT * FROM device_user WHERE device_id = ? AND user_id = ?", (d_id, u_id,))
    u = cur.fetchone()
    if u != None:
        # do nothing
        return 0
    # assign to the user
    cur.execute("INSERT INTO device_user (device_id, user_id, comment) VALUES (?, ?, ?)",(d_id, u_id, comment,))
    con.commit()
    con.close()
    return {'message':'Device Assigned'}

def add_device_para(db_addr, d_id, para_name, unit):
    if check_device(db_addr, d_id) == False:
        raise DeviceIdNotExist
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("INSERT INTO device_parameter (device_id, parameter_name, unit) VALUES (?, ?, ?)",(d_id, para_name, unit,))
    con.commit()
    con.close()
    return {'message':'Parameter Added'}

def get_device_para(db_addr, d_id):
    if check_device(db_addr, d_id) == False:
        raise DeviceIdNotExist
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT * FROM device_parameter WHERE device_id = ?", (d_id,))
    u = cur.fetchall()
    con.close()
    para = {}
    for row in u:
        para[row[1]] = row[2]
    return para

def clear_device_para(db_addr, d_id):
    if check_device(db_addr, d_id) == False:
        raise DeviceIdNotExist
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("DELETE FROM device_parameter WHERE device_id = ?", (d_id,))
    con.commit()
    con.close()
    return {'message':'Parameter Cleared'}

def get_device_list(db_addr):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT device_id, device_name FROM device")
    u = cur.fetchall()
    con.close()
    d_list = []
    for row in u:
        d_list.append({'device_id':row[0],
                      'device_name':row[1]})
    return d_list

def get_user_device_list(db_addr, u_id):
    if check_user(db_addr, u_id) == False:
        raise UserIdNotExist
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT device_id FROM device_user WHERE user_id = ?", (u_id,))
    u = cur.fetchall()
    d_list = []
    for row in u:
        cur.execute("SELECT device_name FROM device WHERE device_id = ?", (row[0],))
        v = cur.fetchone()
        d_list.append({'device_id':row[0],
                      'device_name':v[0]})
    con.close()
    return d_list

def add_record_entry(db_addr, r_id, para_name, data, unit):
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("INSERT INTO record_entries (record_id, parameter_name, data, unit) VALUES (?, ?, ?, ?)",(r_id, para_name, data, unit,))
    con.commit()
    con.close()
    
def check_device_admission(db_addr, d_id, u_id):
    if check_user(db_addr, u_id) == False:
        raise UserIdNotExist
    if check_device(db_addr, d_id) == False:
        raise DeviceIdNotExist
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    # check if admission exist
    cur.execute("SELECT * FROM device_user WHERE device_id = ? AND user_id = ?", (d_id, u_id,))
    u = cur.fetchone()
    con.close()
    if u == None:
        return False
    return True
    
def add_record(db_addr, u_id, d_id, record, comment):
    if check_user(db_addr, u_id) == False:
        raise UserIdNotExist
    if check_device(db_addr, d_id) == False:
        raise DeviceIdNotExist
    if check_device_admission(db_addr, d_id, u_id) == False:
        raise NoAdmissionToAccessDevice
    para = get_device_para(db_addr, d_id)
    # insert the record
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("INSERT INTO record (device_id, user_id, date_year, date_month, date_date, comment) VALUES (?, ?, ?, ?, ?, ?)",
                (d_id, u_id, 0, 0, 0, comment,))
    r_id = cur.lastrowid
    con.commit()
    con.close()
    device_para = get_device_para(db_addr,d_id)
    for para in record.keys():
        if para in device_para.keys():
            add_record_entry(db_addr, r_id, para, record[para], device_para[para])
    return {'message':'Record Added'}, 201
            
def get_user_record(db_addr, u_id):
    if check_user(db_addr, u_id) == False:
        raise UserIdNotExist
    record_list = []
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT * FROM record WHERE user_id = ?", (u_id,))
    u = cur.fetchall()
    for row in u:
        record = {}
        entries = []
        record['record_id'] = row[0]
        record['device_id'] = row[1]
        record['user_id'] = row[2]
        record['year'] = row[3]
        record['month'] = row[4]
        record['date'] = row[5]
        record['comment'] = row[6]
        cur.execute("SELECT * FROM record_entries WHERE record_id = ?", (row[0],))
        v = cur.fetchall()
        for e in v:
            entries.append([e[1], e[2], e[3]])
        record['entries'] = deepcopy(entries)
        record_list.append(deepcopy(record))
    con.close()
    return record_list

def check_user_chat_group(db_addr, u_id, g_id):
    if check_user(db_addr, u_id) == False:
        raise UserIdNotExist
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    # check if admission exist
    cur.execute("SELECT * FROM chat_group WHERE user_id = ? AND group_id = ?", (u_id, g_id,))
    u = cur.fetchone()
    con.close()
    if u == None:
        return False
    return True

def get_user_chat_group(db_addr, u_id):
    if check_user(db_addr, u_id) == False:
        raise UserIdNotExist
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT group_id, group_name FROM chat_group WHERE user_id = ?", (u_id,))
    u = cur.fetchall()
    con.close()
    g_list = []
    for row in u:
        g_list.append({'group_id': row[0], 'group_name': row[1]})
    return g_list

def create_chat_group(db_addr, u_id, g_name, g_id):
    if check_user(db_addr, u_id) == False:
        raise UserIdNotExist
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    # check if admission exist
    cur.execute("SELECT * FROM chat_group WHERE group_id = ?", (g_id,))
    u = cur.fetchone()
    if u != None:
        con.close()
        raise NoAccessToChatGroup
    cur.execute("INSERT INTO chat_group (group_id, group_name, user_id) VALUES (?, ?, ?)",(g_id, g_name, u_id,))
    con.commit()
    con.close()
    

def add_user_chat_group(db_addr, u_id_s, u_id_r, g_id):
    if check_user(db_addr, u_id_s) == False:
        raise UserIdNotExist
    if check_user(db_addr, u_id_r) == False:
        raise UserIdNotExist
    if check_user_chat_group(db_addr, u_id_s, g_id) == False:
        raise NoAccessToChatGroup
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT group_name FROM chat_group WHERE group_id = ?", (g_id,))
    u = cur.fetchone()
    g_name = u[0]
    cur.execute("INSERT INTO chat_group (group_id, group_name, user_id) VALUES (?, ?, ?)",(g_id, g_name, u_id_r,))
    con.commit()
    con.close()
    
    return {'message':'Added User to the Chat Group'}

def remove_user_chat_group(db_addr, u_id_s, u_id_r, g_id):
    if check_user(db_addr, u_id_s) == False:
        raise UserIdNotExist
    if check_user(db_addr, u_id_r) == False:
        raise UserIdNotExist
    if check_user_chat_group(db_addr, u_id_s, g_id) == False:
        raise NoAccessToChatGroup
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("DELETE FROM chat_group WHERE user_id = ? AND group_id = ?", (u_id_r, g_id,))
    con.commit()
    con.close()
    
    return {'message':'Removed User from the Chat Group'}

def send_msg(db_addr, u_id_s, u_id_r, g_id, msg):
    if check_user(db_addr, u_id_s) == False:
        raise UserIdNotExist
    if check_user(db_addr, u_id_r) == False and check_user_chat_group(db_addr, u_id_s, g_id) == False:
        raise NoAccessToChatGroup
    msg_time = datetime.datetime.now()
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("INSERT INTO chat_msg (user_id_s, user_id_r, group_id, content, time) VALUES (?, ?, ?, ?, ?)",
                (u_id_s, u_id_r, g_id, msg, msg_time,))
    con.commit()
    con.close()

    return {'message':'Message Sent'}

def view_user_msg(db_addr, u_id):
    if check_user(db_addr, u_id) == False:
        raise UserIdNotExist
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT * FROM chat_msg WHERE user_id_r = ? ORDER BY time DESC", (u_id,))
    u = cur.fetchall()
    con.close()
    msg_list = []
    for row in u:
        msg_list.append({'from': row[1], 'to': row[2], 'group': row[3], 'time': row[4], 'content': row[0]})
    return msg_list

def view_group_msg(db_addr,u_id, g_id):
    if check_user(db_addr, u_id) == False:
        raise UserIdNotExist
    if check_user_chat_group(db_addr, u_id, g_id) == False:
        raise NoAccessToChatGroup
    con = sqlite3.connect(db_addr)
    cur = con.cursor()
    cur.execute("SELECT * FROM chat_msg WHERE group_id = ? ORDER BY time DESC", (g_id,))
    u = cur.fetchall()
    con.close()
    msg_list = []
    for row in u:
        msg_list.append({'from': row[1], 'to': row[2], 'group': row[3], 'time': row[4], 'content': row[0]})
    return msg_list
    
def call_func(db_addr, module_name, func_name, u_id, func_args):
    # Administrative
    if module_name == 'Administrative' and func_name == 'Add User':
        return new_user(db_addr, func_args[0], func_args[1], func_args[2], func_args[3], func_args[4], func_args[5])
    if module_name == 'Administrative' and func_name == 'Change User Role':
        return change_user_role(db_addr, func_args[0], func_args[1])
    if module_name == 'Administrative' and func_name == 'Delete User Info':
        return delete_user(db_addr, func_args[0])
    if module_name == 'Administrative' and func_name == 'Get User List':
        return get_user_list(db_addr)
    # Device
    if module_name == 'Device' and func_name == 'Add Device':
        return add_device(db_addr, func_args[0], func_args[1], func_args[2])
    if module_name == 'Device' and func_name == 'Get Device List':
        return get_device_list(db_addr)
    if module_name == 'Device' and func_name == 'Check Device Parameter':
        return get_device_para(db_addr, func_args[0])
    if module_name == 'Device' and func_name == 'Clear Device Parameter':
        return clear_device_para(db_addr, func_args[0])
    if module_name == 'Device' and func_name == 'Add Device Parameter':
        return add_device_para(db_addr, func_args[0], func_args[1], func_args[2])
    if module_name == 'Device' and func_name == 'Assign Device':
        return assign_device(db_addr, func_args[0], func_args[1], func_args[2])
    if module_name == 'Device' and func_name == 'Upload Test Record':
        return add_record(db_addr, func_args[0], func_args[1], func_args[2], func_args[3])
    if module_name == 'Device' and func_name == 'View Patient Test Records':
        return get_user_record(db_addr, func_args[0])
    if module_name == 'Device' and func_name == 'View Your Test Records':
        return get_user_record(db_addr, u_id)
    # Chat
    if module_name == 'Chat' and func_name == 'Create Chat Group':
        return create_chat_group(db_addr, u_id, func_args[0], func_args[1])
    if module_name == 'Chat' and func_name == 'Add User to Chat Group':
        return add_user_chat_group(db_addr, u_id, func_args[0], func_args[1])
    if module_name == 'Chat' and func_name == 'Remove User from Chat Group':
        return remove_user_chat_group(db_addr, u_id, func_args[0], func_args[1])
    if module_name == 'Chat' and func_name == 'Send Message':
        return send_msg(db_addr, u_id, func_args[0], func_args[1], func_args[2])
    if module_name == 'Chat' and func_name == 'View Your Message':
        return view_user_msg(db_addr, u_id)
    if module_name == 'Chat' and func_name == 'View Group Message':
        return view_group_msg(db_addr, u_id, func_args[1])
    return None
