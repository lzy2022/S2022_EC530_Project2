import requests
import json

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "moduleFunction/Chat/View Your Message", {'u_id': 1, 'pw': 'admin'
                                                                                ,'para': []})
print(response.json())

response = requests.get(BASE + "moduleFunction/Chat/View Group Message", {'u_id': 1, 'pw': 'admin'
                                                                                ,'para': [123]})
print(response.json())

