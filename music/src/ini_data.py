from requests.sessions import session
import requests

request = requests.get('http://127.0.0.1:8000/api/users/').json()
print('-----REQUEST------')
print(request)
