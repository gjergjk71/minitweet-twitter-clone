from django.urls import path, include
from . import views

urlpatterns = [
    path("feed", views.feed,name="feed"),
]
