import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "moduleFunction/Device/Get Device List", {'u_id': 1, 'pw': 'admin',
                                                      'module_n': 'Administrative', 'function_n': 'Get User List', 'para': ['A','B',0,0,0,'ASD']})
print(response.json())