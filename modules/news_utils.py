import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

api_key = os.getenv('NEWS_API_KEY')

api_key = os.getenv('NEWS_API_KEY')

def get_news():
    print("| Country        | Code |")
    print("| -------------- | ---- |")
    print("| United States  |  us  |")
    print("| India          |  in  |")
    print("| United Kingdom |  gb  |")
    print("| Canada         |  ca  |")
    print("| Australia      |  au  |")
    print("| Saudi Arabia   |  sa  |")
    print("***ONLY AVAILABLE FOR US NOW")

    country = input("Enter the country:(country codes like us,in): ").lower()
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"


    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles",[])

        if not articles:
            print("No news articles found for",country)
            return
        
        print("***Top 5 News Headlines***\n")
        for i,article in enumerate(articles[:5],start = 1):
            print(f"{i}. {article['title']}")
    
    else:
        print(f"Error fetching news: {response.status_code}")