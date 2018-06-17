from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	text = models.TextField(max_length=1000)
	created_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.text[:250]

class HashTag(models.Model):
	name = models.CharField(max_length=100,unique=True)
	tweets = models.ManyToManyField(Tweet)
	def __str__(self):
		return self.name