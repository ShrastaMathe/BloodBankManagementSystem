from django.db import models

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  age= models.IntegerField(null=True)
  blood_group = models.CharField(max_length=5, null='A')
  address= models.TextField(null=True)
  volume=models.IntegerField(null=True)
  joined_date = models.DateField(null=True)


