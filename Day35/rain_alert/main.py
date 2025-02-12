import requests
import json
import smtplib

LATITUDE = "50.969975"
LONGITUDE = "12.733107"
RAIN_CODE_MAX = 700

#-------------------------- READ API CALL -------------------
def get_forecast(api_key, latitude, longitude):
    '''query for current forecast'''
    
    parameters = {
        "lat": latitude,
        "lon": longitude,
        "appid":api_key,
        "cnt": 4
    }

    try:
        response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
        response.raise_for_status()
    except:
        print("Getting current forecast failed")
        return None
        
    data = response.json()

    return data
    
#----------------------- SEND EMAIL CLIENT ----------------
def send_email(config):
    sender = config["email"]["sender_email"]
    recipient = config["email"]["recipient_email"]
    sender_smtp = config["email"]["sender_smtp"]
    sender_password = config["email"]["sender_password"]

    with smtplib.SMTP(host=sender_smtp, port=587) as connection:
        connection.starttls()

        connection.login(user=sender, password=sender_password)
        connection.sendmail(from_addr=sender, 
                            to_addrs=recipient, 
                            msg="Subject:It will rain\n\nMake sure to use an umbrella"
                        )

#--------------------------- SET CONFIG ---------------------
def get_config():
    try:
        with open("../../.env.json", "r") as file:
            data = json.load(file)    
    except FileNotFoundError:
        print("config file not . Aborting")
        exit()
    except json.JSONDecodeError:
        print("could not parse json data. Aborting")
        exit()
        
    return data


config = get_config()

forecast = get_forecast(config["openweather_api"]["api_key"], LATITUDE, LONGITUDE)
for interval in forecast["list"]:
    weather = interval["weather"][0]
    if(weather["id"] < RAIN_CODE_MAX):
        send_email(config)
        break
        
        