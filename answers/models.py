# answers/models.py
from django.db import models
from users.models import CustomUser  # Import the User model
from questions.models import Question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Add this line
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s answer: {self.content}"

