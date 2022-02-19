from db_info import DB_acc_info

def text_UI_add_user(db_acc):
    new_user_first_name = input("Please Enter the First Name of the New User:\n")
    new_user_last_name = input("Please Enter the Last Name of the New User:\n")
    new_user_pw = input("Please Enter the Password of the New User:\n")
    db_acc.run_module_func('Administrative', 'Add User', [new_user_first_name, new_user_last_name, 0, 0, 0, new_user_pw])
    
def text_UI_change_user_role(db_acc):
    u_id = input("Please Enter the User ID of the User being Changed:\n")
    role_name = input("Please Enter the New Role:\n")
    db_acc.run_module_func('Administrative', 'Change User Role', [u_id, role_name])