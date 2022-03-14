import requests
import json

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "moduleFunction/Device/Upload Test Record", {'u_id': 18, 'pw': 'ASD'
                                                                                ,'para': [18, 1, json.dumps({'Blood Pressure': 1111, 'Weight': 222}),'New Test']})
print(response.json())