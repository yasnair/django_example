from http.client import OK
from re import I, S
from requests.sessions import session
import requests
import os, json

#Urls constants
AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'
USER_URL = 'http://127.0.0.1:8000/api/users/'

#This must be in enviroment variables
CLIENT_ID = "5727d237fa69491eafa4979065ac7649"
CLIENT_SECRET = "4470b556a7464f6d84cb511eba1fb2b3"
REDIRECT_URI = ""

#Custom class
#Class to access Spotify API
class Spotify():
    def __init__ (self):
        self.token      = None
        self.expires_in = None
        self.limit = 50
        self.offset = 0
        self.headers = {'Authorization': 'Bearer {token}'}
        self.get_token()


    #Obtiene Token de autorizacion   
    def get_token(self):
        # Get token from Spotify - POST
        '''
        auth_response = requests.post(AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': os.environ.get('CLIENT_ID'),
            'client_secret': os.environ.get('CLIENT_SECRET'),
         }).json()
         '''
        auth_response = requests.post(AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
         }).json()

        
        self.token       = auth_response['access_token']
        self.expires_in  = auth_response['expires_in']
        self.headers['Authorization'] = 'Bearer {token}'.format(token=self.token)

        #return auth_response 
        
    def load_info_db(self):
        
        #1. Get ID Users from a playlist collaborative to start the flow process
        users_list = self.get_users_from_playlist()
        users_list.append('meyas5')
        users_list.append('smedjan')
        #2. Get user info for db
        users = self.get_users_info(users_list)
        i = 0
        data = {
                    "id": "meyas5",
                    "display_name": "meyas5",
                    "active":"true"
                }
            
        request = requests.post(USER_URL, data)
        print(f'status_code:{request.status_code}')
        print(f'content:{request.content}')
        print(f'text:{request.text}')

        '''
        for user in users:
            data = user
            i = i + 1
            
            playlists = self.get_user_playlists(user['id'])
            if user['id'] == 'meyas5':
                    print(f'-------MEYAS5-------')
                    print(json.dumps(data, indent=4))
                    print(f'-------PLAYLISTS-------')
                    print(json.dumps(playlists , indent=4))
                    print('----------------------------------')
           
            for playlist in playlists:
                #aqui se debe crear la pleyalist en bd
                print('----------------------------------')
                if user['id'] == 'meyas5':
                    print(f'-------User {i}-------')
                    print(json.dumps(data, indent=4))
                    print(f'-------PLAYLISTS-------')
                    print(json.dumps(playlists , indent=4))
                    print('----------------------------------')
        '''


    

    def get_users_info(self, userlist = []):
        
        user_list = []
        for user_id in userlist:
            request = requests.get(BASE_URL + 'users/'+ user_id,
                                   headers=self.headers).json()    
              
            user_list.append(
                    {
                        'id'           : request['id'],
                        'display_name' : request['display_name']

                    }
            )
        return user_list



    def get_users_from_playlist(self):
        playlist_id_in = ['3tRAm0o0uT2EcyTPOBAwkN']
        users_list = []
        for playlist_id in playlist_id_in: 
            request = requests.get(BASE_URL + 'playlists/'+ playlist_id + '/tracks',
                                   headers=self.headers,
                                   params={'fields':'items(added_by.id)','limit': self.limit, 'offset': self.offset})
            list_users = request.json()['items']
            for item in list_users:
                if item['added_by']['id'] not in users_list:
                    users_list.append(item['added_by']['id'])
                
        return users_list
                
    def get_user_playlists(self, user_id):
        
        #Get User's Playlists
        playlist_info = []   

        request = requests.get(BASE_URL + 'users/'+ user_id + '/playlists',
                                    headers=self.headers,
                                    params={'limit': self.limit, 'offset': self.offset})
        user_playlist = request.json()['items']

        for playlist in user_playlist:
            #playlist_info  = playlist_info.append({'id': playlist['id'], 'name': playlist['name']})
            playlist_info.append(
                {'id'           : playlist['id'], 
                 'name'         : playlist['name'], 
                 'collaborative': playlist['collaborative'],
                 'public'       : playlist['public'],
                 'description'  : playlist['description']
                }
                )
        return playlist_info 

    def is_token_valid(self):
        #Falta implementar
        return True

    def get_playlist_items(self, playlist_info):
        playlist_items_info = []
        
        for index, row in playlist_info.iterrows():
            request = requests.get(BASE_URL + 'playlists/'+ row['id'] + '/tracks',
                                        headers=headers,
                                        params={'fields': 'items(track(name,href,album(name,href)))','offset': self.offset, 'limit': self.limit })
            tracks = request.json()['items']
            for track in tracks:
                track_url = track['track']['href']
                album_url = track['track']['album']['href']
                playlist_items_info = playlist_items_info.append({'track_id': track_url.split('tracks/')[1] , 
                                                                  'playlist_id': row['id'],
                                                                  'album_id': album_url.split('albums/')[1],
                                                                  'name': track['track']['name']}, ignore_index=True)

        return playlist_items_info

    
    
    

    def load_user_playlists(self, user_list=[]):
        for user in user_list:
            
            user_playlists = self.get_user_playlists(user)
            print('-------USER----------')
            print(user)

            for playlist in user_playlists :
                print(playlist)
                #response = requests.post(playlist_url_path, data=playlist)
                #if response == '201': #Succesful
                    #Here should associate playlist-user
            






