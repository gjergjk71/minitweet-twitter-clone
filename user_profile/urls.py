from django.urls import path
from . import views

urlpatterns = [
	path("profile/<username>",views.showProfile,name="showProfile"),
	path("follow/<ID>",views.followUser,name="followUser"),
]
