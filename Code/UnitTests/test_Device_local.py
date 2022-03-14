import sys
import os
# adding the parent directory to
# the sys.path.
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from db_info import DB_acc_info

db_addr = './Project_2_test.db'

def test_add_device():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(1, 'admin')
    result = db_ac.run_module_func('Device', 'Add Device', ['Test_Device', 'Test_Maker', 1])
    assert result['message'] == 'Device Added'
    pass

def test_get_devicelist():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(1, 'admin')
    result = db_ac.run_module_func('Device', 'Get Device List', [])
    assert result[0]['device_name'] == 'Test_Device'
    pass

def test_add_parameter():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(1, 'admin')
    result = db_ac.run_module_func('Device', 'Add Device Parameter', [1, 'Weight', 'Kg'])
    assert result['message'] == 'Parameter Added'
    pass

def test_get_parameterlist():
    db_ac = DB_acc_info(db_addr)
    db_ac.user_login(1, 'admin')
    result = db_ac.run_module_func('Device', 'Check Device Parameter', [1])
    assert result[0]['Weight'] == 'Kg'
    pass