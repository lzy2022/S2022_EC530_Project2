# S2022_EC530_Project2

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
        
## Database Structure (Tables)
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
     
