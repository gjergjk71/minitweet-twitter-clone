from django.shortcuts import render, redirect
from .models import Tweet
# Create your views here.

def createTweet(request,redirectTo):
	if request.method == "POST":
		current_user = request.user
		text = request.POST.get("tweetText")
		tweet = Tweet.objects.create(user=current_user,text=text)
		return redirect(redirectTo)
	else:
		return redirect(redirectTo)
