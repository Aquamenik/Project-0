from django.urls import path
from . import views

urlpatterns = [
    path("", views.say_hello, name="say_hello"),
    path("v1/", views.v1, name="v1"),
]