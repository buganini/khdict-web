from django.db import models
from django.contrib.auth.models import User

class Land(models.Model):
    def __unicode__(self):
        return self.creator.username+"/"+self.name
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Tinderland(models.Model):
    def __unicode__(self):
        return self.creator.username+"/"+self.name
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    land = models.ForeignKey(Land, null=True)
    osm = models.BooleanField()

class Tinder(models.Model):
    def __unicode__(self):
        return self.creator.username+"/"+self.land.title+"/"+self.title
	creator = models.ForeignKey(User)
	land = models.ForeignKey(Land)
	title = models.CharField(max_length=255)
	lat = models.DecimalField(max_digits=13, decimal_places=10)
	lng = models.DecimalField(max_digits=13, decimal_places=10)
