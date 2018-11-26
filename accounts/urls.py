"""Blackit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from django.contrib.auth.views import LoginView, LogoutView

from .forms import CustomAuthenticationForm
from . import views

urlpatterns = [
    url('^login/$',
        LoginView.as_view(template_name="login.html",
                          authentication_form=CustomAuthenticationForm,
                          ),
        name='login'),
    url('^logout/$', LogoutView.as_view(next_page="/login/")),
    url('^new/$', views.user_new, name='user_new'),

    #User Settings/Edit

    #User Profile
]