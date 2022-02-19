from project2_exceptions import PassWordNotMatch, UserIdNotExist
from pw_check import varify_user
from module_func import new_user
from db_info import DB_acc_info
from text_UI_interface import text_UI_add_user, text_UI_change_user_role


def main():
    db_ac = DB_acc_info('./DB/Project_2.db')
    db_ac.user_login(8, 'default')
    text_UI_add_user(db_ac)
    text_UI_change_user_role(db_ac)

if __name__ == "__main__":
    main()