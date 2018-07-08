from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user_profile.models import Profile
# Create your views here.

def redirectLogin(request):
	return redirect("/login")

def custom_login(request,**kwargs):
	if request.user.is_authenticated:
		return redirect("/feed")
	elif request.method == "POST":            
		username=request.POST.get("username")
		password = request.POST.get("password")                     
		user = authenticate(request, username=username, password=password)
		if user is not None:
			return login(request)
		else:
			return render(request,"registration/login.html",{'invalid': True })
	elif request.method == "GET":
		return login(request)

def register(request): #
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			birthday = request.POST.get("birthday")
			education = request.POST.get("education")
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')

			user = authenticate(username=username,
									password=raw_password)
			Profile.objects.create(user=user,birthday=birthday,education=education)

			return redirect('/feed')
	else:
		form = UserCreationForm()
	
	return render(request,"registration/register.html",{"form":form})


