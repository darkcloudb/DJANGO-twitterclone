from django.shortcuts import render
from tweet.models import Tweet

def notification_view(request):
    you = request.user
    tweets = Tweet.objects.filter(tags=you)
    for tweet in tweets:
        tweet.tags.clear()
        tweet.save()
    return render(request, 'notify.html', {'tweets': tweets})
