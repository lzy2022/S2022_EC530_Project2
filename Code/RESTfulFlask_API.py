from flask import Flask
from flask_restful import Api, Resource, reqparse
from db_info import DB_acc_info
import random

app = Flask(__name__)
api = Api(app)

db_addr = './DB/Project_2.db'
session_list = {}
session_list[0] = DB_acc_info(db_addr)

def get_DB_Acc_session(session_id):
    return session_list[session_id]

def new_DB_Acc_session(u_id, pw):
    session_id = random.randint(1000, 3000)
    session_list[session_id] = DB_acc_info(db_addr)
    session_list[session_id].user_login(u_id, pw)
    return session_id

class User_Login(Resource):
    def get(self):
        return {'msg': "Hello"}
    
api.add_resource(H, "/hello")

if __name__ == "__main__":
    app.run(debug=True)