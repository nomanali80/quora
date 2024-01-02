# questions/models.py
from django.db import models
from users.models import CustomUser
from topics.models import Topic

class Question(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    topics = models.ManyToManyField(Topic)
    liked_by = models.ManyToManyField(CustomUser, related_name='liked_questions', blank=True)
    disliked_by = models.ManyToManyField(CustomUser, related_name='disliked_questions', blank=True)

    def __str__(self):
        return self.content
