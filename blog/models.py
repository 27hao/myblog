from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
	title=models.CharField(max_length=100)
	text=models.TextField()
	time=models.DateTimeField()
	user=models.CharField(max_length=30)
	def __unicode__ (self):
		return self.title
class Comment(models.Model):
	text=models.TextField()
	time=models.DateTimeField()
	email=models.EmailField(blank=True)
	article=models.ForeignKey(Article)
	def __unicode__ (self):
		return self.text