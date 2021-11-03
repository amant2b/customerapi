from django.db import models

# Create your models here.


class customerModel(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    age=models.IntegerField()
    phoneno=models.CharField(max_length=12)
    email=models.EmailField(max_length=254)

