import requests
import json


URL ="http://127.0.0.1:8000/studentapi/"

#Get Method Function Here
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url= URL, data = json_data)
    data = r.json()
    print(data)
# get_data(2)



#Post/create Method Function Here
def post_data():
    data = {
        'id' : 1,
        'name' : 'ravi',
        'roll' : 101,
        'city' : 'indore'
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

# post_data()



# for update/patch

