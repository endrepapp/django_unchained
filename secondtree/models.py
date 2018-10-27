from django.db import models

class Post(models.Model):
	text = models.CharField(max_length=1000)

class User(models.Model):
	user = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class ItemDet(models.Model):
	image = models.ImageField()
	position = models.IntegerField(max_length=100)
	description = models.CharField(max_length=500)
	price = models.IntegerField()
	category = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
