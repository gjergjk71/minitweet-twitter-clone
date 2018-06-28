from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
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



