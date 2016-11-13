from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Kind(models.Model):
	name=models.CharField(max_length=30)
	def __unicode__ ():
		return self.name

class Manager(models.Model):
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	email=models.EmailField()
	lastTime=models.DateTimeField()
	def __unicode__ ():
		return self.username

class Article(models.Model):
	title=models.CharField(max_length=100)
	text=models.TextField()
	time=models.DateTimeField()
	user=models.ForeignKey(Manager)
	kind=models.ForeignKey(Kind)
	def __unicode__ (self):
		return self.title

class Comment(models.Model):
	text=models.TextField()
	time=models.DateTimeField()
	email=models.EmailField(blank=True)
	article=models.ForeignKey(Article)
	def __unicode__ (self):
		return self.text


	