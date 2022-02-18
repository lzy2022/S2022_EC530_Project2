from project2_exceptions import PassWordNotMatch, UserIdNotExist
from pw_check import varify_user


def main():
    result = False
    try:
        result = varify_user(3, 'admin')
    except UserIdNotExist:
        print('id not exist')
    except PassWordNotMatch:
        print('incorrect pw')
    if result == True:
        print("Hello!")

if __name__ == "__main__":
    main()