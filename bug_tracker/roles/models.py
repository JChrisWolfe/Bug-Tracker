from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_role_id = models.IntegerField()
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=254)

class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_title = models.CharField(max_length=20)
    role_description = models.TextField(max_length=2000)