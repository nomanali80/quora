from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login
from users.models import CustomUser 
from answers.models import Answer
from questions.models import Question
from topics.models import Topic
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('edit_profile')
        else:
            messages.error(request, 'Failed to update profile.')
    else:
        form = CustomUserForm(instance=request.user)

    return render(request, 'registration/edit_profile.html', {'form': form})

def show_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user_answers = Answer.objects.filter(user=user)
    followed_topics = Topic.objects.filter(followed_by=user)

    answered_data = {}
    for answer in user_answers:
        question = answer.question
        if question not in answered_data:
            answered_data[question] = []
        answered_data[question].append(answer)

    return render(request, 'registration/show_profile.html', {'user': user, 'answered_data': answered_data, 'followed_topics': followed_topics})


def dashboard(request):
    all_topics = Topic.objects.all()
    selected_topics = request.GET.getlist('topics')
    if selected_topics:
        questions = Question.objects.filter(topics__in=selected_topics)
    else:
        followed_topics = request.user.followings.all()
        questions = Question.objects.filter(topics__in=followed_topics)
    questions_per_page = 10
    paginator = Paginator(questions, questions_per_page)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'dashboard.html', {'questions': questions, 'all_topics': all_topics, 'selected_topics': selected_topics})
