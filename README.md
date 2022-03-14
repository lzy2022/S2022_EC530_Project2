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
  ### RESTfulFlask_API.py
     RESTfulFlask_API.py contains the main function of the API. This file is used to launch the back-end server
     
  ### db_info.py
     db_info.py contains the object managing database information & user information. 
  
  ### db_setup.py
     db_setup.py would download a database framework of this project. This module is used in the back-end server setup process
  
  ### module_func.py
     module_func.py implements functions users can call to interact with the database
     
  ### project2_exceptions.py
     project2_exceptions.py contains the exceptions that would raise by the back-end server
     
