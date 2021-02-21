from django.db import models

class Poliklinik(models.Model):
    kd_poli = models.CharField(primary_key=True, max_length=5)
    nm_poli = models.CharField(max_length=50, blank=True, null=True)
    registrasi = models.FloatField()
    registrasilama = models.FloatField()
    status = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'poliklinik'

class Bangsal(models.Model):
    kd_bangsal = models.CharField(primary_key=True, max_length=5)
    nm_bangsal = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bangsal'

class Kamar(models.Model):
    kd_kamar = models.CharField(primary_key=True, max_length=15)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal', blank=True, null=True)
    trf_kamar = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)
    kelas = models.CharField(max_length=11, blank=True, null=True)
    statusdata = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kamar'