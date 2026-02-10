from django.db import models
from django.contrib.auth.models import Group
# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length= 100)
    email = models.EmailField(unique= True)
    password = models.CharField(max_length= 70)
    is_active = models.BooleanField(default= True)
    grupo = models.ForeignKey(Group, on_delete = models.CASCADE)

    def __str__(self):
        return self.username