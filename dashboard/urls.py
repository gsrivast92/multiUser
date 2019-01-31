"""Dashboard URL Configuration
"""
from django.contrib import admin
from django.urls import path,re_path,include
from dashboard.views import *


urlpatterns = [
    re_path('^dashboard', TemplateView.as_view(template_name='dashboard.html'),name='dashboard'),
]
