import sys
import os
# adding the parent directory to
# the sys.path.
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import requests
import json

BASE = "http://127.0.0.1:5000/"

def test_add_user():
    response = requests.get(BASE + "moduleFunction/Chat/View Group Message", {'u_id': 1, 'pw': 'admin'
                                                                                ,'para': ['A', 'B', 0, 0 ,0 , 'PW1']})
    assert response.json() == {'message':'New User Added'}
    
def test_change_role():
    response = requests.get(BASE + "moduleFunction/Chat/View Group Message", {'u_id': 1, 'pw': 'admin'
                                                                                ,'para': ['A', 'B', 0, 0 ,0 , 'PW1']})
    assert response.json() == {'message':'New User Added'}