from django.contrib import admin
from .models import User, Image, Like   

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'device_id')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_id', 'url', 'user_id', 'created_at', 'description', 'hashtags', 'orientation')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'like_type', 'image_id', 'user_id', 'pixels')

admin.site.register(User, UserAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Like, LikeAdmin)
