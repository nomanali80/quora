from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomUserForm
from django.contrib.auth.decorators import login_required

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

@login_required    
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')  # Redirect to the profile page after successful update
    else:
        form = CustomUserForm(instance=request.user)

    return render(request, 'registration/edit_profile.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

