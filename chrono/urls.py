from django.urls import path
from chrono import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
]
