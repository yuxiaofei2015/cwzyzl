from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,)
    owner = models.ForeignKey(User)

    def __str__(self):
        return "Group: %s" % self.id

    def __unicode__(self):
        return "Group: %s" % self.name


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    createTime = models.DateTimeField()
    author = models.ForeignKey(User)
    group = models.ForeignKey(Group, null=True)

    def __str__(self):
        return "Blog: %s" % self.id

    def __unicode__(self):
        return "Blog: %s" % self.title
