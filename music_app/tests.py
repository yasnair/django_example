from django.test import TestCase
#from initial_db_data import Spotify
from music.src.initial_db_data import Spotify
import os
from requests.sessions import session
import requests


# Create your tests here.
class SpotifyTestCase(TestCase):
    def setUp(self):
        sp = Spotify(os.environ.get("USER_ID"))
        print("TOKEN", sp.token)
        print("HEADER", sp.headers)

    def test_data(self):
        print("TEST")



