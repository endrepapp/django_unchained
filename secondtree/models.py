from django.db import models

class User(models.Model):
	user = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)

	def __str__(self):
		return self.user

class ItemDet(models.Model):
	image = models.ImageField()
	position = models.IntegerField()
	description = models.CharField(max_length=500)
	price = models.IntegerField()
	category = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	objects = models.Manager()

	def __str__(self):
		return self.name + ' - ' + self.category

