import requests
import shodan

requests.packages.urllib3.disable_warnings()

API_KEY = "Y3eCcLAZgj1sIcftPUiIW4zVONuYEfvj"

SEARCH_FOR = 'services.http.response.html_title='WSO2 Management Console''
f = open("urls.txt", "a")
api = shodan.Shodan(API_KEY)
result = api.search(SEARCH_FOR, limit=1000)
for service in result['matches']:
    IP = service['ip_str']
    url = "https://{}".format(IP)
    f.writelines(url+"\n")

print("[+] Found {} results.".format(result['total']))
