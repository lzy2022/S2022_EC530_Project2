import sys
import os
# adding the parent directory to
# the sys.path.
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from project2_exceptions import UserIdNotExist, PassWordNotMatch
from pw_check import varify_user

def test_adminlogin_1():
    result = False
    try:
        result = varify_user(1, 'admin')
    except UserIdNotExist:
        assert 0 == 1
    except PassWordNotMatch:
        assert 0 == 1
    if result == True:
        assert 1 == 1

def test_adminlogin_2():
    result = False
    try:
        result = varify_user(99, 'admin')
    except UserIdNotExist:
        assert 1 == 1
    except PassWordNotMatch:
        assert 0 == 1
    if result == True:
        assert 0 == 1
        
def test_adminlogin_3():
    result = False
    try:
        result = varify_user(1, 'adminnnnnnnn')
    except UserIdNotExist:
        assert 0 == 1
    except PassWordNotMatch:
        assert 1 == 1
    if result == True:
        assert 0 == 1