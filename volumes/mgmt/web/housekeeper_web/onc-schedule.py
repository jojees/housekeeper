from icalendar import Calendar, Event
from datetime import date, datetime, timedelta
#import calendar

today = date.today()
first_day = today - timedelta(days=2)
#first_day = today.replace(day=1)
#last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1])
#week_ago = today - timedelta(days=7)
last_day = today + timedelta(days=1)

g = open('OpsSchedule.ics','rb')
gcal = Calendar.from_ical(g.read())
onc_events = []
for component in gcal.walk():
    if component.name == "VEVENT":
	if ((component.get('DTSTART').dt).date() >= first_day) and ((component.get('DTEND').dt).date() <= last_day):
            print "---------------------------------"
	    event = {}
	    event['attendee'] = component.get('attendee')
            print component.get('attendee')
	    event['uid'] = component.get('uid')
            print component.get('uid')
	    event['url'] = component.get('url')
            print component.get('url')
	    event['start'] = (component.get('DTSTART').dt).strftime("%Y-%m-%d %H:%M:%S")
	    print (component.get('DTSTART').dt).strftime("%Y-%m-%d %H:%M:%S")
	    event['end'] = (component.get('DTEND').dt).strftime("%Y-%m-%d %H:%M:%S")
	    print (component.get('DTEND').dt).strftime("%Y-%m-%d %H:%M:%S")
	    event['summary'] = component.get('summary')
            print component.get('summary')
	    onc_events.append(event)
g.close()
print onc_events

#VEVENT({u'ATTENDEE': vCalAddress('joji@jojees.net'), u'UID': vText('Q26EHQ5LK9LFV5'), u'URL': u'https://jojees.pagerduty.com/schedules#PTU8LH4', u'DTEND': <icalendar.prop.vDDDTypes object at 0x7f2d4f3e6ed0>, u'DTSTART': <icalendar.prop.vDDDTypes object at 0x7f2d4f3e6f90>, u'SUMMARY': vText('On Call - Joji Vithayathil Johny - OpsSchedule')})


