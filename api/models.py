from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    img = models.ImageField(upload_to ='uploads/% Y/% m/% d/', blank=True, null=True)