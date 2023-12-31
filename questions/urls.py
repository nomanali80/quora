# questions/urls.py
from django.urls import path
from .views import create_question, like_dislike_question, show_question

urlpatterns = [
    path('create/', create_question, name='create_question'),
    path('like_dislike_question/<int:question_id>/', like_dislike_question, name='like_dislike_question'),
    path('show_question/<int:question_id>/', show_question, name='show_question'),
]
