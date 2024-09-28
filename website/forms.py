from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('name', 'email', 'text')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a your email'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a your question'
            })
        }