from django.urls import path
from .views import topic_list, create_topic, follow_unfollow_topic, show_topic

urlpatterns = [
    path('topic_list/', topic_list, name='topic_list'),
    path('create/', create_topic, name='create_topic'),
    path('follow_unfollow_topic/<int:topic_id>/', follow_unfollow_topic, name='follow_unfollow_topic'),
    path('show_topic/<int:topic_id>/', show_topic, name='show_topic'),
]
