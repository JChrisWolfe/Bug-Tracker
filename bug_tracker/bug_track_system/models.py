from django.db import models

# Create your models here.
class Bugs(models.Model):
    bug_id = models.IntegerField(primary_key=True)
    bug_developer_id = models.IntegerField()
    bug_title = models.CharField(max_length=60)
    bug_type = models.CharField(max_length=20)
    bug_description = models.TextField(max_length=3000)
    bug_tester_id = models.IntegerField()

class Projects(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_developer_id = models.IntegerField()
    project_tester_id = models.IntegerField()
    project_name = models.CharField(max_length=20)
    project_assign = models.TextField()
    project_last_date = models.DateField(auto_now=True, auto_now_add=True)
    project_type = models.CharField(max_length=20)
    project_description = models.TextField(max_length=3000)