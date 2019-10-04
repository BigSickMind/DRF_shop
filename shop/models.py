from django.db import models


class User(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    creation_date = models.DateTimeField()
