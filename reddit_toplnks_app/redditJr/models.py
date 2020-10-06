from django.db import models

# Create your models here.

class User_data(models.Model):
	user_name = models.CharField(max_length = 20,unique = True,null = False)
	subreddits = models.TextField()
# 	