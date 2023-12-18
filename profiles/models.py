from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

class Profile(models.Model):
    username = models.CharField(max_length=15)
    profile_pic = models.ImageField(
        upload_to='profile_pics', blank=True, null=True)
    account = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profiles')
