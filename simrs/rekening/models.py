from django.db import models

# Create your models here.
class Rekening(models.Model):
    kd_rek = models.CharField(primary_key=True, max_length=15)
    nm_rek = models.CharField(max_length=100, blank=True, null=True)
    tipe = models.CharField(max_length=1, blank=True, null=True)
    balance = models.CharField(max_length=1, blank=True, null=True)
    level = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rekening'