import requests

apiKey = '07006c479c204bdab838fcf40c2ff26a'
url  = ("https://newsapi.org/v2/everything?q=tesla&from=2024-02-19&"
        "sortBy=publishedAt&"
        f"apiKey={apiKey}")

request = requests.get(url)
content = request.json()

for article in content["articles"]:
        print(article["title"])
        print(article["description"])