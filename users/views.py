from django.shortcuts import render, redirect
from django.contrib.auth.views import login 

# Create your views here.

def custom_login(request):
	current_user = request.user
	if current_user.is_authenticated:
		return redirect("/feed/")
	else:
		return login(request)

