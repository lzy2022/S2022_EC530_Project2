import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "moduleFunction/Device/View Your Test Records", {'u_id': 16, 'pw': 'pw1234',
                                                      'module_n': 'Device', 'function_n': 'View Your Test Records', 'para': [16]})
print(response.json())