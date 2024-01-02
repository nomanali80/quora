# answers/urls.py
from django.urls import path
from .views import create_answer, like_dislike_answer

urlpatterns = [
    path('create/<int:question_id>/', create_answer, name='create_answer'),
    path('like_dislike_answer/<int:answer_id>/', like_dislike_answer, name='like_dislike_answer'),
    # Add more URLs as needed
]
