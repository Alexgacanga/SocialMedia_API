from django.db import models
from django.forms import CharField, IntegerField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique= True)
    bio = models.CharField(blank= True)
    profile_picture = models.ImageField(blank= True, null= True, upload_to='profile_pics/')

    def __str__(self):
        return self.username
    
class Follow(models.Model):
    follower = models.ForeignKey(User, related_name= 'following', on_delete= models.CASCADE)
    following = models.ForeignKey(User, related_name= 'followers', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        unique_together = ('follower', 'following')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.follower} follows {self.following}"