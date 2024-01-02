# answers/models.py
from django.db import models
from users.models import CustomUser  # Import the User model
from questions.models import Question
from django.db.models import Count

class AnswerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(num_likes=Count('liked_by')).order_by('-num_likes')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Add this line
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(CustomUser, related_name='liked_answers', blank=True)
    disliked_by = models.ManyToManyField(CustomUser, related_name='disliked_answers', blank=True)

    objects = AnswerManager()

    def __str__(self):
        return f"{self.user.username}'s answer: {self.content}"
