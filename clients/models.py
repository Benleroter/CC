from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User
#from django.urls import reverse
from PIL import Image


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(default='n/a',max_length=255, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    contact1 = models.CharField(max_length=255, blank=True, null=True)
    contact1tel = models.CharField(max_length=255, blank=True, null=True)
    contact1email = models.CharField(max_length=255, blank=True, null=True)
    contact2 = models.CharField(max_length=255, blank=True, null=True)
    contact2tel = models.CharField(max_length=255, blank=True, null=True)
    contact2email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'client'

    def __str__(self):
        return f'{self.user.username} ClientProfile'  

    #def save(self, *args, **kwargs):
    #    super(clientProfile,self).save(*args, **kwargs)    

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
