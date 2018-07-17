from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tweets.models import Tweet
from user_profile.models import Follow,Profile
# Create your views here.

@login_required
def feed(request):
	current_user = request.user
	following = [current_user]
	for follow in Follow.objects.filter(follower=current_user):
		# following is the User which is followed by 
		# current_user or follow.follower
		following.append(follow.following)

	tweets = Tweet.objects.filter(user__in=following).order_by("-created_date")
	current_userProfile = Profile.objects.get(user=current_user)
	context = {"tweets":tweets}
	return render(request,"feed.html",context)