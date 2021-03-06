from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from markdownx.fields import MarkdownxFormField

from notes.models import Note


class NoteForm(forms.ModelForm):
    text = MarkdownxFormField()

    class Meta:
        model = Note
        fields = ['title', 'is_public', 'text']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
