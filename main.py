import requests
import send_email
import os
from dotenv import load_dotenv
import datetime

# Load environment variables into the file
load_dotenv()

# Call the api
apiKey = os.getenv("apiKey")
topic = "devin"
url = (f"https://newsapi.org/v2/everything?q={topic}&"
       "from=2024-02-19&"
       "sortBy=publishedAt&"
       f"apiKey={apiKey}&"
       "language=en")

# make get request
request = requests.get(url)

# get the json data from the response
content = request.json()

# get current date
current_date = datetime.date.today()
day_name = current_date.strftime("%A")

article_data = f"Subject: {day_name}'s news on {topic} \n\n"

# get the latest 10 articles
for article in content["articles"][2:12]:

    # check for null values
    if (article["title"] or article["description"]) is not None:
        # concatenate the title and description into one data variable
        articles = str(article["title"]) + " : \n " + str(article["description"]) + " \n " + article["url"]
        article_data += articles + " \n \n"

# call the send email function
send_email.send_email(article_data)

