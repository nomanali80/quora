
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
import cloudinary
import cloudinary.uploader

class CustomUserCreationForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('name', 'age', 'gender', 'email', 'username', 'profile_picture')

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture', False)
        if profile_picture:
            result = cloudinary.uploader.upload(profile_picture, folder="profile_pics")
            return result['secure_url']
        else:
            return None

    def clean_age(self):
        content = self.cleaned_data['age']
        if content <= 0:
            raise forms.ValidationError("Age must greater than 0")

        return content

    def save(self, commit=True):
        user = super().save(commit=False)
        cleaned_profile_picture = self.clean_profile_picture()
        if cleaned_profile_picture:
            user.profile_picture = cleaned_profile_picture
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
