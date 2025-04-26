from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True,blank=True)
    contact = models.CharField(max_length=15)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user}'
    
    
class Post(models.Model):
    user_post = models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True,blank=True)
    post = models.TextField()
    likes = models.ManyToManyField(User,related_name='post_likes',blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    

    @property
    def like_count(self):
        return self.likes.count()
    
    def __str__(self):
        return f'{self.post}'
    
