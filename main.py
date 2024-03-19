import requests
import send_email
import os
from dotenv import load_dotenv

# Load environment variables into the file
load_dotenv()

# Call the api
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

    # check for null values
    if (article["title"] or article["description"]) is not None:
        # concatenate the title and description into one data variable
        articles = str(article["title"]) + " : \n " + str(article["description"]) + " \n " + article["url"]
        article_data += articles + " \n \n"

# call the send email function
send_email.send_email(str(article_data))

