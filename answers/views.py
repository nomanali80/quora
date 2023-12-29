# answers/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm
from .models import Answer
from questions.models import Question
import ipdb

# ... (existing imports)

@login_required
def create_answer(request, question_id):
    # ... (existing code)
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Return a partial HTML response for AJAX requests
                answers = Answer.objects.filter(question=question)
                return render(request, 'questions/answers_partial.html', {'answers': answers})

            return redirect('question_list')