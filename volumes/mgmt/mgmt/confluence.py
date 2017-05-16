from datetime import datetime
import json
import requests
import base64

def parse_time(s):
    ''' Parse 12-hours format '''
    return datetime.strptime(s, '%I:%M %p')

pgstarttime = parse_time('08:00 PM')
pgendtime   = parse_time('08:00 AM')

if datetime.now() > pgstarttime and datetime.now() < pgendtime:
    print 'on-call going on'
    timezone = 'India'
    timezone_short = 'IN'
else:
    print 'on-call us'
    timezone = 'United States'
    timezone_short = 'US'

def on_call_person():
    if timezone == 'United States':
        return 'Brad'
    else:
        return 'Joji'
confluence_title = "%s On-Call Notes %s"
PageTitle =  confluence_title % (timezone_short, datetime.now().strftime("%Y-%m-%d %H-%M-%S"))                                                                                   
template = """
<p>
<strong>Title:</strong> %s
<br/><br/>
<strong>Date:</strong> %s
<br/><br/>
<strong>On-Call Geo:</strong> %s
<br/><br/>
<strong>On-Call Person:</strong> %s
</p>
"""
                                                                                  
content = template % (PageTitle, datetime.today().strftime("%d %B %Y"), timezone, on_call_person())

filename = 'sample.html'
f = open(filename,'w')
f.write(content)
f.close()

with open('sample.html', 'r') as content_file:
    dump_content = content_file.read()
    
def confluence_login():
    username = 'confluence_username'
    password = 'confluence_password'
    auth = requests.auth.HTTPBasicAuth(username, password)
    return (username, password)

pageid = 65538
BASE_URL = "https://jojees.atlassian.net/wiki/rest/api/content/"

data = {
    "type":"page",
    "title": PageTitle, 
    "ancestors": [{"id":pageid}], 
    "space":{"key":"SRE"},
    "body": {
        "storage": {
            "value":content,
            "representation":"storage"
                }   
            }
    }

data = json.dumps(data)

r = requests.post(
        BASE_URL,
        data = data,
        auth = confluence_login(),
        headers = { 'Content-Type' : 'application/json'}
    )
r.raise_for_status()
print r.status_code
print r.headers['content-type']
print r.encoding
print r.json()