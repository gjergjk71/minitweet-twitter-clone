from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from user_profile.models import Profile

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, **kwargs):
	if kwargs["created"]:
		Profile.objects.create(user=instance)