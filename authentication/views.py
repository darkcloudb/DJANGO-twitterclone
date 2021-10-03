from django.shortcuts import render, reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from authentication.forms import LoginForm, SignUpForm
from twitteruser.models import MyUser


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        new_user = MyUser.objects.create_user(
            username=data['username'],
            password=data['password']
            )
        login(request, new_user)
        return HttpResponseRedirect(reverse('homepage'))
    form = SignUpForm()
    return render(request, 'new_tweeter.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, 'form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
