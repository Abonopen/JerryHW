from django.db import models
from datetime import datetime
# Create your models here.
class Message(models.Model):
	auther = models.CharField(max_length=20)
	title = models.CharField(max_length=50)
	content = models.TextField(max_length=500)
	date = models.DateTimeField()

	def __str__(self):
		return self.title
