from django.urls import path

from . import google_api
from . import user

urlpatterns = [
    path('google/translate', google_api.translate, name='api_translate'),
    path('user', user.addUser, name="add_user"),
    path('user/<str:username>', user.deleteUser, name="delete_user" )
]