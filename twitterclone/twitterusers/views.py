from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import Add_User_form
from .models import TwitterUser
from twitterclone.tweets.models import Tweet


def userview(request, id):
    html = 'useronly.html'

    users = TwitterUser.objects.filter(id=id)

    userstweets = Tweet.objects.filter(twitteruser=id)

    following_count = users.first().following.count()

    return render(request, html,
                  {'users': users, 'userstweets': userstweets, 'following_count': following_count})

def userform_view(request):
    html = 'formz.html'

    if request.method == 'POST':
        twitter_user_form = Add_User_form(request.POST)

        if twitter_user_form.is_valid():
            data = twitter_user_form.cleaned_data
            user = User.objects.create_user(
                username=data['name'],
                password=data['password']
            )
            TwitterUser.objects.create(
                user=user,
                name=data['name']
            )
            return HttpResponseRedirect(reverse('homepage'))

    twitter_user_form = AddUserForm()

    return render(request, html, {'form': twitter_user_form})

def follow_view(request, id):

    following = TwitterUser.objects.get(id=id)

    request.user.twitteruser.following.add(following)

    return HttpResponseRedirect(reverse('user', args=(id,)))


def unfollow_view(request, id):

    unfollow = TwitterUser.objects.get(id=id)

    request.user.twitteruser.following.remove(unfollow)

    return HttpResponseRedirect(reverse('user', args=(id,)))    
