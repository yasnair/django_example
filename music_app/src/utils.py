from http.client import OK
from re import I, S
from requests.sessions import session
import requests
import os, json

#Urls constants
AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

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

    
    def get_users_info(self, userlist = []):
        #Get user profile from spotify
        user_list = []
        for user_id in userlist:
            request = requests.get(BASE_URL + 'users/'+ user_id,
                                   headers=self.headers).json()
            user_list.append(request)  
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

    
    def load_users(self):
        users_list = self.get_users_from_playlist()
        user_info_data = []
        user_url_path = 'http://127.0.0.1:8000/api/users/'
        users_list.append('meyas5')
        users_list.append('smedjan')
        users = self.get_users_info(users_list)
        user_list_out = []
        for user in users:
            user_info_data.append(
                {
                    'id'           : user['id'],
                    'display_name' : user['display_name']

                }
                )
            '''
            response = requests.post(user_url_path, data=data).status_code
            
            if response == '201' or response == '400':
                user_list_out.append(user['id'])      
            else:
                user_list_out.append(user['id'])
            '''
            user_list_out.append(user['id'])
        return user_list_out

    def load_user_playlists(self, user_list=[]):
        playlist_url_path = 'http://127.0.0.1:8000/api/playlist/'
        for user in user_list:
            
            user_playlists = self.get_user_playlists(user)
            print('-------USER----------')
            print(user)
            for playlist in user_playlists :
                print(playlist)
                #response = requests.post(playlist_url_path, data=playlist)
                #if response == '201': #Succesful
                    #Here should associate playlist-user
            






