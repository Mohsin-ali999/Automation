import requests

url = 'https://gorest.co.in/public/v2/users'

header = {
    'Content-Type': 'application/json',
    'Authorization':'Bearer da064cfdce313a77b36f1398e12dcd265d2e01be94bcdcd403bdfaff7fde4c46'
}

body = {
    "name": "Devaan",
    "email": "cpa_dhawan_deepan321123@ratke.test",
    "gender": "male",
    "status": "active"
}

postreq = requests.post(url, headers=header,json=body)
print(postreq.json())

assert postreq.status_code == 201

getreq = requests.get(url+'/'+str(postreq.json()['id']), headers=header)

print(getreq.json())
