from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile,Follow
# Create your views here.

def showProfile(request,username):
	user = User.objects.get(username=username)
	profile = Profile.objects.get(user=user)

	user_followers = len(Follow.objects.filter(follower=user))
	user_following = len(Follow.objects.filter(following=user))

	context = {"user_info":user,"profile":profile,
			"user_followers":user_followers,"user_following":user_following}

	return render(request,"profile.html",context)

