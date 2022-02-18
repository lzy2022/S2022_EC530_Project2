from project2_exceptions import PassWordNotMatch, UserIdNotExist
from pw_check import varify_user
from module_func import new_user
from db_info import DB_acc_info


def main():
    db_ac = DB_acc_info('./DB/Project_2.db')
    db_ac.user_login(1, 'admin')
    db_ac.run_module_func('Administrative', 'Add User', [])
    db_ac.run_module_func('Administrative', 'Change User Role', [])

if __name__ == "__main__":
    main()