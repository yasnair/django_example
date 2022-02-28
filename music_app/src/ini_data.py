
from utils import Spotify
import json
# Initialise environment variables


sp = Spotify()
#1 Create Users using endpoint
users_list = sp.load_users_db()

#2 Create playlists
user_playlists = sp.load_user_playlists()


#2. Get users Playlists.
#print(json.dumps(users_list , indent=4))


            







        





 

















