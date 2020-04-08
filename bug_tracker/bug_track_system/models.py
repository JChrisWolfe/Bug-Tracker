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
    pass