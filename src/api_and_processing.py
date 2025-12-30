import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv('EMAIL_ADDRESS')

id="A5032583158"

# Get data from OpenAlex ID
url_writer = f"https://api.openalex.org/authors"
payload = {"mailto":email}

response = requests.get(url=f"{url_writer}/{id}",params=payload)
if response.status_code == 200:
    data = response.json()

# Extract name of writer
neightbor_0 = data['display_name']

# Get all works from writer
url_works = "https://api.openalex.org/works"
payload = {"filter": f"author.id:{id}","mailto": email}

response = requests.get(url=url_works,params=payload)
if response.status_code == 200:
    data = response.json()

# Extract all authors ids from the 20 works
count_works = 0
author_count = {}
for work in data["results"]:
    authors = work['authorships']
    for author in authors:
        name = author['author']['id']
        author_count[name] = author_count.get(name, 0) + 1 
    count_works += 1
    if count_works == 20:
        break

author_data = {}
for author in author_count:
    payload = {"mailto":email}

    response = requests.get(url=f"{url_writer}/{author}",params=payload)
    if response.status_code == 200:
        author_data[author] = response.json()
        author_data[author]['connection_count'] = author_count[author]
        print(author_data[author]['display_name'])
    else:
        print(response.status_code)
        break

with open("../data/output.json", "w") as file:
    json.dump(author_data, file, indent=4)










