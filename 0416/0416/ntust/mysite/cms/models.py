from django.db import models

# Create your models here.
class Myself(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=15)
	address = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.name

class member(models.Model):
	name = models.CharField(max_length=20)
	language = models.CharField(max_length=20)
	age = models.IntegerField(default=0)
	myself = models.ForeignKey(Myself)

	def __str__(self):
		return self.name

