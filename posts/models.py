from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

def Post(models.Model):
    subreddit = models.ForeignKey('subreddit.Sub', on_delete=models.DO_NOTHING)
    author = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    votes = models.IntegerField(default=0)
    vote = GenericRelation(Vote)
    

def Vote(models.Model):
    value = models.IntegerField()
    owner = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
##    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey('content_type', 'object_id')

def Comment(models.Model):

    
    vote = GenericRelation(Vote)
    

####
##Consider Merging Post/Comment
####
