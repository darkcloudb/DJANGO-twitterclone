from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from twitteruser.models import MyUser
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    self = request.user
    followers = self.following.values('id')
    self_tweets = Tweet.objects.filter(tweeter=self).order_by('-tweeted_at')
    follower_tweets = Tweet.objects.filter(tweeter__in=followers).order_by('-tweeted_at')
    tweets = self_tweets | follower_tweets
    return render(request, 'index.html', {'self': self, 'tweets': tweets})
# received help from my brother on above function ^


def user_detail(request, id):
    tweeter = MyUser.objects.get(id=id)
    tweets = Tweet.objects.all()
    followers = tweeter.followers.all()
    following = tweeter.following.all()
    return render(request, 'user_detail.html', {'tweeter': tweeter, 'tweets': tweets, 'followers': followers, 'following': following})


def follow_user(request, id):
    self = request.user
    target = MyUser.objects.get(id=id)
    self.following.add(target)
    # target.following.add(self)
    self.save()
    return redirect(request.META.get("HTTP_REFERER"))


def unfollow_user(request, id):
    self = request.user
    target = MyUser.objects.get(id=id)
    self.following.remove(target)
    # target.following.remove(self)
    # self.follow_check.set = False
    self.save()
    print('unfollowed')
    return redirect(request.META.get("HTTP_REFERER"))
