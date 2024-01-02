from django.urls import path
from .views import topic_list, create_topic, follow_unfollow_topic  # assuming your view is named 'index'

urlpatterns = [
    path('topic_list/', topic_list, name='topic_list'),
    path('create/', create_topic, name='create_topic'),
    path('follow_unfollow_topic/<int:topic_id>/', follow_unfollow_topic, name='follow_unfollow_topic'),
    # Add other patterns for topic details, create, etc.
]
