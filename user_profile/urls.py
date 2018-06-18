from django.urls import path
from . import views
from tweets.views import createTweet

urlpatterns = [
	path("profile/<username>",views.showProfile,name="showProfile"),
	path("follow/<ID>",views.followUser,name="followUser"),
	path("unfollow/<ID>",views.unfollowUser,name="unfollowUser"),
    path("profile/createTweet/", createTweet,name="createTweet")
]
