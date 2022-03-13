# EC530 Project 2 By Zhiyuan Liu
# This file contains the EXCEPTION classes

class Error(Exception):
    """Base Class"""
    pass

class UserIdNotExist(Error):
    def msg(self):
        return 'UserIdNotExist'
    pass

class DeviceIdNotExist(Error):
    def msg(self):
        return 'DeviceIdNotExist'
    pass

class PassWordNotMatch(Error):
    def msg(self):
        return 'PassWordNotMatch'
    pass

class RoleNotExist(Error):
    def msg(self):
        return 'RoleNotExist'
    pass

class NoAdmissionToAccessDevice(Error):
    def msg(self):
        return 'NoAdmissionToAccessDevice'
    pass

class RequireUserLogin(Error):
    def msg(self):
        return 'RequireUserLogin'
    pass

class NoAccessToModuleOrFunction(Error):
    def msg(self):
        return 'NoAccessToModuleOrFunction'
    pass

class NoAccessToChatGroup(Error):
    def msg(self):
        return 'NoAccessToChatGroup'
    pass