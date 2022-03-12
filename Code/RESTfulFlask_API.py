from ast import arg
from flask import Flask
from flask_restful import Api, Resource, reqparse
from numpy import require
from db_info import DB_acc_info
import random
import copy
from project2_exceptions import Error

app = Flask(__name__)
api = Api(app)

db_addr = './DB/Project_2.db'

db_ac = DB_acc_info(db_addr)

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

m_f_args = reqparse.RequestParser()
m_f_args.add_argument("u_id", type=int, help="Need user ID", required=True)
m_f_args.add_argument("pw", type=str, help="Need password", required=True)
m_f_args.add_argument("module_n", type=str, help="Need module name")
m_f_args.add_argument("function_n", type=str, help="Need function name")
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

    
api.add_resource(User_Login, '/login')
api.add_resource(Module_Function, '/moduleFunction/<string:module_name>/<string:function_name>')

if __name__ == "__main__":
    app.run(debug=True)