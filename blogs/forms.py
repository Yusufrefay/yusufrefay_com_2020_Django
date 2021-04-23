from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'id':'name', 'class' : 'input', 'type': 'text', 'name': 'name', 'placeholder': 'Full name'}),
            'email': forms.TextInput(attrs={'id':'email', 'class' : 'input', 'type': 'email', 'name': 'email', 'placeholder': 'example@example.com'}),
            'body': forms.Textarea(attrs={'id':'message', 'class' : 'input', 'name': 'message', 'placeholder': 'Your comments...'})
        }