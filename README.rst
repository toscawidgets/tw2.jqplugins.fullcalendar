tw2.jqplugins.fullcalendar
=============================

:Author:  Robert Sudwarts <robert.sudwarts at gmail.com >

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _jQuery FullCalendar Plugin: http://arshaw.com/fullcalendar/
.. _jQuery FullCalendar Documentation: http://arshaw.com/fullcalendar/docs/

A toscawidgets2 wrapper for the FullCalendar jquery plugin library.

See the FullCalendar library's documentation for further information:
`jQuery FullCalendar Documentation`_ 

For demos of other tw2.jqplugin widgets see: http://tw2-demos.threebean.org/

Description
-------------

`toscawidgets2 (tw2)`_ aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

`jQuery FullCalendar Plugin`_ is a jQuery plugin that provides a full-sized, 
drag & drop calendar. It uses AJAX to fetch events on-the-fly for each month 
and is easily configured to use your own feed format (an extension is provided 
for Google Calendar). It is visually customizable and exposes hooks for 
user-triggered events (like clicking or dragging an event). The FullCalendar
library is open source and dual licensed under the MIT or GPL Version 2 licenses.

This module, tw2.jqplugins.fullcalendar, provides `toscawidgets2 (tw2)`_ access 
to the `jQuery FullCalendar Plugin`_ widget.

Sampling tw2.jqplugins.fullcalendar in the WidgetBrowser
-----------------------------------------------------------

The best way to scope out ``tw2.jqplugins.fullcalendar`` is to load its widgets 
in the ``tw2.devtools`` WidgetBrowser.  To see the source code that configures 
them, check out 
``tw2.jqplugins.fullcalendar/tw2/jqplugins/fullcalendar/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git@github.com:toscawidgets/tw2.jqplugins.fullcalendar.git
    $ cd tw2.jqplugins.fullcalendar
    $ mkvirtualenv tw2.jqplugins.fullcalendar
    (tw2.jqplugins.fullcalendar) $ pip install tw2.devtools
    (tw2.jqplugins.fullcalendar) $ python setup.py develop
    (tw2.jqplugins.fullcalendar) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.
