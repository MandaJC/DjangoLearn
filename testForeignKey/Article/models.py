from django.db import models

# Create your models here.

class User(models.Model):
    SEX_CHOICE = ("male", "femail")
    username = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=30)
    sex = models.CharField(choices=SEX_CHOICE)

class Article(models.Model):
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='author')
