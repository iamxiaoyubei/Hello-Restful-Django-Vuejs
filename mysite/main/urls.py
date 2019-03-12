from django.urls import path

from . import google_api

urlpatterns = [
    path('google/translate', google_api.translate, name='api_translate'),
]