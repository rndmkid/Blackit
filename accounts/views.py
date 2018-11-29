from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import UserForm
from .models import User
# Create your views here.

def user_new(request, template='user_new.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Unpack form values
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User(username=username,
                        password=password,
                        email=email,
                        )
            user.save()
            # Auto login the user
            return HttpResponseRedirect('/success/')
    else:
        form = UserForm()

    return render(request, template, {'form':form})

#User Profile/Detail View


#User Settings/Edit View
