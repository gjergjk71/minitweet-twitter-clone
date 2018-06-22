from django.db import models
from django.contrib.auth.models import User
from user_profile.models import Profile

# Create your models here.

class Tweet(models.Model):
	profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	text = models.TextField(max_length=1000)
	created_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.text[:250]

class Comment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE)
	text = models.TextField(max_length=1000)
	created_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.text[:250]

class LikeTweet(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE)
	def __str__(self):
		return "{} - {}".format(self.user,self.tweet)

class LikeComment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
	def __str__(self):
		return "{} - {}".format(self.user,self.comment)

class HashTag(models.Model):
	name = models.CharField(max_length=100,unique=True)
	tweets = models.ManyToManyField(Tweet)
	def __str__(self):
		return self.name