from django.contrib import admin
from .models import Profile
from .models import Post
from .models import LikePost

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)