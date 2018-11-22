from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

def Post(models.Model):
    subreddit = models.ForeignKey('subreddit.Sub', on_delete=models.DO_NOTHING)
    author = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    votes = models.IntegerField(default=0)
    response_to = models.ForeignKey('posts.Post',
                                    on_delete=models.DO_NOTHING,
                                    null=True,
                                    blank=True)
    isComment = models.BooleanField(default=False)
    content = models.TextField()
    title = models.CharField(max_length=50)

def Vote(models.Model):
    value = models.IntegerField()
    owner = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    
