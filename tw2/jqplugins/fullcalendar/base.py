import tw2.core as twc

fullcalendar_js = twc.JSLink(
        modname = 'tw2.jqplugins.fullcalendar',
        filename = 'static/js/fullcalendar.min.js'
        )

gcal_js = twc.JSLink(
        modname = 'tw2.jqplugins.fullcalendar',
        filename = 'static/js/gcal.js'
        )

fullcalendar_css = twc.CSSLink(
        modname = 'tw2.jqplugins.fullcalendar',
        filename ='static/css/fullcalendar.css'
        )

fullcalendar_print_css = twc.CSSLink(
        modname = 'tw2.jqplugins.fullcalendar',
        filename ='static/css/fullcalendar.print.css',
        media="print"
        )
