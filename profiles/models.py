from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
