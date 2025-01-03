# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.countdown_timer, name="countdown_timer"),
    path("add/", views.add_event, name="add_event"),
]
