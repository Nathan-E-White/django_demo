"""
TODO:   Right now this file isn't doing anything AFAIK, I just put it in here when I was learning about timezones
"""
import pytz
from django.shortcuts import redirect, render


def set_timezone(request):
    """

    :param request:
    :return:
    """
    if request.method == "Post":
        request.session["django_timezone"] = request.POST["timezone"]
        return redirect("/")
    else:
        return render(request, "template.html", {"timezones": pytz.common_timezones})
