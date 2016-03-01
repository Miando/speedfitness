from django.db import models
from django.contrib.flatpages.models import FlatPage as FlatPageOld

class FlatPage(FlatPageOld):
    photo = models.ImageField(upload_to='new/')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    menu = models.CharField(max_length=200)
    images = models.ImageField(upload_to='new', blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
