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

app_name ='latter_had'

urlpatterns = [
    path('latterhad_form/', views.LatterhadForm, name='latterhad_form'),
    # path('latterhad_update_form/', views.Latt, name='latterhad_update_form'),
    path('create_latterhad/', views.CreateLatterhadCard, name='CreateLatterHadCard'),
    path('get_wk_pdf/', views.get_wk_pdf, name='get_wk_pdf'),
    path('selected_country/', views.selected_country, name='selected_country'),
    path('selected_state_city/', views.selected_state_city, name='selected_state_city'),
    path('selected_language/', views.selected_language, name='selected_language'),
    path('latterhad_home/', views.latterhad_home, name='latterhad_home'),
    path('add_language_label/', views.CreateLanguageLabel, name='add_language_label'),
    path('word_docs/', views.word_docs, name='word_docs'),
    path('retrofit_example/', views.RetrofitExample, name='retrofit_example'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

