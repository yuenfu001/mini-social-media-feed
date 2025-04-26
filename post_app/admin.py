from django.contrib import admin
from .models import Post, Profile

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id','user_post','post','date_created','date_modified'
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user','contact','location'
    ]



