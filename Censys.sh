#!/bin/bash

# Run the Censys search command and pipe the output to jq
censys_output=$(censys search "services.http.response.html_title: 'WSO2 Management Console'" | jq -c '.[] | {ip: .ip, ports: [.services[].port]}')

# Loop through each line of the output
while read -r line; do
  # Extract the IP address and ports from the line
  ip=$(echo "$line" | jq -r '.ip')
  ports=$(echo "$line" | jq -r '.ports[]')

  # Loop through each port and output the corresponding URL
  while read -r port; do
    if [ "$port" -eq 80 ]; then
      echo "http://$ip:$port"
    elif [ "$port" -eq 443 ]; then
      echo "https://$ip:$port"
    fi
  done <<< "$ports"
done <<< "$censys_output"
