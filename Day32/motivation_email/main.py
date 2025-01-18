import smtplib, json, random
import datetime as dt

#----------------------------  READ CONFIG FILE ---------------------
try:
    with open("../.config.json", "r") as file:
        data = json.load(file)    
except FileNotFoundError:
    print("config file not . Aborting")
    exit()
except json.JSONDecodeError:
    print("could not parse json data. Aborting")
    exit()
 
#----------------------------  READ QUOTES FILE ---------------------
quotes = []
try:
    with open("quotes.txt", "r") as file:
        for line in file:
            
            quote_and_author  = line.split("\"-")
            quotes.append(quote_and_author)
except FileNotFoundError:
    print("quotes file not . Aborting")
    exit()
      
      
#---------------------------- SELECT QUOTE -----------------
now = dt.datetime.now()
if now.weekday() == 5: # Saturday quote
    
    selected_quote = random.choice(quotes)

    sender = data["sender_email"]
    recipient = data["recipient_email"]
    sender_smtp = data["sender_smtp"]
    sender_password = data["sender_password"]

    with smtplib.SMTP(host=sender_smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=sender, password=sender_password)
        connection.sendmail(from_addr=sender, 
                            to_addrs=recipient, 
                            msg=f"Subject:Motivational Saturday Quote\n\n{selected_quote[0]}\"\n-{selected_quote[1]}"
                        )