import sys
import os
# adding the parent directory to
# the sys.path.
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from db_info import DB_acc_info

db_addr = './Project_2_test.db'

def test_add_user():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(1, 'admin')
    result = db_ac.run_module_func('Administrative', 'Add User', ['A', 'B', 0, 0 ,0 , 'PW1'])
    assert result['message'] == 'New User Added'
    pass

def test_change_role():
    pass

def test_delete_user():
    pass