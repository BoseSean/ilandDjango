from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.conf import settings
# from ckeditor.fields import RichTextField

#Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=200, unique=True)
    tag_slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.tag_name
    def get_absolute_url(self):
        return "/%s/" %(self.tag_slug)

class Department(models.Model):
    department_name = models.CharField(max_length=200, unique=True)
    department_slug = models.SlugField(max_length=200, unique=True)
    def __unicode__(self):
        return self.department_name
    def get_absolute_url(self):
        return "/%s/" %(self.department_name)


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length = 150,blank = False)
    tag = models.ManyToManyField(Tag)
    body = models.TextField()
    draft = models.BooleanField(default=True)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    department = models.ManyToManyField(Department)
    
 

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s" %(self.id)

    class Meta:
        ordering = ["-timestamp", "-updated"]