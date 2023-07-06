#!/bin/bash

# ZoomEye API key
api_key="your_zoom_eye_api_key"

# ZoomEye search query
query="your_search_query"

# Request data from ZoomEye API
response=$(curl -s -X GET -H "API-KEY: $api_key" "https://api.zoomeye.org/host/search?query=$query")

# Parse IPs and Ports
echo $response | jq -r '.matches[] | "\(.ip):\(.portinfo.port)"' > output.txt
