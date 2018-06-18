from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,Follow
# Create your views here.

def showProfile(request,username):
	user = User.objects.get(username=username)
	profile = Profile.objects.get(user=user)
	unfollow_user = False
	user_followers = len(Follow.objects.filter(follower=user))
	user_following = len(Follow.objects.filter(following=user))

	if Follow.objects.filter(follower=request.user,following=user):
		unfollow_user = True
	context = {"user_info":user,"profile":profile,"unfollow_user":unfollow_user,
			"user_followers":user_followers,"user_following":user_following}

	return render(request,"profile.html",context)

def followUser(request,ID):
	follow_args = {
		"follower":request.user,
		"following":User.objects.get(pk=ID)
	}
	if not Follow.objects.filter(**follow_args):
		Follow.objects.create(**follow_args)

	return redirect("/profile/{}".format(follow_args["following"].username))

def unfollowUser(request,ID):
	follow_args = {
		"follower":request.user,
		"following":User.objects.get(pk=ID)
	}
	Follow.objects.filter(**follow_args).delete()
	return redirect("/profile/{}".format(follow_args["following"].username))
