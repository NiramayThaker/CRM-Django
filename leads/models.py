from django.db import models

# Create your models here.
class Lead(models.Model):
	SOURCE_CHOICES = (
		('YouTube', 'YouTube')
		('Google', 'Google')
		('Newsletter', 'Newsletter')
	)

	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	age = models.IntegerField(default=0)
	phoned = models.BooleanField(default=False)
	source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
