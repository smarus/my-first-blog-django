from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    text = models.TextField()
    createdDate = models.DateTimeField(default=timezone.now())
    publishedDate = models.DateTimeField(blank=True, null=True)


def publish(self):
    self.publishedDate = timezone.now()
    self.save()


def __str__(self):
    return self.name


def __unicode__(self):
    return self.name
