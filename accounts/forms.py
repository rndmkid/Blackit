from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User
from django.contrib.auth import get_user_model

class CustomAuthenticationForm(AuthenticationForm):

    def authenticate(self, request, username, password, **kwargs):
        UserModel = get_user_model()
        try:
            out = UserModel.objects.get(username=username,
                                        password=password)
            return out
        except:
            return None
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = self.authenticate(self.request,
                                           username=username,
                                           password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

class UserForm(UserCreationForm):
    
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
