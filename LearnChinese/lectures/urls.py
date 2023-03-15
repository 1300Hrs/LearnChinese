from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.courses_home, name="courses_home"),
    path("reading/", views.reading_lessons, name="reading"),
    path("listening", views.listening_lessons, name="listening"),
]