from os import lseek
from django.urls import path
from landing.views import *
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('', views.Index, name='index')
]