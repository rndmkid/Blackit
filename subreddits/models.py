from django.db import models

# Create your models here.
def Subreddit(models.Model):
    name = models.CharField(maxlength=50)
