from django.shortcuts import render, redirect
from .models import Tweet
# Create your views here.

def createTweet(request):
	if request.method == "POST":
		current_user = request.user
		text = request.POST.get("tweetText")
		nextPage = request.POST.get("next")
		tweet = Tweet.objects.create(user=current_user,text=text)
		return redirect(nextPage)
	else:
		return redirect(nextPage)