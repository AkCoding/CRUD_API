import requests
import json


URL ="http://127.0.0.1:8000/studentapi/"

#Get Method Function Here
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url= URL, headers=headers, data = json_data)
    data = r.json()
    print(data)
# get_data()



#Post/create Method Function Here
def post_data():
    data = {
        'id' : 8,
        'name' : 'karan',
        'roll' : 108,
        'city' : 'indore'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

# post_data()



# for update/put
def update_data():
    data = {
        'id' : 8,
        'name' : 'shit',
        'city' : 'sanchi'
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# update_data()

# for Delete Method
def delete_data():
    data = {'id' : 3}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

delete_data()

