from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Post


@receiver(post_save,sender=User)
def create_profile_for_new_user(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


# @receiver(post_save,sender=Post)
# def create_tag_for_new_post(sender,instance,created,**kwargs):
#     if created:
#         Likes.objects.create(posting=instance)