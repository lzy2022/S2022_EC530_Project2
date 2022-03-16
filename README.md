# S2022_EC530_Project2

 [Github Structure](#Github-Structure)
 
 [Api File Structure](#Api-File-Structure)
 
 [Setting up Back-end Sever](#Setting-up-Back-end-Sever)
 
 [Database Structure](#Database-Structure)
 
 [Functions of RESTful API & Request Formates](#Functions-of-RESTful-API-&-Request-Formates)
 
 [----Login Request](#1.Login-Request)
 
 [----Function Request](#2.Function-Request)
 
 [--------Administrative Module](#Administrative-Module)
 
 [--------Device Module](#Device-Module)
 
 [--------Chat Module](#Chat-Module)

## Github Structure
### Top Level
    - .github
    - Code (*The Main Body of the Project)
    - Flake8_Styles
    - requirements.txt
    - README.md
#### Code 
    - DB
        Database back-ups of the project
    - UnitTests
        UnitTests folder contains the Github Action tests for the project
    - UnitTests_Online
        Tests in UnitTests_Online need to set up a remote sever
    - RESTfulFlask_API.py
    - db_info,py
    - db_setup.py
    - module_func.py
    - project2_exceptions.py

## Api File Structure
  #### RESTfulFlask_API.py
  RESTfulFlask_API.py contains the main function of the API. This file is used to launch the back-end server
     
  #### db_info.py
  db_info.py contains the object managing database information & user information. 
  
  #### db_setup.py
  db_setup.py would download a database framework of this project. This module is used in the back-end server setup process
  
  #### module_func.py
  module_func.py implements functions users can call to interact with the database
     
  #### project2_exceptions.py
  project2_exceptions.py contains the exceptions that would raise by the back-end server
  
## Setting up Back-end Sever
        .\db_setup.py [database location]    # only needed for the first time, [database location] should also contains the filename for the database
        .\RESTfulFlask_API.py [database location]
   db_setup.py would set up a database framework by downloading a .db file from S2022_EC530_Project2/Code/DB/Project_2_back.db in this github repositories, the downloaded file would be saved in [database location] (url: https://github.com/lzy2022/S2022_EC530_Project2/raw/main/Code/DB/Project_2_back.db). Users only need to run db_setup.py when they are initializing the sever for the first time. To launch the sever, just enter:
   
        .\RESTfulFlask_API.py [database location]

The framework of the database contains the all the charts & basic infomations to run the sever. A default user account in saved the framework:
        user_id: 1
        pass_word: admin
        name(f&l): Admin Admin
        role: Admin
        
## Database Structure
#### users:
        Contains user_id, user's first/last name, birth date, account creating date
#### user_pw:
        Contains user_id, user's login password
#### roles:
        Contains the list of user's roles in this database, now supporting [Admin], [Doctor], [Nurse] and [Patient]
#### user_role:
        Contains user_id and the corresponding role name. A user can have more than 1 role.
#### modules:
        Contains module_id and module_name of the modules, now supporting [Administrative], [Device] and [Chat]
#### role_module:
        Log different roles' accessibility to each module 
#### role_module_func:
        Log different roles' accessibility to each function (functions implemented in S2022_EC530_Project2/Code/module_func.py)
#### device:
        Contains device_id, device_name, created date and maker information
#### device_maker:
        Contains device maker's information
#### device_parameter:
        Contains acceptable parameters of different devices (device can have more than 1 parameter)
#### device_user:
        Log user's accessibility to different device (match user_id & device_id)
#### record:
        Log user's device record (created date, device_id, user_id, special comments). Record entries/data are in another chart 
#### record_entries:
        Match record_id and record_entries (parameter_name, data & unit). Record may have more than 1 entries
#### chat_group:
        Contains users accessibility to different group chat (user_id & group_id)
#### chat_msg:
        Log chat messages (sender_user_id, receiver_user_id, receiver_group_id)
        
## Functions of RESTful API & Request Formates
The following parts contain formates and functions that can be called from the front-end side using http requests. Users need to import the following python modules:

        import requests
        import json
        
### 1. Login Request
Back-end RESTful API implimentation of the Login Request:

        login_args = reqparse.RequestParser()
        login_args.add_argument("u_id", type=int, help="Need user ID", required=True)
        login_args.add_argument("pw", type=str, help="Need password", required=True)

        class User_Login(Resource):
            def get(self):
                db_ac = DB_acc_info(db_addr)
                args = login_args.parse_args()
                try:
                    db_ac.user_login(args['u_id'], args['pw'])
                except:
                    return {'message':'Login failed!'}, 400
                user_name = db_ac.get_user_name()
                user_role = db_ac.get_user_role()
                user_module = db_ac.get_module_list()
                user_function = db_ac.get_func_dic()
                db_ac.user_logout()
                return {'message':'Loged in', 'user_name': user_name, 'user_role': user_role, 
                        'user_module': user_module, 'user_function':user_function}, 200
                        
        api.add_resource(User_Login, '/login')
                        
http login request can be done using the following request: 

        BASE = "http://127.0.0.1:5000/"
        response = requests.get(BASE + "login", {'u_id': [user_id], 'pw': [user_password]})
        
[response] containse the essential information for the front-end to intialize the local session, including user's first/last name, role, accessibility to modules and functions.

### 2. Function Request
Back-end RESTful API implimentation of the function requests (interact with the Database):

        m_f_args = reqparse.RequestParser()
        m_f_args.add_argument("u_id", type=int, help="Need user ID", required=True)
        m_f_args.add_argument("pw", type=str, help="Need password", required=True)
        m_f_args.add_argument("para", help="Need module name", action="append")

        class Module_Function(Resource):
            def get(self, module_name, function_name):
                db_ac = DB_acc_info(db_addr)
                args = m_f_args.parse_args()
                try:
                    db_ac.user_login(args['u_id'], args['pw'])
                except:
                    return {'message':'Login failed!'}, 400
                f_para = copy.deepcopy(args['para'])
                try:
                    result = db_ac.run_module_func(module_name, function_name, f_para)
                except Error as err:
                    return {'message': err.msg()}, 400
                db_ac.user_logout()
                return result

        api.add_resource(Module_Function, '/moduleFunction/<string:module_name>/<string:function_name>')

All the functions interact with the databse can use the following request formate:
 
        BASE = "http://127.0.0.1:5000/"
        response = requests.get(BASE + "moduleFunction/[module_name]/[function_name]", {'u_id': [user_id], 'pw': [user_password]
                                                                                        ,'para': [list_of_parameters_passed_to_function]})
                                                                                        
For example, to create a new user with name [First Last], birth date [1/1/1000] and password set to be ['PW1'], use the following request:

        response = requests.get(BASE + "moduleFunction/Administrative/Add User", {'u_id': 1, 'pw': 'admin'
                                                                                        ,'para': ['First', 'Last', 1000, 1, 1, 'PW1']})
                                                                                
To access the function [Add User] in module [Administrative], we need a user account with role [Admin], in the example I use the default admin account with user_id = 1, pw = 'admin'. 'para' contains the parameters passed to the function [Add User] and create a new account.

All the available functions are implemented in S2022_EC530_Project2/Code/module_func.py, fowlloing are the module/function names and the required parameters for each function. Accessibility of different roles to the functions can be modified using the [role_module_func] table in the database. 
                                              
### Administrative Module
#### 1. moduleFunction/Administrative/Add User
This function would create a new user account with the given parametes. The new account created would have no role information by default. To assign role information to the new account, use the function [moduleFunction/Administrative/Change User Role]. New account would be automatically assigned a user_id. To view the new user_id of the account created, use the function [moduleFunction/Administrative/Get User List].

Accessible by the following roles:

        Admin
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Administrative/Add User", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[New_First_name], [New_last_name], [New_birthdate_y], [New_birthdate_m], [New_birthdate_d], [New_pass_word]]})
                                                                                        
#### 2. moduleFunction/Administrative/Change User Role
This function would add a new role to an existing user account. Now supporting 4 possible roles: [Admin], [Doctor], [Nurse], [Patient]. 

Accessible by the following roles:

        Admin
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Administrative/Change User Role", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[user_id_assigning], [role_name]]})
 
#### 3. moduleFunction/Administrative/Delete User Info
This function would delete an existing user account. All the related information including device record and user_id would be removed from the database (group messages would be kept)

Accessible by the following roles:

        Admin
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Administrative/Delete User Info", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[user_id_deleting]]})

#### 4. moduleFunction/Administrative/Get User List
This function would return a list of users as response, including all the user_id and the corresponding first/last names and role information. Front-end can refer to the user list and implement a search function to look for specific user and his/her user_id. 

Accessible by the following roles:

        ALL ROLES
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Administrative/Get User List", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': []})
                                                                                        
                                                                                        
### Device Module
#### 1. moduleFunction/Device/Add Device
This function would create a new device information in the database. The created device would contains [device_id](auto-assigned), [device_name], [maker_name] and [state]. A new device would have no available parameter as default. To add parameter to the device, use the function [moduleFunction/Device/Add Device Parameter]. A device could have more than 1 parameter.

Accessible by the following roles:

        Admin
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Device/Add Device", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[device_name], [maker_name], [state]]})
                                                                                        
#### 2. moduleFunction/Device/Get Device List
This function would return a list containing all the device_name and the corresponding device_id. Front-end can refer to the device list and implement a search function to look for specific device and it's device_id. 


Accessible by the following roles:

        ALL ROLES
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Device/Get Device List", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': []})   

#### 3. moduleFunction/Device/Add Device Parameter
This function would add a new parameter to an existing device in terms of [parameter_name] & [parameter_unit]. Each device may have more than 1 parameter 

Accessible by the following roles:

        Admin
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Device/Add Device Parameter", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[parameter_name], [parameter_unit]]})  

#### 4. moduleFunction/Device/Check Device Parameter
This function would return the list of parameters and units corresponding a single device (refering to the device using [device_id]). Front-end could use the list of parameters to a generate report chart for the user to fill.

Accessible by the following roles:

        ALL ROLES
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Device/Check Device Parameter", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[device_id]]})

#### 5. moduleFunction/Device/Clear Device Parameter
This function would clear all the parameters currently assigned to the device. User can clear all the current parameters and assign new ones to the device.

Accessible by the following roles:

        Admin
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Device/Check Device Parameter", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[device_id]]})

#### 6. moduleFunction/Device/Assign Device
This function would assign the device to a user. User can upload test report only with the devices they have access to. A User can be assigned more than 1 device and each device can be assigned to more than 1 user.

Accessible by the following roles:

        Admin
        Doctor
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Device/Check Device Parameter", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[device_id], [assigning_user_id], [text_comment]]})

#### 7. moduleFunction/Device/Upload Test Record
This function would upload a test record from a corresponding user and device. Each entry in the record contains [parameter_name], [data] and [parameter_unit]. This function would check the available parameters of the device and log only the appropriate parameters into the data base.

[record] is a python dictionary object and need to be dumped using jason.dumps(). Each entry in the record. Names of the parameter must match the available parameters of the device, or else the entry would be recognized as inappropriate and ignored

        record = json.dumps({parameter_1: data_1, parameter_2: data_2, ...})

Accessible by the following roles:

        Patient
        Doctor
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Device/Upload Test Record", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[user_id], [device_id], [record], [text_comment]]})
                                                                                        
#### 8. moduleFunction/Device/View Patient Test Records
This function would return a list of test records corresponding to a [user_id]. Each record includes [device_id], [user_id], a list of record entries, and upload time. Each record entry contains [parameter_name], [data] and [parameter_unit].

Accessible by the following roles:

        Admin
        Doctor
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Device/View Patient Test Records", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[assigning_user_id]]})

#### 9. moduleFunction/Device/View Your Test Records
This function would return a list of test records corresponding to the current user. Each record includes [device_id], [user_id], a list of record entries, and upload time. Each record entry contains [parameter_name], [data] and [parameter_unit].

Accessible by the following roles:

        Patient
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Device/View Patient Test Records", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': []})
                                                                                        
### Chat Module
#### 1. moduleFunction/Chat/Create Chat Group
This function would create a new chat group with specified [group_name] and [group_id] (group_id need to be unique). A new chat groupe would include only the current user (creater of the group). To add or remove users, use the function [moduleFunction/Chat/Add User to Chat Group] and [moduleFunction/Chat/Remove User from Chat Group]

Accessible by the following roles:

        ALL ROLES
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Chat/Create Chat Group", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[group_name], [group_id]]})
                                                                                        
#### 2. moduleFunction/Chat/Add User to Chat Group
This function would assgin user access to a specific group. Only user who is currently in the group can add another user into the group (refered using [user_id] and [group_id]). Having access to a group means the user can send/receive message or add/remove users in the group.

Accessible by the following roles:

        ALL ROLES
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Chat/Create Chat Group", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[user_id_adding], [group_id]]})
                                                                                        
#### 3. moduleFunction/Chat/Remove User from Chat Group
This function would remove a specific user from the caht group. Only user who is currently in the group can remove user from the group (refered using [user_id] and [group_id]).

Accessible by the following roles:

        ALL ROLES
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Chat/Create Chat Group", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[user_id_removing], [group_id]]})
                                                                                        
#### 4. moduleFunction/Chat/Send Message
This function would send text message to a chat group or a specific user (using [user_id] and [group_id]). If the user don't want this message being sent to any user (or any group), use [-1] for the [user_id] (or [group_id]). But there must be at least one valid receiver in [user_id] and [group_id]. If the message is sent to a group, the sender must be a member of that group.

Accessible by the following roles:

        ALL ROLES
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Chat/Send Message", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[user_id_sending], [group_id_sending], [text_message]]})

#### 6. moduleFunction/Chat/View Your Message
This function would return a list of chat message sent to the current user (only the individual message, not group chat). Each message contains [sender_user_id], [receiver_user_id], [receiving_group_id], [time], [text_content]

Accessible by the following roles:

        ALL ROLES
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Chat/View Your Message", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': []})
                                                                                        
#### 7. moduleFunction/Chat/View Group Message
This function would return a list of chat message sent to the specific group chat. Each message contains [sender_user_id], [receiver_user_id], [receiving_group_id], [time], [text_content]. Users must have access to the group before viewing group messages.

Accessible by the following roles:

        ALL ROLES
        
Request Formate:

        response = requests.get(BASE + "moduleFunction/Chat/View Group Message", {'u_id': [your_account_id], 'pw': [your_account_pw]
                                                                                        ,'para': [[group_id_viewing]]})
