'''
 Use the NewsAPI and the requests module to fetch the daily news 
 related to different topics. Go to: https://newsapi.org/ and 
 explore the various options to build you application
'''
import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&sortBy=popularity&apiKey=b9f68b2501734c11b42dfed59f9baf80"

r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")