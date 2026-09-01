import requests
import logging
import json

logging.basicConfig(filename="app.log",level=logging.INFO)

def get_users():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        print(response.status_code)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        logging.error('API ERROR',e)
        return []

def save_users_to_file():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")

        # response.raise_for_status()
        # print(response.json())
        data = response.json()
        with open('users.json','w') as file:
            json.dump(data,file,indent=4)
        logging.info("Users retrieved successfully")
        return True
    except requests.exceptions.RequestException as e:
        logging.error('API ERROR',e)
        return False


def get_user_by_id(user_id):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")

        # response.raise_for_status()
        # print(response.json())
        data = response.json()
        for user_data in data:
            if user_data['id'] == user_id:
                print('user_data',user_data)  
                logging.info(f"Users retrieved successfully with id {user_id}")
                return True
        logging.warning(f"user data with {user_id} not found")4
        return False
    except requests.exceptions.RequestException as e:
        logging.error('API ERROR',e)

logging.info('Application Started')
while True:
    try:
        print('\n User Dictionary Menu')
        print('1. View Users')
        print('2. Search User By ID')
        print('3. Save Users To File')
        print('4. Exit')
        user_management = int(input('\n Enter value \n')) 
    except ValueError:
            print('Enter value between 1 to 4')
            continue

    if user_management == 1:
        users = get_users()
        if users:
            print(users)
        else:
            print('API error')

    elif user_management == 2:
        try: user_id = int(input('Enter User id \n')) 
        except Exception as e: print(e) 
        users = get_user_by_id(user_id)
        if users:
            print("User found")
        else:
            print("User not found")

    elif user_management == 3:
        save_data = save_users_to_file()
        if save_data:
            print('user saved to file')
        else:
            print('user not saved to file')
    elif user_management == 4:
        print ('Exiting.....')
        logging.info(f"Exit Application")
        break
    else:
        print('Invalid choice please select between 1 to 4')