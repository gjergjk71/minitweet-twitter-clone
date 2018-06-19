from django.contrib import admin
from .models import Tweet,HashTag,Comment,LikeTweet,LikeComment
# Register your models here.

admin.site.register(Tweet)
admin.site.register(HashTag)
admin.site.register(Comment)
admin.site.register(LikeTweet)
admin.site.register(LikeComment)
