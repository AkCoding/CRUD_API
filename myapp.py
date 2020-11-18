import requests

URL ="http://127.0.0.1:8000/stuinfo/3"

r = requests.get(url = URL)

data = r.json()

print(data)