from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TopicForm
from .models import Topic

def topic_list(request):
    topics_per_page = 6
    topics = Topic.objects.all()

    paginator = Paginator(topics, topics_per_page)
    page = request.GET.get('page')
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    return render(request, 'topics/topic_list.html', {'topics': topics})

def show_topic(request, topic_id):
    questions_per_page = 10
    topic = get_object_or_404(Topic, id=topic_id)
    questions = topic.get_related_questions()
    paginator = Paginator(questions, questions_per_page)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    page = request.GET.get('page')
    return render(request, 'topics/show_topic.html', { 'topic': topic, 'questions': questions })

def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('topic_list')
        else:
            print(form.errors)
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
    followed_count = topic.followed_by.all().count()
    label = 'Following' if followed else 'Follow +'

    return JsonResponse({'status': 'success', 'label': label, 'followed_count': followed_count})
