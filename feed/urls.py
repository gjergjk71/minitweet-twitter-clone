from django.urls import path, include
from . import views
from tweets.views import createTweet
urlpatterns = [
    path("feed", views.feed,name="feed"),
    path("feed/createTweet", createTweet,name="createTweet")
]
