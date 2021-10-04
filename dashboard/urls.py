#!/usr/bin/env python
"""
Adds the views from the dashboard app to the list of URLS that the project generates
"""
from django.urls import path
from . import views

#    path('', views.dashboard_with_pivot, name = 'dashboard_with_pivot'),
#    path('data', views.pivot_data, name = 'pivot_data'),
urlpatterns = [
    path("", views.homepage, name = "homepage")
    ]
