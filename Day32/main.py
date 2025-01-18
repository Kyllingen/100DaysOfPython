import smtplib, json

#---------------------------- READ FILE ---------------------
try:
    with open(".config.json", "r") as file:
        data = json.load(file)    
except FileNotFoundError:
    print("config file not . Aborting")
    exit()
except json.JSONDecodeError:
    print("could not parse json data. Aborting")
    exit()

#---------------------------- SEND MAIL --------------------
sender = data["sender_email"]
recipient = data["recipient_email"]
sender_smtp = data["sender_smtp"]
sender_password = data["sender_password"]

with smtplib.SMTP(host=sender_smtp, port=587) as connection:
    connection.starttls()

    connection.login(user=sender, password=sender_password)
    connection.sendmail(from_addr=sender, 
                        to_addrs=recipient, 
                        msg="Subject:Python Message\n\nThis is the content of the message"
                    )