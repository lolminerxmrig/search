import requests
import json

# fofa api url
url = "https://fofa.so/api/v1/search/all?email={email}&key={key}&qbase64={query}"

# replace the variables with your own
email = "your_fofa_email"
key = "your_fofa_key"
query = "your_query" # replace with your encoded query

# send get request to fofa api
response = requests.get(url.format(email=email, key=key, query=query))

# convert the response to json
data = json.loads(response.text)

# open the file in write mode
with open("output.txt", "w") as file:
    # loop over the data
    for result in data["results"]:
        # write ip and port to file
        file.write(f"{result['ip']}: {result['port']}\n")
