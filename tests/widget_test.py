from webob import Request
from webob.multidict import NestedMultiDict
from tw2.core.testbase import assert_in_xml, assert_eq_xml, WidgetTest
from nose.tools import raises, eq_
from cStringIO import StringIO
from tw2.core import EmptyField, IntValidator, ValidationError
from cgi import FieldStorage
import formencode

import webob
if hasattr(webob, 'NestedMultiDict'):
    from webob import NestedMultiDict
else:
    from webob.multidict import NestedMultiDict

import tw2.jqplugins.fullcalendar as w

class TestFullCalendarWidget(WidgetTest):
    widget = w.FullCalendarWidget
    attrs = {'id' : 'cal'}
    options = {'editable': True, 'theme': True}
    expected = """
<div id="cal:wrapper">

<div id="cal"> </div>

<script type="text/javascript">
$(document).ready(function() {
    $("#cal").fullCalendar({});
});
</script>

</div>
"""

