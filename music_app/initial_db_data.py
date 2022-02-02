from requests.sessions import session
import requests
import os
import sys

#Class to access Spotify API
class Spotify():
    def __init__ (self, user_id):
        self.token      = None
        self.expires_in = None
        self.user_id  = user_id
        self.limit = 50
        self.offset = 0
        self.get_token()
        self.headers = {'Authorization': 'Bearer {token}'}


    #Obtiene Token de autorizacion   
    def get_token(self):
        # Get token from Spotify - POST
        auth_response = requests.post(os.environ.get('AUTH_URL'), {
            'grant_type': 'client_credentials',
            'client_id': os.environ.get('CLIENT_ID'),
            'client_secret': os.environ.get('CLIENT_SECRET'),
         }).json()

        self.token       = auth_response['access_token']
        self.expires_in  = auth_response['expires_in']
        self.headers['Authorization'] = 'Bearer {token}'.format(token=self.token)


            # save the access token
            #access_token = auth_response['access_token']
        #return auth_response['access_token']

    def get_user_playlists(self):
        
        #Get User's Playlists
        playlist_info = []   #pd.DataFrame(columns=['id','name'])

        request = requests.get(BASE_URL + 'users/'+ self.user_id + '/playlists',
                                    headers=headers,
                                    params={'limit': self.limit, 'offset': self.offset})
        user_playlist = request.json()['items']

        for playlist in user_playlist:
            #playlist_info  = playlist_info.append({'id': playlist['id'], 'name': playlist['name']})
            playlist_info.append({'id': playlist['id'], 'name': playlist['name']})
        return json.dumps(playlist_info, indent=4)    

    def is_token_valid(self):
        #Falta implementar
        return True

    def get_playlist_items(self, playlist_info):
        playlist_items_info = [] #pd.DataFrame(columns=['track_id','playlist_id','album_id','name'])
        
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
