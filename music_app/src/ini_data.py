from turtle import clear
from requests.sessions import session
import requests
import json
import pprint
from utils import Spotify

sp = Spotify()
user_list = sp.load_users()
#print('------USUARIOS-------')
#print(json.dumps(user_list, indent=4))
users_playlists = sp.load_user_playlists(user_list)






        





 

















