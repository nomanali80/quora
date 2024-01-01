# topics/models.py

from django.db import models
from users.models import CustomUser

class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    topic_picture = models.ImageField(upload_to='topic_pics/', blank=True, null=True)
    followed_by = models.ManyToManyField(CustomUser, related_name='followings', blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

