from flask import Flask, render_template
from icalendar import Calendar, Event
from datetime import date, datetime, timedelta
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html',
                          title = 'SHN OPS')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/sre')
def sre():
    return render_template('sre.html',
                          title = 'Site Reliability Analysis')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html',
                          title = 'Inventory')

@app.route('/tools')
def tools():
    return render_template('tools.html',
                          title = 'Tools')

@app.route('/tools/oc-logs')
def oc_schedule():
    today = date.today()
    first_day = today - timedelta(days=2)
    last_day = today + timedelta(days=1)
    
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    ical_url = os.path.join(SITE_ROOT, "data", "OpsSchedule.ics")
    g = open(ical_url,'rb')
    gcal = Calendar.from_ical(g.read())
    onc_events = []
    for component in gcal.walk():
        if component.name == "VEVENT":
            if ((component.get('DTSTART').dt).date() >= first_day) and ((component.get('DTEND').dt).date() <= last_day):
                event = {}
                event['attendee'] = component.get('attendee')
                event['uid'] = component.get('uid')
                event['url'] = component.get('url')
                event['start'] = component.get('DTSTART').dt
                event['end'] = component.get('DTEND').dt
#                event['start'] = (component.get('DTSTART').dt).strftime("%Y-%m-%d %H:%M:%S")
#                event['end'] = (component.get('DTEND').dt).strftime("%Y-%m-%d %H:%M:%S")
                event['summary'] = component.get('summary')
                onc_events.append(event)
    g.close()   
    
    return render_template('sre_onc.html',
                          title = 'On-Call Logs',
                          entries=onc_events)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
