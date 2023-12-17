from django.db import models
from profiles.models import Profile


class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='items')
    image = models.ImageField(upload_to='items', blank=True, null=True)
