# questions/models.py
from django.db import models
from users.models import CustomUser
from topics.models import Topic
from django.db.models import Count

class QuestionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(num_likes=Count('liked_by')).order_by('-num_likes')

class Question(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    topics = models.ManyToManyField(Topic)
    liked_by = models.ManyToManyField(CustomUser, related_name='liked_questions', blank=True)
    disliked_by = models.ManyToManyField(CustomUser, related_name='disliked_questions', blank=True)

    objects = QuestionManager()

    def __str__(self):
        return self.content
