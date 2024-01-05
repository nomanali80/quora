# topics/forms.py

from django import forms
from .models import Topic

import cloudinary
import cloudinary.uploader

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'topic_picture']

    def save(self, commit=True):
        topic = super().save(commit=False)

        if 'topic_picture' in self.cleaned_data:
            topic_picture = self.cleaned_data['topic_picture']

            # Upload profile picture to Cloudinary
            result = cloudinary.uploader.upload(topic_picture, folder="topic_pics")
            topic.topic_picture = result['secure_url']

        if commit:
            topic.save()
        return topic
