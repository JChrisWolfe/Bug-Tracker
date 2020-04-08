from django.db import models
from phone_field import PhoneField

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

class Permission(models.Model):
    permission_id = models.IntegerField(primary_key=True)
    permission_role_id = models.IntegerField()
    permission_module = models.TextField()
    permission_name = models.CharField(max_length=20)

class Manager(models.Model):
    manager_id = models.IntegerField(primary_key=True)
    manager_name = models.CharField(max_length=20)

    # https://pypi.org/project/django-phone-field/
    manager_mobile = PhoneField(blank=True, help_text='Contact Phone Number')
    manager_email = models.EmailField()
    manager_address = models.CharField(max_length=500)
    manager_username = models.CharField(max_length=20)
    # Add manager_password maybe?

class Tester(models.Model):
    tester_id = models.IntegerField(primary_key=True)
    tester_name = models.CharField(max_length=20)
    tester_email = models.EmailField()
    tester_address = models.CharField(max_length=500)

    # tester_password maybe?
