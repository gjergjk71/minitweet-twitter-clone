from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
	path('', views.redirectLogin,name="redirectLogin"),
    path("login", views.custom_login, name="login"),
    path("register", views.register, name="register"),
]