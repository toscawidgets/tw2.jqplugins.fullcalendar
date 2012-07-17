import tw2.core as twc

import tw2.jquery
import tw2.jqplugins.ui.base as tw2_jq_ui

from tw2.jqplugins.fullcalendar import base
from tw2.core.resources import encoder

from datetime import date, datetime

__all__ = ['FullCalendarWidget']

class FullCalendarWidget(tw2_jq_ui.JQueryUIWidget):
    """
    See the FullCalendar library's documentation for fuller information:
    http://arshaw.com/fullcalendar/docs/

    List of options passed to ``options`` parameter:

        events -- calendar events **[not to be confused with widget events!]**

        header -- (default: False) or dict()

        theme -- Boolean (default: False) Enables/disables use of jQuery UI
            theming

        firstDay -- Integer (default=0) Date on which week begins.
            Defaults to Sunday.

        isRTL -- Boolean (default: False) to display in right to left mode

        weekends -- Boolean (default: True) Whether to include Saturday/Sunday
            columns in any of the calendar views.

        weekMode -- String (default: 'fixed') Available options: 'fixed',
            'liquid' or 'variable'

        height -- Integer.  Sets entire calendar (inc. header) pixel height.
            By default, this option is unset and the calendar's height
            is calculated by ``aspectRatio``

        contentHeight -- Integer.  Sets calendar content to pixel height.
            By default, this option is unset and the calendar's height is
            calculated by ``aspectRatio``

        aspectRatio -- Float (default: 1.35)  Determines the width-to-height
            aspect ratio of the calendar

        editable -- Boolean (default: False)
    """
    resources = [
            tw2.jquery.jquery_js,
            tw2_jq_ui.jquery_ui_js, tw2_jq_ui.jquery_ui_css,
            base.fullcalendar_js, base.gcal_js,
            base.fullcalendar_css, base.fullcalendar_print_css,
        ]

    template = "mako:tw2.jqplugins.fullcalendar.templates.fullcalendar"
    jqmethod = "fullCalendar"

    def prepare(self):
        '''
        prepare() is required here to convert start/end dates [if passed
        as python `date` or `datetime` objects] using .isoformat() to enable
        encoding
        '''
        
        if 'events' in self.options:
            for evt in self.options['events']:
                if 'start' in evt and isinstance(evt['start'], (date, datetime)):
                    evt['start'] = evt['start'].isoformat()
                if 'end' in evt and isinstance(evt['end'], (date, datetime)):
                    evt['end'] = evt['end'].isoformat()

        super(FullCalendarWidget, self).prepare()


