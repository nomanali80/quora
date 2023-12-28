from django.urls import path
from users.views import register, dashboard, edit_profile
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html', success_url='/quora/dashboard/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # Add other views as needed
]