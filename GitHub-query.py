import requests
import json

# Variables
access_token='YOUR_GITHUB_TOKEN'
headers = {'Authorization':"Token "+access_token}
search_term = 'YOUR_SEARCH_TERM'

# GitHub API request
response = requests.get('https://api.github.com/search/repositories?q='+search_term, headers=headers)

# Parse response to JSON
json_response = json.loads(response.text)

# Save URLs to a file
with open('github_links.txt', 'w') as file:
    for item in json_response['items']:
        file.write(item['html_url'] + '\n')
