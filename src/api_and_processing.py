import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv('EMAIL_ADDRESS')

id="A5032583158"

url_writer = f"https://api.openalex.org/authors/{id}"
payload = {"mailto":email}

# Get data from OpenAlex ID
response = requests.get(url=url_writer,params=payload)
if response.status_code == 200:
    data = response.json()

# Extract name of writer
print(data['display_name'])

url_works = "https://api.openalex.org/works"
payload = {"filter": f"author.id:{id}","mailto": email}

# Get all works from writer
response = requests.get(url=url_works,params=payload)
if response.status_code == 200:
    data = response.json()

# Extract first 20 works ids from writer
works = []
for work in data["results"]:
    works.append(work['id'][21:])
    if len(works) == 20:
        break

print(works)






