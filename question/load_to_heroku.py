import requests
import os, json
from requests_toolbelt.multipart.encoder import MultipartEncoder

API_URL = "https://django-nba-backend.herokuapp.com/api/player/"


os.chdir('/Users/boden/docs/nba-site/nba/question/json_data_correct')
list_of_json = os.listdir()

for x in list_of_json:
    with open(x) as f:        
        # m = MultipartEncoder(fields={'data': ('file.csv', f, 'json')})
        # headers = {'Content-Type': m.content_type}
        # r = requests.post(API_URL, data=m, headers=headers)
        f = open(x,'r')
        player_data = f.readline()
        # print(player_data)
        # print(player_data)
        name = x[:-5]
        # print(player_data)
        # final = {"name": name, "data": player_data}
        r = requests.post(API_URL, {"name": name, "data": "test : [1,2,3]"})
        
        print(r)
        break