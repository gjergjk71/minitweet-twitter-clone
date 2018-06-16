from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
# Create your views here.

def redirectLogin(request):
	return redirect("/login")

def custom_login(request):
	current_user = request.user
	if current_user.is_authenticated:
		return redirect("/feed")
	else:
		return login(request)


def register(request):
	if request.method == "POST":
		firstname = request.POST.get("firstname")
		lastname = request.POST.get("lastname")
		email = request.POST.get("email")
		username = request.POST.get("usernameRegister")
		password = request.POST.get("passwordRegister")

		createUser = User.objects.create_user(email=email,username=username,password=password)
		createUser.firstname = firstname
		createUser.lastname = lastname
		createUser.save()
		user = authenticate(username=request.POST.get("usernameRegister"),
								password=request.POST.get("passwordRegister"))
		if user is not None:
			return redirect("/feed")
		else:
			return redirect("/login")
	else:
		return redirect("/login")



