from http.client import OK
from re import I, S
from requests.sessions import session
from constants import AUTH_URL, CLIENT_ID, CLIENT_SECRET, BASE_URL, USER_URL, REDIRECT_URI
import requests
import os, json

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


    #Load info to DB fetching Spotify data
    def load_users_db(self):
        
        #1. Get ID Users from a playlist collaborative to start the flow process
        users = self.get_users_from_playlist()
        users_list = []
        for user in users:
            data = user
            request = requests.post(USER_URL, data) #creating user
            #if request.status_code == '201':
            users_list.append(data)

        return  users_list

           
    #Get user info from Spotify
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


    #Get users from Playlists Id
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

        users_list.append('meyas5')
        users_list.append('smedjan')  

        users = self.get_users_info(users_list)      
        return users

                
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
                 'description'  : playlist['description'],
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

    
    
    #Create playlist to a user in DB
    def load_user_playlists(self, user_list=[]):
        users_playlist = []
        
        for user in user_list:
        
            user_playlists = self.get_user_playlists(user)

            for playlist in user_playlists :
                if user == 'meyas5':
                    print('-----PLAYLISTS-MEYAS5-------')
                    print(playlist)
                #response = requests.post(playlist_url_path, data=playlist)
                #if response == '201': #Succesful
                    #Here should associate playlist-user
        return users_playlist 
         
        
            
            






