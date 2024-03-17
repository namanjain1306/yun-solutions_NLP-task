import requests
from bs4 import BeautifulSoup
import tweepy

def scrape_google_news():
    base_url = "https://www.google.com/search?q=Reliance+Industries+Ltd.+news&tbm=nws&tbs=qdr:d"
    headers = {
        "User-Agent": Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/58.0.3029.110 Safari/537.3

    }
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    news_list = []
    news_elements = soup.find_all("div", class_="ZINbbc xpd O9g5cc uUPGi")
    for news_element in news_elements:
        link_element = news_element.find("a")
        if link_element:
            source = news_element.find("span", class_="xQ82C e8fRJf").get_text()
            url = link_element["href"]
            title = link_element.get_text()
            news_list.append({"source": source, "text": title, "url": url})

    return news_list

def scrape_twitter(api_key, api_secret_key, access_token, access_token_secret, query):
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets = api.search(q=query, count=10)
    twitter_text = ''
    for tweet in tweets:
        twitter_text += tweet.text + ' '
    return twitter_text.strip()

def fetch_latest_news():
    news_sources = [
        'https://twitter.com/search?q=Reliance%20Industries%20Ltd&src=typed_query&f=live',
        # Add more news websites URLs as needed
    ]

    api_key = 'your_api_key'
    api_secret_key = 'your_api_secret_key'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'

    news_data = []

    for source in news_sources:
        if 'twitter.com' in source:
            text = scrape_twitter(api_key, api_secret_key, access_token, access_token_secret, 'Reliance Industries Ltd')
        else:
            news = scrape_news(source)
            text = news['text'] if news else ''
        news_data.append({'source': source, 'text': text})

    # Google News scraping
    google_news = scrape_google_news()
    for news in google_news:
        news_data.append({'source': news['source'], 'text': news['text']})

    return news_data

latest_news = fetch_latest_news()
for news in latest_news:
    print(news)
