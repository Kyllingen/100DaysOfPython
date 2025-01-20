
import random
import pandas
import datetime as dt
import json
import smtplib
import os


def readfile(file: str):
    ''' reads a file and returns content'''
    content = None
    try:
        filetype = os.path.splitext(file)[1]
        print(filetype, file)
        if filetype == 'csv':
            content = pandas.read_csv(file, sep=',' )
        elif filetype == 'txt':
            with open(file, "r") as text_file:
                content = text_file.read()
        elif filetype == "json":
            with open(file, "r") as json_file:
                content = json.load(json_file) 
    except FileNotFoundError:
        print(f"file {file} not found. Aborting")
        exit(-1)
    except json.JSONDecodeError:
        print("could not parse json data. Aborting")
        exit(-1)
    
    return content

def get_birthdays():
    ''' return list of birthdays for today'''
    csv = readfile("birthdays.csv")
    now = dt.datetime.now()
    this_day = now.day
    this_month = now.month

    return csv.loc[(csv["month"] == this_month) & (csv["day"] == this_day)]

def send_email(email:str, letter:str, data: dict):
    ''' send email to given receipient'''
    sender = data["sender_email"]
    recipient = email
    sender_smtp = data["sender_smtp"]
    sender_password = data["sender_password"]

    with smtplib.SMTP(host=sender_smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=sender_password)
        connection.sendmail(from_addr=sender, 
                            to_addrs=recipient, 
                            msg=f"Subject:Happy Birthday\n\n{letter}"
                        )



config = readfile("../.config.json")
birthdays = get_birthdays()

if not birthdays.empty:
    for index, row in birthdays.iterrows():
        name = row["name"]
        email = row["email"]
        letter_num = random.randint(1,3)
        letter = readfile(f"letter_templates/letter_{letter_num}.txt")
        
        #replace letter
        letter = letter.replace("[NAME]", name)

        send_email(email, letter, config)



