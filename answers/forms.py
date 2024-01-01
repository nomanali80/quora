# answers/forms.py
from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {'content': forms.TextInput(attrs={'class': 'form-control'})}