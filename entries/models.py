from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Entry(models.Model):
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    classification = models.CharField(max_length=64)
    entry_name = models.CharField(max_length=64)
    tier = models.CharField(max_length=1,default='f')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entry_name
