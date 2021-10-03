"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from authentication import views as auth_views
from notification import views as n_views
from tweet import views as tweet_views
from twitteruser import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.homepage, name='homepage'),
    path('login/', auth_views.login_page),
    path('logout/', auth_views.logout_view),
    path('tweet/', tweet_views.new_tweet),
    path('signup/', auth_views.signup_view),
    path('user/<int:id>/', user_views.user_detail, name='user'),
    path('tweet/<int:id>/', tweet_views.tweet_detail),
    path('follow/<int:id>/', user_views.follow_user),
    path('unfollow/<int:id>/', user_views.unfollow_user),
    path('notify/', n_views.notification_view)
]
