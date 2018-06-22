from django.shortcuts import render, redirect
from .models import Tweet
from django.contrib.auth.models import User
from user_profile.models import Profile
# Create your views here.

def createTweet(request):
	if request.method == "POST":
		current_user = request.user
		text = request.POST.get("tweetText")
		nextPage = request.POST.get("next")
		if nextPage == "/feed":
			user_profile = Profile.objects.get(user=current_user)
			tweet = Tweet.objects.create(profile=user_profile,user=current_user,text=text)
		elif "/profile/" in nextPage:
			username = nextPage.split("/")[-1]
			user_profile = User.objects.get(username=username)
			current_profile = Profile.objects.get(user=user_profile)
			tweet = Tweet.objects.create(profile=current_profile,user=current_user,text=text)
		return redirect(nextPage)
	else:
		return redirect(nextPage)