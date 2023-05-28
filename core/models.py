from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    username = models.ForeignKey(User, on_delete= models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank = True)
    profile_img = models.ImageField(upload_to='profile_images', default = 'blanc_propic.png')
    date_of_birth = models.DateField()
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
    
    
    