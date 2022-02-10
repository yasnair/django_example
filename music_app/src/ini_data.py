from requests.sessions import session
import requests
import json
import pprint
from initial_db_data import Spotify
from django.conf import settings
import os

'''
request = requests.get('http://127.0.0.1:8000/api/users/').json()
print('-----USERS------')
print(json.dumps(request, indent=4))


request = requests.get('http://127.0.0.1:8000/api/playlist/').json()
print('-----PLAYLISTS------')
print(json.dumps(request, indent=4))
'''
print('-----CLIENT ID-----')
print(os.environ.get('CLIENT_ID'))












