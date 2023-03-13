from django.db import models
from django.contrib.auth.models import User


class group(models.Model):
    name = models.CharField(max_length=16, null='')
    students = models.IntegerField()
    user = models.ManyToManyField(User, null= True)