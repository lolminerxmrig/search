# search
search zoomeye , shodan , censys

zoomeye search 'title:Zimbra Web Client Sign In'  -num 3500  -filter=ip,port >> 1.txt



shodan search 'http.favicon.hash:-305179312'  --fields ip_str,port --limit 500 --separator ":" | sed 's/.$//'
shodan search 'http.component:"atlassian confluence"'  --fields ip_str,port --limit 500 --separator ":" | sed 's/.$//'
shodan search 'http.title:"Log In - Confluence" 200'  --fields ip_str,port --limit 500 --separator ":" | sed 's/.$//'
shodan search 'http.component:"atlassian confluence" http.title:"Log In - Confluence" 200'  --fields ip_str,port --limit 500 --separator ":" | sed 's/.$//'
shodan search 'http.component:"atlassian confluence"'  --fields ip_str,port --limit 500 --separator ":" | sed 's/.$//'
shodan search 'http.favicon.hash:-305179312 200'  --fields ip_str,port --limit 500 --separator ":" | sed 's/.$//'
shodan  search "http.favicon.hash:-1250474341" --fields=ip_str,port --separator ":" --limit 1000 | grep ''
shodan  search 'title:"Workspace ONE Access"' --fields=ip_str,port --separator ":" --limit 1000 | grep ''


zoomeye search 'iconhash:-1250474341'  -num 780  -filter=ip,port
zoomeye search 'iconhash:-305179312' -num 800 -filter=ip,port
zoomeye search 'app:"atlassian confluence"' -num 800 -filter=ip,port
zoomeye search 'title:"Log In -Confluence"' -num 800 -filter=ip,port



pip install --upgrade censys

