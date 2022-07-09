# start
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control-input',
                 'required': True,
                 'placeholder': 'Article Title'
                }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control-input',
                'required': True,
                'placeholder': 'Article Title Tag' 
                }),
            'author': forms.Select(attrs={
                'class': 'form-control-input',
                'required': True,
                }),
            'body': forms.Textarea(attrs={
                'class': 'form-control-input',
                'required': True,
                'placeholder': 'Article Content'
                }),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control-input',
                 'required': True,
                 'placeholder': 'Article Title'
                }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control-input',
                'required': True,
                'placeholder': 'Article Title Tag' 
                }),
            'body': forms.Textarea(attrs={
                'class': 'form-control-input',
                'required': True,
                'placeholder': 'Article Content'
                }),
        }

