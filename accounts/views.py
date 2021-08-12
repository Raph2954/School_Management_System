from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,ListView,View
from django.shortcuts import render, redirect, get_object_or_404
from secondary.models import Teacher, Student, Subjects, Class
from django.http import HttpResponseRedirect, request, HttpResponse
from django.contrib import messages
from .forms import LoginForm,UserRegistrationForm
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                          'registration/registration_done.html',
                          {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})




