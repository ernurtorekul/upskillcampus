from django.db import models


# Create your models here.

class URL(models.Model):
    name = models.CharField(max_length = 255)
    link = models.CharField(max_length = 10000)
    uuid = models.CharField(max_length = 10)

