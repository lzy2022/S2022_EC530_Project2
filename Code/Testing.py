from project2_exceptions import PassWordNotMatch, UserIdNotExist
from pw_check import varify_user
from module_func import new_user


def main():
    result = False
    try:
        result = varify_user(1, 'admin')
    except UserIdNotExist:
        print('id not exist')
    except PassWordNotMatch:
        print('incorrect pw')
    if result == True:
        print("Hello!")
    new_user('a', 'b', 0, 0, 0, 'default')

if __name__ == "__main__":
    main()