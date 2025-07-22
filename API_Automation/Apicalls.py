import requests


###################### Get Request ###########################

print("GET REQUESTS")

get_head = {
    'Accept':'text/plains'
}

response = requests.get('https://fakerestapi.azurewebsites.net//api/v1/Activities/3', headers=get_head)

# print(response.status_code)
print(response.json())

# assert response.status_code == 201

print(response.url)

print(response.text)

########################## POST REQUEST ##########################

print('POST REQUEST')

post_headers = {

    'Accept' : 'text/plains',
    'Content-Type': 'application/json'
}

post_body = {
  "id": 165,
  "title": "Harry Potter",
  "dueDate": "2025-07-16T07:23:59.660Z",
  "completed": True
}

post_res = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Activities', headers = post_headers, json=post_body)

body_res = post_res.json()

print(body_res)
assert body_res['id'] == 165

###################### PUT REQUEST #######################

print("Before Update")

get_head = {
    'Accept':'text/plains'
}

response = requests.get('https://fakerestapi.azurewebsites.net//api/v1/Activities/3', headers=get_head)

print(response.json())

print('After Update')

putheader = {    
    'Accept' : 'text/plains',
    'Content-Type': 'application/json'
}

putbody = {
  "id": 11,
  "title": "ABC",
  "dueDate": "2025-07-16T09:00:07.939Z",
  "completed": True
}

putresponse = requests.put('https://fakerestapi.azurewebsites.net//api/v1/Activities/3', headers=putheader,json=putbody)

print(putresponse.json())
