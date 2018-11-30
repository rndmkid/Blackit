from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Post(models.Model):
    subreddit = models.ForeignKey('subreddits.Subreddit', on_delete=models.DO_NOTHING)
    author = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    votes = models.IntegerField(default=0)
    response_to = models.ForeignKey('posts.Post',
                                    on_delete=models.DO_NOTHING,
                                    null=True,
                                    blank=True)
    isComment = models.BooleanField(default=False)
    title = models.TextField()

class Vote(models.Model):
    UP = 1
    DOWN = -1
    VOTE_CHOICES = (
        (UP, 'up'),
        (DOWN, 'down'),
    )
    
    value = models.IntegerField(choices=VOTE_CHOICES)
    owner = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    
