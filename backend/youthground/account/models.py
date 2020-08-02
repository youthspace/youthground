from django.db import models

class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=77)
    name = models.CharField(max_length=50)
    root_folder = models.CharField(max_length=36)
    created_at = models.DateTimeField()
