from django.test import TestCase
from .models import User, UsersPlaylists, Playlist


# Create your tests here.
class M2MThroughTest(TestCase):
    def setUp(self):
        # Create three users:
        self.joe = User.objects.create(id='u1', display_name='Joe')
        self.jim = User.objects.create(id='u2', display_name='Jim')
        self.bob = User.objects.create(id='u3', display_name='Bob')
      
        # And three Playlist:
        self.play1 = Playlist.objects.create(id='p1', name='play1', collaborative=True)
        self.play2 = Playlist.objects.create(id='p2', name='play2', collaborative=True)
        self.play3 = Playlist.objects.create(id='p3', name='play3', collaborative=True)
        
        # Every user collaborate in the collaborative playlist, but
        # Joe is the owner.
        UsersPlaylists.objects.create(user=self.joe, playlist=self.play1, user_type=UsersPlaylists.USER_TYPE_OWNER)
        UsersPlaylists.objects.create(user=self.jim, playlist=self.play1, user_type=UsersPlaylists.USER_TYPE_COLLA)
        UsersPlaylists.objects.create(user=self.bob, playlist=self.play1, user_type=UsersPlaylists.USER_TYPE_COLLA)

        UsersPlaylists.objects.create(user=self.joe, playlist=self.play2, user_type=UsersPlaylists.USER_TYPE_COLLA)
        UsersPlaylists.objects.create(user=self.jim, playlist=self.play2, user_type=UsersPlaylists.USER_TYPE_OWNER)
        UsersPlaylists.objects.create(user=self.bob, playlist=self.play2, user_type=UsersPlaylists.USER_TYPE_COLLA)

        UsersPlaylists.objects.create(user=self.joe, playlist=self.play3, user_type=UsersPlaylists.USER_TYPE_COLLA)
        UsersPlaylists.objects.create(user=self.jim, playlist=self.play3, user_type=UsersPlaylists.USER_TYPE_COLLA)
        UsersPlaylists.objects.create(user=self.bob, playlist=self.play3, user_type=UsersPlaylists.USER_TYPE_OWNER)




        
    def test_unfiltered_playlist(self):
        # Which playlist is Jim in?
        jims_playlist = Playlist.objects.filter(users=self.jim, userplaylist__user_type=UsersPlaylists.USER_TYPE_OWNER)
        queryset = Playlist.objects.filter(userplaylist__user_type=UsersPlaylists.USER_TYPE_OWNER)
        print('-----jims_playlist----')
        for o in jims_playlist:
            print(o.name)

        print('-----QUERYSET----')
        print(queryset)
        #self.assertEqual(list(jims_playlist), [self.play1, self.play2, self.play3])
        
'''
    def test_owner_playlist(self):
        # But which playlist does Jim owner?
        jim_owner = Playlist.objects.filter(users=self.jim, userplaylist__user_type=UsersPlaylists.USER_TYPE_OWNER)
        self.assertEqual(list(jim_owner), [self.play3])
    
    def test_users_playlists(self):
        # And which Playlists is Bob just a Collaborate of?
        bob_coll = Playlist.objects.filter(users=self.bob, userplaylist__user_type=UsersPlaylists.USER_TYPE_COLLA)
        self.assertEqual(list(bob_coll), [self.play1, self.play3])
'''


    
    
    


