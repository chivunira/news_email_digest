import requests
import send_email
import os
from dotenv import load_dotenv

load_dotenv()
apiKey = os.getenv("apiKey")

url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-02-19&"
       "sortBy=publishedAt&"
       f"apiKey={apiKey}")

# make get request
request = requests.get(url)

# get the json data from the response
content = request.json()

article_data = ""

# get article titles and descriptions
for article in content["articles"]:

    # check for null values and pass a string in their place
    title = article["title"] if article["title"] is not None else " "
    description = article["description"] if article["description"] is not None else " "

    # concatenate the title and description into one data variable
    articles = str(title) + " : \n " + str(description) + " \n " + article["url"]
    article_data += articles + " \n \n"

# call the send email function
send_email.send_email(str(article_data))

