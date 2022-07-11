from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    Image=models.ImageField(null=True,blank=True,upload_to="images/")

