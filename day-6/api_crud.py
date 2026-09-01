import requests
import logging

logging.basicConfig(filename="app.log",level=logging.INFO)
###POST request #####
# payload ={
#     "title":"python learning",
#     "body":"Day 6 practice",
#     "userId":11
# }

# response = requests.post(url='https://jsonplaceholder.typicode.com/posts',
#               json=payload)

# print(response.status_code)
# print(response.json())

###PUT request #####
# payload ={
#     "id":1,
#     "title":"Title update",
#     "body":"Content update",
#     "userId":11
# }

# response = requests.put(url='https://jsonplaceholder.typicode.com/posts/1',
#               json=payload)

# print(response.status_code)
# print(response.json())

###DELETE request #####
# response = requests.delete(url='https://jsonplaceholder.typicode.com/posts/1')

# print(response.status_code)
# print(response.json())


#### request with headers ####
# headers = {
#     'content-Type': 'application/json'
# }

# response = requests.get(url='https://jsonplaceholder.typicode.com/users',
#                         headers=headers)
# print(response)

#### request with Authorization headers ####
# headers = {
#     'Authorization': 'Bearer YOUR_TOKEN'
# }

# response = requests.get(url='https://jsonplaceholder.typicode.com/users',
#                         headers=headers)
# print(response)

###### generic get api #########
logging.info('Fetching users')
def get_generic_data(urll):
    try:
        response = requests.get(url=urll)
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.RequestException as e:
        logging.error('API ERROR',e)

user_data = get_generic_data("https://jsonplaceholder.typicode.com/users")

if user_data:
    logging.info('data retrived')
        
