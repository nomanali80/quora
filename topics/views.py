#from django.shortcuts import render
from .models import Topic

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'topics/topic_list.html', {'topics': topics})


from django.shortcuts import render, redirect
from .forms import TopicForm

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
