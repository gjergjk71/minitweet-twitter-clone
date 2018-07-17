from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_photo", null=True, blank=True)
    description = models.TextField(max_length=250, blank=True)
    birthday = models.DateTimeField(null=True, blank=True)
    education = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.user)


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

    def __str__(self):
        return "{} started following {}".format(self.follower.username, self.following.username)
