from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import LoginForm
from twitterclone.twitterusers.forms import Add_User_form
from twitterclone.twitterusers.models import TwitterUser

def login_view(request):
    html = 'login.html'

    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get(
                    'next', reverse('homepage')
                    )
            )

    login_form = LoginForm()

    return render(request, html, {'login_form': login_form})


def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('homepage'))


def registeruser_form(request):
    html = 'formz.html'

    if request.method == 'POST':
        register_form = Add_User_form(request.POST)

        if register_form.is_valid():
            data = register_form.cleaned_data
            user = User.objects.create_user(
                username=data['name'],
                password=data['password']
            )
            TwitterUser.objects.create(
                user=user,
                # name=data['name']
            )
            return HttpResponseRedirect(reverse('homepage'))

    register_form = Add_User_form()

    return render(request, html, {'form': register_form})
