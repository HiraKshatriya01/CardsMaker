from . import views
from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import *
from django.conf.urls import include, url
import os

app_name ='users'
urlpatterns = [
    path('splash_screen/', views.SplashScreen, name='splash_screen'),
    path('home/', views.Home, name='home'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
#
