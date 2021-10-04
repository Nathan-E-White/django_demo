#!/usr/bin/env python
"""
TODO:   This is for the timezone middleware that I'm not using anymore, add it back in or remove it.
"""
import pytz
from django.utils import timezone


class TimezoneMiddleware:
    """
    TODO: Fill in, add back in to project or remove
    """


    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        tzname = request.session.get("django_timezone")
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)
