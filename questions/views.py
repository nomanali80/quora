# questions/views.py
from django.shortcuts import render, redirect
from .forms import QuestionForm
from topics.models import Topic
from .models import Question
from django.http import JsonResponse
import ipdb

def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user  # Assuming you have user authentication in place
            question.save()
            form.save_m2m()  # Save the many-to-many relationships
            return redirect('question_list')  # Change 'question_list' to your actual URL name for displaying questions
    else:
        form = QuestionForm()

    topics = Topic.objects.all()
    return render(request, 'questions/create_question.html', {'form': form, 'topics': topics})


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'questions/question_list.html', {'questions': questions})

def like_dislike_question(request, question_id):
    like_dislike = request.POST.get('like_dislike', None)
    question = Question.objects.get(pk=question_id)
    user = request.user

    if like_dislike == 'like':
      if user in question.liked_by.all():
          question.liked_by.remove(user)
      else:
          question.liked_by.add(user)
          question.disliked_by.remove(user)
    else:
      if user in question.disliked_by.all():
          question.disliked_by.remove(user)
      else:
          question.disliked_by.add(user)
          question.liked_by.remove(user)

    question.save()

    liked = user in question.liked_by.all()
    disliked = user in question.disliked_by.all()

    return JsonResponse({'status': 'success', 'like_count': question.liked_by.count(), 'dislike_count': question.disliked_by.count(), "liked": liked, "disliked": disliked })

