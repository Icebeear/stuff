import requests
import smtplib 

username = "example"
password = "example"

stock_params = {
    "symbol": "TSLA",
    "interval": "60min",
    "function": "TIME_SERIES_INTRADAY",
    "apikey": "example",
}

stock = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
data = stock.json()["Time Series (60min)"]
dates = [key for key in data]

news_params = {
    "from": dates[0][:-9],
    "language": "en",
    "q": "Tesla",
    "apiKey": "example",
}

news = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
news_data = news.json()["articles"]
three_art = news_data[:3]
formated_articles = [f"Headline: {article['title']} \nBrief: {article['content'][:-13]}" for article in three_art]

def news(status):
    for article in formated_articles:
            article = article.encode('ascii', 'ignore').decode('ascii')
            send_mail(subject=f"Tesla {status}", sms=article, adress="example")
    
def send_mail(subject, sms, adress):
    with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(
        from_addr=username, 
        to_addrs=adress, 
        msg=f"Subject:{subject}\n\n{sms}"
        )

a = float(data[dates[16]]["4. close"])
b = float(data[dates[0]]["4. close"]) 
percent = (100*(b - a) / max(a, b))

if percent > 0:
    news("UP")
else:
    news("DOWN")