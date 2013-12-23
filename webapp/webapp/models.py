from django.db import models
from django.contrib.auth.models import User

class License(models.Model):
	name = models.CharField(max_length=30)
	text = models.TextField()

	def __str__(self):
		return self.name

class UserLicense(models.Model):
	# user = models.ForeignKey(User)
	license_type = models.ForeignKey(License)
	author = models.CharField(max_length=500)
	year = models.DateField()
	organisation = models.CharField(max_length=500)
	short_url = models.CharField(max_length=5, blank=True, unique=True)