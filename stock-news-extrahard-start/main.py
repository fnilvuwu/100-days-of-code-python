import requests
from twilio.rest import Client
ALPHAVANTAGE_KEY = ALPHAVANTAGE_KEY
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(
    "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=3ZME9TK2FX3Q9Z2S")
stock_data = stock_response.json()

current_date = stock_data["Meta Data"]["3. Last Refreshed"]
yesterday_date = stock_data["Meta Data"]["3. Last Refreshed"][:8] + \
    str(int(stock_data["Meta Data"]["3. Last Refreshed"][8:]) - 1)

# current_price = float(stock_data["Time Series (Daily)"][current_date]["4. close"])
# yesterday_price = float(stock_data["Time Series (Daily)"][yesterday_date]["4. close"])

current_price = 50
yesterday_price = 100
percent_change = round(100 - (current_price/yesterday_price * 100))

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
NEWSAPI_KEY = NEWSAPI_KEY
news_response = requests.get(
    "https://newsapi.org/v2/everything?q=Tesla&from=2022-03-31&sortBy=popularity&apiKey=8626633ca89b465d91236e289dcb9e3b")
news_data = news_response.json()
account_sid = account_sid
auth_token = auth_token

client = Client(account_sid, auth_token)
if percent_change > 5:
    for i in range(3):
        message_title = f"TSLA:🔺{percent_change}%"
        news_title = f"""Headline: {news_data["articles"][i]["title"]} (TSLA)?."""
        news_desc = f"""Brief: {news_data["articles"][i]["description"]}\n"""
        message = client.messages.create(
            messaging_service_sid=messaging_service_sid,
            body=f"""{message_title}\n{news_title}\n{news_desc}""",
            from_=from_phone_number,
            to=to_phone_number
        )

        print(message.sid)

elif percent_change < -5:
    for i in range(3):
        message_title = f"TSLA:🔻{percent_change}%"
        news_title = f"""Headline: {news_data["articles"][i]["title"]} (TSLA)?."""
        news_desc = f"""Brief: {news_data["articles"][i]["description"]}\n"""

        message = client.messages.create(
            messaging_service_sid=messaging_service_sid,
            body=f"""{message_title}\n{news_title}\n{news_desc}""",
            from_=from_phone_number,
            to=to_phone_number
        )

        print(message.sid)

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
