from django.db import models

# Create your models here.
class Bookshops(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=15)
	address = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.name

class Books(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=3, decimal_places=0)
	language = models.CharField(max_length=20)
	editor = models.CharField(max_length=50, blank=True)
	is_second_hand = models.BooleanField(default=False)
	bookshop = models.ForeignKey(Bookshops)

	def __str__(self):
		return self.name

