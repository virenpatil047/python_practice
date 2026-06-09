import requests, requests_cache, os, json, random
from twilio.rest import Client

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")

requests_cache.install_cache("cache", expire_after=600)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

def send_sms(percentage, title, desc):
    client = Client(account_sid, auth_token)
    # msg = f"TSLA down {abs(round(percentage))}%"
    msg =   f"TSLA: {'up' if percentage > 0 else 'down'}{abs(round(percentage))}%\nHeadline: {title}\nBrief: {desc}"
    
    print(repr(msg))
    
    message = client.messages.create(
        body=msg,
        from_="+13613044933",
        to="+91XXXXXXXXXX",
    )
    
    print(message.status)

alpha_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "outputsize" : "compact",
    "apikey" : os.getenv("ALPHA_KEY")
}

try:
    
    url = 'https://www.alphavantage.co/query'
    alpha_r = requests.get(url, params=alpha_params)
    # print(alpha_r.url)
    alpha_r.raise_for_status()
    alpha_data = alpha_r.json()
except requests.exceptions.RequestException as e:
    print(f"Error : {e}")


# print(data)
# print("cache" if getattr(alpha_r, "from_cache", False) else "server")
time_series = dict(list(alpha_data["Time Series (Daily)"].items())[:2]) # dict slicing
ytd, df_ytd = time_series.keys() # Unpacking 
percentage_diff = (float(time_series[ytd]["4. close"]) - float(time_series[df_ytd]["1. open"])) * 100 / float(time_series[df_ytd]["1. open"])

if abs(percentage_diff) >= 5:
    try:
        news_link = "https://newsapi.org/v2/everything"
        news_params = {
            "q" : COMPANY_NAME,
            "apiKey" : os.getenv("NEWS_KEY"),
            "from" : df_ytd,
            "to" : ytd,
            "sortBy" : "relevancy"
        }
        news_r = requests.get(news_link, params=news_params)
        news_r.raise_for_status()
        news_data = news_r.json()
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")
    
    # articles = news_data["articles"][:3]
    article_td = {a["title"] : a["description"] for a in news_data["articles"][:3]}
    # article_td = {k : v for (k,v) in articles.items()}description
    # print(article_td)
    
    # with open("data.txt", "w") as f:
    #     json.dump(news_data, f, indent=4)
    t = random.choice(list(article_td.keys()))
    send_sms(percentage_diff, t, article_td[t])
