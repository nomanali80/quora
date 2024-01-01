# answers/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm
from .models import Answer
from questions.models import Question
import ipdb
from django.http import JsonResponse

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

def like_dislike_answer(request, answer_id):
    #ipdb.set_trace()
    like_dislike = request.POST.get('like_dislike', None)
    answer = Answer.objects.get(pk=answer_id)
    user = request.user

    if like_dislike == 'like':
      if user in answer.liked_by.all():
          answer.liked_by.remove(user)
      else:
          answer.liked_by.add(user)
          answer.disliked_by.remove(user)
    else:
      if user in answer.disliked_by.all():
          answer.disliked_by.remove(user)
      else:
          answer.disliked_by.add(user)
          answer.liked_by.remove(user)

    answer.save()

    liked = user in answer.liked_by.all()
    disliked = user in answer.disliked_by.all()

    return JsonResponse({'status': 'success', 'like_count': answer.liked_by.count(), 'dislike_count': answer.disliked_by.count(), "liked": liked, "disliked": disliked})
