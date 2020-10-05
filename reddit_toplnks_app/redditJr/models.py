from django.db import models

# Create your models here.

class user_data(models.Model):
	email = models.EmailField()
	post = models.TextField()
# 	