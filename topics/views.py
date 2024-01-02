#from django.shortcuts import render
from .models import Topic
from django.http import JsonResponse
import ipdb
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TopicForm

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'topics/topic_list.html', {'topics': topics})

def show_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    return render(request, 'topics/show_topic.html', {'topic': topic})

def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('topic_list')  # Replace 'topic_list' with the name of your topic list URL
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = TopicForm()

    return render(request, 'topics/create_topic.html', {'form': form})

def follow_unfollow_topic(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    user = request.user

    if user in topic.followed_by.all():
        topic.followed_by.remove(user)
    else:
        topic.followed_by.add(user)

    topic.save()

    followed = user in topic.followed_by.all()
    label = 'Following' if followed else 'Follow +'

    return JsonResponse({'status': 'success', 'label': label})
