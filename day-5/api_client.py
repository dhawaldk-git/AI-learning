import requests
import logging
import json
# response = requests.get("https://jsonplaceholder.typicode.com/users")
# print(response.status_code)
# print(type(response))
# data = response.json()
# for res in data:
#     # print('res',res['name'])
#     if res['id'] == 1:
#         print('res',res['name'])

logging.basicConfig(filename="app.log",level=logging.INFO)

def get_users():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")

        # response.raise_for_status()
        # print(response.json())
        data = response.json()
        with open('users.json','w') as file:
            json.dump(data,file,indent=4)
        logging.info("Users retrieved successfully")
    except requests.exceptions.RequestException as e:
        logging.error('API ERROR',e)

users = get_users()

# print(users)