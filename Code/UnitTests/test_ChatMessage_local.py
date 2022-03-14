import sys
import os
# adding the parent directory to
# the sys.path.
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from db_info import DB_acc_info
import json

db_addr = './Project_2_test.db'

def test_add_user():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(1, 'admin')
    result = db_ac.run_module_func('Administrative', 'Add User', ['A', 'B', 0, 0 ,0 , 'PW1'])
    assert result['message'] == 'New User Added'
    pass

def test_send_message():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(1, 'admin')
    result = db_ac.run_module_func('Chat', 'Send Message', [2, -1, 'Test Message'])
    assert result['message'] == 'Message Sent'
    pass

def test_receive_message():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(2, 'PW1')
    result = db_ac.run_module_func('Chat', 'View Your Message', [])
    assert result[0]['content'] == 'Test Message'
    pass

def test_creat_chatgroup():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(1, 'admin')
    result = db_ac.run_module_func('Chat', 'Create Chat Group', ['Test Group', 123])
    assert result['message'] == 'Chat Group Created'
    pass

def test_adduser_chatgroup():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(1, 'admin')
    result = db_ac.run_module_func('Chat', 'Add User to Chat Group', [2, 123])
    assert result['message'] == 'Added User to the Chat Group'
    pass

def test_send_groupmsg():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(2, 'PW1')
    result = db_ac.run_module_func('Chat', 'Send Message', [-1, 123, 'Test Group Message'])
    assert result['message'] == 'Message Sent'
    pass

def test_receive_groupmsg():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(1, 'admin')
    result = db_ac.run_module_func('Chat', 'View Group Message', [123])
    assert result[0]['content'] == 'Test Group Message'
    pass

def test_remove_groupuser():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(1, 'admin')
    result = db_ac.run_module_func('Chat', 'Remove User from Chat Group', [2, 123])
    assert result['message'] == 'Removed User from the Chat Group'
    pass