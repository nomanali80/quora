from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['content', 'topics']

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) >= 250:
            raise forms.ValidationError("Content must be less than 250 characters.")

        return content
