import requests
import datetime as dt
import smtplib
import json
import time

MY_LAT = 46.406 
MY_LONG = 12.7027

def readfile(file: str):
    ''' reads a file and returns content'''
    try:
        with open(file, "r") as json_file:
            content = json.load(json_file) 
    except FileNotFoundError:
        print(f"file {file} not found. Aborting")
        exit(-1)
    except json.JSONDecodeError:
        print("could not parse json data. Aborting")
        exit(-1)
    
    return content

def get_iss_position():
    '''query for curent ISS position'''
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
    except:
        print("Getting ISS position failed")
        return None
        
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data ["iss_position"]["latitude"])
    return (longitude, latitude)

def is_night_time(lat, long):
    '''returns True if its nighttime at current location'''
    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now()
    hour_now = time_now.hour
    
    if hour_now >= sunset and hour_now <= sunrise:
        return True
    
    return False

def iss_here(iss_loc, my_loc):
    ''' verfiy if location is close enough and its nightime'''
    if (iss_loc[0] <= (my_loc[0]+5) or iss_loc[0] >= (my_loc[0]-5)) \
        and (iss_loc[1] <= (my_loc[1]+5) or iss_loc[1] >= (my_loc[1]-5)):
        
        return True
    print(iss_loc, my_loc)
    return False

def send_email(data: dict):
    ''' send email to given receipient'''
    sender = data["sender_email"]
    recipient = data["recipient_email"]
    sender_smtp = data["sender_smtp"]
    sender_password = data["sender_password"]

    with smtplib.SMTP(host=sender_smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=sender_password)
        connection.sendmail(from_addr=sender, 
                            to_addrs=recipient, 
                            msg=f"Subject:Look up\n\nThe ISS Station is over you"
                        )


config = readfile("../../Day32/.config.json")

while True:
    
    iss_position = get_iss_position()
    if iss_position != None:
        
        is_night = is_night_time(MY_LAT, MY_LONG)
        is_iss_here = iss_here(iss_position, (MY_LAT, MY_LONG))
    
        if is_night and is_iss_here:
            print("Sending email")
            send_email(config)
        
        time.sleep(60)


