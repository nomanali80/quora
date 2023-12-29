# topics/models.py

from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    topic_picture = models.ImageField(upload_to='topic_pics/', blank=True, null=True)

    def __str__(self):
        return self.title

