from django.db import models

class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=255, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.name)
