import requests



## STEP 0: Read in env variables
#--------------------------- SET CONFIG ---------------------
def get_config():
    try:
        with open("../.env.json", "r") as file:
            data = json.load(file)    
    except FileNotFoundError:
        print("config file not found. Aborting")
        exit()
    except json.JSONDecodeError:
        print("could not parse json data. Aborting")
        exit()
        
    return data

def create_user():
    '''creates a new user if it does not already exist'''
    response = requests.post(url=pixela_endpoint, json=user_params)
    if response.isSucess:
        print("User created successfully")
        update_user()

def update_user(data: json):
    '''updates the user data in the config file'''
    data["pixela_api"]["user_exists"] = True
    try:
        with open("../.env.json", "w+") as file:
            file.write(json.dump(data))
    except FileNotFoundError:
        print("config file not found. Aborting")
        exit()
    except json.JSONDecodeError:
        print("could not parse json data. Aborting")
        exit()
    