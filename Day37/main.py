import requests
import json


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

def create_user(user_params: json):
    '''creates a new user if it does not already exist'''
    
    pixela_endpoint = "https://pixe.la/v1/users"
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
        
def create_graph(graph_params: json, user_params: json):
    '''creates a new graph if it does not already exist'''
    
    pixela_endpoint = f"https://pixe.la/v1/users/{user_params['username']}/graphs"
    response = requests.post(url=pixela_endpoint, json=graph_params)
    if response.isSucess:
        print("Graph created successfully")
    
## STEP 1: Get pixela API endpoint and user params
config = get_config()
user_params = {
    "token": config["pixela_api"]["token"],
    "username": config["pixela_api"]["username"],
    "agreeTermsOfService": config["pixela_api"]["agreeTermsOfService"],
    "notMinor": config["pixela_api"]["notMinor"]
}

## STEP 2: Check if user exists and create if not
if config["pixela_api"]["user_exists"] == False:
    create_user()
    
## STEP 3: Create a graph
create_graph_params = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai",
    "timezone": "Europe/Oslo"
}

create_graph(create_graph_params, user_params)