# EC530 Project 2 By Zhiyuan Liu
# This file contains the EXCEPTION classes

class Error(Exception):
    """Base Class"""
    pass

class UserIdNotExist(Error):
    pass

class PassWordNotMatch(Error):
    pass

class RoleNotExist(Error):
    pass