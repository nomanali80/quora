# questions/views.py
from django.shortcuts import render, redirect
from .forms import QuestionForm
from topics.models import Topic
from .models import Question

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
