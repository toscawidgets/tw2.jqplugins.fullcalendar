"""
.. note:
   `start` and `end` dates may be passed to the options parameter as
   python datetime.date or datetime.datetime objects in which case they will
   be converted to ISOFormat.  Equally, date/datetimes may be passed as
   strings eg. "2012-07-17T20:08:21.634121"
"""
import tw2.core as twc

from widgets import *
from datetime import date, datetime, timedelta

now = datetime.now()

calendar_events = [
            {'title': 'the day before yesterday',
             'start': now - timedelta(days=2),
             'allDay': False,
            },
            {'title': 'the day after tomorrow',
             'start': now + timedelta(days=2),
             'allDay': False,
            },
            {'title': 'stretch or drag me!',
             'start': now - timedelta(days=7),
             'allDay': False,
            },
            {'title': "static: using iso formatted strings " \
                      "-- will be lost in the past!",
             'start': "2012-07-02T20:08:21.634121",
             'end': "2012-07-02T21:08:21.634121",
             'allDay': False,
            },
            {'title': 'long event',
             'start': now + timedelta(days=7),
             'end': now + timedelta(days=10),
            },
            {'title': 'all day event',
             'start': now.date(),
             'allDay': True,
            },
        ]

_day_click_js = twc.js_function('function(dt){ alert(dt); }')
_event_click_js = twc.js_function('''
function(calEvt, jsEvent, view)
{
    alert('title: ' + calEvt['title'] + '\\n'
        + 'start: ' + calEvt['start'] + '\\n'
        + 'end: ' + calEvt['end']
        );
}
''')

class BasicCalendarWidget(FullCalendarWidget):
    '''
    see source code for js functions and `calendar_events`
    '''
    attrs = {'style': 'width: 100%;'}
    options={'header': {
                'left': 'prev,next today',
                'center': 'title',
                'right': 'month,agendaWeek,agendaDay'
                },
             'events': calendar_events,
             'editable': True,
             'aspectRatio': 1.60,
             'theme': True,
             'dayClick': _day_click_js,
             'eventClick': _event_click_js,
            }


