from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from topics.models import Topic
from .models import Question
from .forms import QuestionForm
from django.contrib import messages

def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            form.save_m2m()
            messages.success(request, 'Question created successfully.')
            return redirect('dashboard')
        else:
            error_messages = []

            for field, errors in form.errors.items():
                field_errors = ', '.join(errors)
                error_messages.append(f'{field.capitalize()}: {field_errors}')

            error_message = 'Failed to create question. ' + ', '.join(error_messages)
            messages.error(request, error_message)

    else:
        form = QuestionForm()

    topics = Topic.objects.all()
    return render(request, 'questions/create_question.html', {'form': form, 'topics': topics})

def show_question(request, question_id):
     question = get_object_or_404(Question, id=question_id)
     return render(request, 'questions/show_question.html', {'question': question})

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
