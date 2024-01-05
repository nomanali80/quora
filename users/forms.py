
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
import cloudinary
import cloudinary.uploader

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'age', 'gender', 'email', 'username', 'profile_picture')

    def save(self, commit=True):
        user = super().save(commit=False)

        if 'profile_picture' in self.cleaned_data:
            profile_picture = self.cleaned_data['profile_picture']
            result = cloudinary.uploader.upload(profile_picture, folder="profile_pics")
            user.profile_picture = result['secure_url']

        if commit:
            user.save()
        return user


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'age', 'gender', 'email', 'profile_picture']

    def save(self, commit=True):
        user = super().save(commit=False)

        if 'profile_picture' in self.changed_data:
            profile_picture = self.cleaned_data['profile_picture'].read()
            cloudinary_response = cloudinary.uploader.upload(profile_picture)
            user.profile_picture = cloudinary_response['secure_url']

        if commit:
            user.save()

        return user
