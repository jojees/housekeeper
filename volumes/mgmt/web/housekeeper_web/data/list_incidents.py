import requests, json

# Update to match your API key
API_KEY = 'iqKb9TBxJWekjzaKJGKM'

# Update to match your chosen parameters
SINCE = '2017-05-07 05:00:00+00:00'
UNTIL = '2017-05-07 07:00:00+00:00'
DATE_RANGE = ''
STATUSES = []
INCIDENT_KEY = ''
SERVICE_IDS = []
#TEAM_IDS = ['PXAD757']
TEAM_IDS = []
USER_IDS = []
URGENCIES = []
TIME_ZONE = 'UTC'
SORT_BY = []
INCLUDE = []


def list_incidents():
    url = 'https://api.pagerduty.com/incidents'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'since': SINCE,
        'until': UNTIL,
        'date_range': DATE_RANGE,
        'statuses[]': STATUSES,
        'incident_key': INCIDENT_KEY,
        'service_ids[]': SERVICE_IDS,
        'team_ids[]': TEAM_IDS,
        'user_ids[]': USER_IDS,
        'urgencies[]': URGENCIES,
        'time_zone': TIME_ZONE,
        'sort_by[]': SORT_BY,
        'include[]': INCLUDE
    }
    r = requests.get(url, headers=headers, params=payload)
    print 'Status Code: {code}'.format(code=r.status_code)
    incidents = r.json()
    print json.dumps(incidents)

if __name__ == '__main__':
    list_incidents()