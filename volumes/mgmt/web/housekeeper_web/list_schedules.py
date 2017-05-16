import requests
import json

# Update to match your API key
API_KEY = 'iqKb9TBxJWekjzaKJGKM'

# Update to match your chosen parameters
QUERY = ''


def list_schedules():
    url = 'https://api.pagerduty.com/schedules'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'query': QUERY
    }
    r = requests.get(url, headers=headers, params=payload)
    print 'Status Code: {code}'.format(code=r.status_code)
    schedules = r.json()
    print json.dumps(schedules['schedules'])

if __name__ == '__main__':
    list_schedules()

