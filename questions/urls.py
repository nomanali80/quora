# questions/urls.py
from django.urls import path
from .views import create_question, question_list

urlpatterns = [
    path('create/', create_question, name='create_question'),
    path('list/', question_list, name='question_list'),
    # Add more URLs as needed
]
