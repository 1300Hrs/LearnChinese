from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("chatGPT-integration/", views.translation_bot, name="chatgpt_translation"),
    path("chatGPT/", views.chatGPT_bot, name="chatgpt"),
    path("user_reviews/", views.user_reviews, name='user_reviews'),
    path("about/", views.about, name="about"),
    path("quiz/<int:quiz_id>/", views.quiz, name="quiz"),
]