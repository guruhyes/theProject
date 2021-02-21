from django.db import models

# Create your models here.
class data(models.Model):
    kode_agama = models.CharField(max_length=5,primary_key=True)
    agama = models.CharField(max_length=10,unique=True)

