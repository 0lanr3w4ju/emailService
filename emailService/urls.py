from importlib.resources import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.send_mail_view)
]