from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Post
from django.contrib.auth import get_user_model

#Reminder: Classes = HTML/CSS classes

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
        )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder':'Title',
                    #'class':' '
                }
            ),
            
        }
