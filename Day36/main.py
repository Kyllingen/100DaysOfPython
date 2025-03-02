import json
import requests
import math
import smtplib
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

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

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_price(stock: str, api_key: str):
    '''query for stock prices for given company'''
    
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": api_key
    }
    try:
        response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
        response.raise_for_status()
    except:
        print("Getting current stock prices failed")
        return None
        
    data = response.json()
    
    return data
    
def stock_price_change_percentage(stock_data: json):
    '''checks closing price for yesterday vs day before and reports the overall change in percentage'''
    try:
        prev_day = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
        prev_prev_day = (datetime.now() - timedelta(2)).strftime("%Y-%m-%d")
    
        prev_close = float(stock_data["Time Series (Daily)"][prev_day]["4. close"])
        prev_prev_close = float(stock_data["Time Series (Daily)"][prev_prev_day]["4. close"])
    
        change_percentage = (prev_close - prev_prev_close)*100 / prev_close
    except KeyError:
        print("No results for yesterday found.")
        return 0
        
    return change_percentage

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_company_news(company_name:str, api_key: str):
    '''query for stock prices for given company'''
    
    prev_prev_day = (datetime.now() - timedelta(2)).strftime("%Y-%m-%d")
    
    parameters = {
        "q": company_name + " AND shares",
        "apiKey": api_key,
        "from": prev_prev_day,
        "sortBy": "published",
        "language": "en",
        "pageSize": 3
    }
    
    #try:
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    #except:
    #    print("Getting current company news failed")
    #    return None
        
    data = response.json()
    
    return data

## STEP 3: Use email
# Send a seperate email with the percentage change and each article's title and description to your email
def format_email(stock_change_percentage: float, company_news: dict):
    '''take the news and stock change value and create an email'''
    
    content = STOCK + " "
    arrow = ""
    if stock_change_percentage < 0:
        arrow = "🔻 ".encode("utf-8")
        content +=  str(round(abs(stock_change_percentage),2)) + "%\n"
    else:
        arrow = "🔺 ".encode("utf-8")
        content +=  + str(round(abs(stock_change_percentage),2)) + "%\n"
    
    for article in company_news["articles"]:
        headline = article["title"]
        brief = article["description"]
        content += "Headline: " + headline + "\n" + "Brief: " + brief + "\n\n"
    
    content = arrow + content.encode("utf-8")
    print(content)
    return content
    
def send_email(config: dict, email_content: str):
    ''' sends email with content'''
    sender = config["email"]["sender_email"]
    recipient = config["email"]["recipient_email"]
    sender_smtp = config["email"]["sender_smtp"]
    sender_password = config["email"]["sender_password"]
    
    message = "Subject:Stock Movement for " + COMPANY_NAME + "\n\n" 
    message = message.encode("utf-8")
    message += email_content

    with smtplib.SMTP(host=sender_smtp, port=587) as connection:
        connection.starttls()

        connection.login(user=sender, password=sender_password)
        connection.sendmail(from_addr=sender, 
                            to_addrs=recipient, 
                            msg=message
                        )
    
#Optional: Format the email message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


config = get_config()

stock_price_api_key = config["alphavantage_api"]["api_key"]
news_api_key = config["newsapi_api"]["api_key"]

stock_prices = get_stock_price(STOCK, stock_price_api_key )
stock_change_percentage = stock_price_change_percentage(stock_prices)

if(abs(stock_change_percentage) >= 3):
    company_news = get_company_news(COMPANY_NAME, news_api_key)
    email_content = format_email(stock_change_percentage, company_news)
    send_email(config, email_content)