from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.http.response import HttpResponseRedirect
from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import MyUser
from django.contrib.auth.decorators import login_required
import re


@login_required
def new_tweet(request, id=None):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            msg = Tweet.objects.create(
                tweet=data['tweet'],
                tweeter=request.user
            )
            num_tweet = MyUser.objects.get(username=request.user)
            num_tweet.posts += 1
            num_tweet.save()
            if "@" in msg.tweet:
                check = re.compile(r"@\S+")
                match = check.findall(msg.tweet)
                for username in match:
                    username = username.replace('@', '')
                    matched = MyUser.objects.get(username=username)
                    msg.tags.add(matched)
                    msg.save()
            return HttpResponseRedirect(reverse('homepage'))
    form = TweetForm()
    return render(request, 'form.html', {'form': form})


def tweet_detail(request, id):
    tweet = Tweet.objects.get(id=id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})
