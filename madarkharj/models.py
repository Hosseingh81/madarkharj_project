from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Group(models.Model):
    member=models.ManyToManyField(Member,blank=True)



