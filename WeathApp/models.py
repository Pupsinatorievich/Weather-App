from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()