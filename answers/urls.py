# answers/urls.py
from django.urls import path
from .views import create_answer

urlpatterns = [
    path('create/<int:question_id>/', create_answer, name='create_answer'),
    # Add more URLs as needed
]
