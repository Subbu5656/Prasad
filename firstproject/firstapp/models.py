from django.db import models

# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=200)
	company = models.CharField(max_length=120)
	location = models.CharField(max_length=100)
	salary = models.FloatField()
	gmail = models.EmailField()
	mobile = models.IntegerField()
	def __str__(self):
		return self.name
