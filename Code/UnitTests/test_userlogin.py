import sys
import os
# adding the parent directory to
# the sys.path.
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from project2_exceptions import UserIdNotExist, PassWordNotMatch
from db_info import DB_acc_info

def test_adminlogin_1():
    db_acc = DB_acc_info('./DB/Project_2.db')
    try:
        db_acc.user_login(1, 'admin')
    except UserIdNotExist:
        assert 0 == 1
    except PassWordNotMatch:
        assert 0 == 1
    assert 1 == 1

def test_adminlogin_2():
    db_acc = DB_acc_info('./DB/Project_2.db')
    try:
        db_acc.user_login(100, 'admin')
    except UserIdNotExist:
        assert 1 == 1
    except PassWordNotMatch:
        assert 0 == 1
    assert 0 == 1
        
def test_adminlogin_3():
    db_acc = DB_acc_info('./DB/Project_2.db')
    try:
        db_acc.user_login(1, 'adminnnnnnnn')
    except UserIdNotExist:
        assert 0 == 1
    except PassWordNotMatch:
        assert 1 == 1
    assert 0 == 1