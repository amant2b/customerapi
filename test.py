import json 
import requests

url =  'http://127.0.0.1:8000/'


data={
    "first_name":'Aman',
    "last_name":"mishra",
    "age":"22",
    "phoneno":"8700745689",
    "email":"iaman.m98@gmail.com"
}

json_data= json.dumps(data)

headers={
    'Content-Type':'application/json'

}

r=requests.get(url=url,headers=headers, data=json_data)

print(r.json())