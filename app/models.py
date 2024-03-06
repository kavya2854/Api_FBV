from django.db import models

# Create your models here.

class School(models.Model):
    Scname=models.CharField(max_length=100)
    Scpricipal=models.CharField(max_length=100)
    Sclocation=models.CharField(max_length=100)

    def __str__(self):
        return self.Scname