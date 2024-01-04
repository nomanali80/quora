# topics/models.py

from django.db import models
from users.models import CustomUser
from django.db.models import Count

class TopicManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(follower_count=Count('followed_by')).order_by('-follower_count')

class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    topic_picture = models.ImageField(upload_to='topic_pics/', blank=True, null=True)
    followed_by = models.ManyToManyField(CustomUser, related_name='followings', blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    objects = TopicManager()

    def __str__(self):
        return self.title

    def get_related_questions(self):
        from questions.models import Question
        return Question.objects.filter(topics=self)

