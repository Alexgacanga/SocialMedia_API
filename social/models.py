from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name= 'posts')
    content = models.TextField()
    image = models.ImageField(upload_to= 'posts_images/', blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} - {self.created_at.strftime('%d/%m/%Y %H:%M')}"