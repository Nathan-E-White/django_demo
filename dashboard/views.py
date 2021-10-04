#!/usr/bin/env python
"""
Defines views for the dashboard app. Current version pulls in AAPL stock info and plots candlestick charts.
"""
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from bokeh.plotting import figure
# from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from math import pi
from dashboard.src.utils import get_data, convert_to_df
# import pandas as pd
# import datetime


def dashboard_with_pivot(request):
    """
    TODO:   will render a table to put below the chart plot
    :param request: TODO
    :type request:  TODO
    :return:        TODO
    :rtype:         TODO
    """
    return render(request, "dashboard/dashboard_with_pivot.html", {})


def pivot_data(request, cls):
    """
    TODO:   Will create a table of information to display below plot
    :param request: TODO
    :type request:  TODO
    :param cls:     TODO
    :type cls:      TODO
    :return:        TODO
    :rtype:         TODO
    """
    dataset = cls.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe = False)


# TODO: Add in tables below the chart
# TODO: "Make the chart more interactive."
def homepage(req):
    """
    Renders a chart to display candlesticks to the user
    :param req:     TODO
    :type req:      TODO
    :return:        TODO
    :rtype:         TODO
    """
    # Use the interface we built for the API
    res = get_data("2021-01-04", "2021-01-05")
    src = convert_to_df(res).head(20)
    # src = res.results
    # Need these to get our chart coloring
    incr = src.close > src.open
    decr = src.open > src.close

    # w = 12 * 36000
    width = 60 * 1000
    
    # Bells and whistles to make the chart pop
    c_tools = "pan, wheel_zoom, box_zoom, reset, save"
    c_title = "AAPL chart"

    # Call Bokeh library/define the plot
    p = figure(x_axis_type = "datetime", tools = c_tools, plot_width = 1600, plot_height = 1000, title = c_title)

    # Configure the plot
    p.xaxis.major_label_orientation = pi / 4
    p.grid.grid_line_alpha = 0.3
    p.segment(src.date, src.high, src.date, src.low, color = "black")

    # Set the chart to display increasing candles as green
    # Similarly, set the decreasing bars to red
    # TODO: I don't like this green... get a better shade of green
    p.vbar(src.date[incr], width, src.open[incr], src.close[incr], fill_color = "#D5E1DD", line_color = "black")
    p.vbar(src.date[decr], width, src.open[decr], src.close[decr], fill_color = "#F2583E", line_color = "black")

    # Destructure the Bokeh plot object into <script> and <div> components
    script, div = components(p)

    # Return an actual rendering of the parsed image components
    return render(req, "dashboard/base.html", {"script": script, "div": div})
