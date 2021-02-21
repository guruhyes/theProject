from django.db import models

class PerusahaanPasien(models.Model):
    kode_perusahaan = models.CharField(primary_key=True, max_length=8)
    nama_perusahaan = models.CharField(max_length=70, blank=True, null=True)
    alamat = models.CharField(max_length=100, blank=True, null=True)
    kota = models.CharField(max_length=40, blank=True, null=True)
    no_telp = models.CharField(max_length=27, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perusahaan_pasien'
class SukuBangsa(models.Model):
    nama_suku_bangsa = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'suku_bangsa'
class CacatFisik(models.Model):
    nama_cacat = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = True
        db_table = 'cacat_fisik'
class BahasaPasien(models.Model):
    nama_bahasa = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bahasa_pasien'
class Propinsi(models.Model):
    kd_prop = models.AutoField(primary_key=True)
    nm_prop = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = True
        db_table = 'propinsi'
class Kabupaten(models.Model):
    kd_kab = models.AutoField(primary_key=True)
    nm_kab = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = True
        db_table = 'kabupaten'
class Kecamatan(models.Model):
    kd_kec = models.AutoField(primary_key=True)
    nm_kec = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = True
        db_table = 'kecamatan'
class Kelurahan(models.Model):
    kd_kel = models.AutoField(primary_key=True)
    nm_kel = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = True
        db_table = 'kelurahan'
class Penjab(models.Model):
    kd_pj = models.CharField(primary_key=True, max_length=3)
    png_jawab = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'penjab'
class Pasien(models.Model):
    no_rkm_medis = models.CharField(primary_key=True, max_length=15)
    nm_pasien = models.CharField(max_length=40, blank=True, null=True)
    no_ktp = models.CharField(max_length=20, blank=True, null=True)
    jk = models.CharField(max_length=1, blank=True, null=True)
    tmp_lahir = models.CharField(max_length=15, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    nm_ibu = models.CharField(max_length=40)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    gol_darah = models.CharField(max_length=2, blank=True, null=True)
    pekerjaan = models.CharField(max_length=35, blank=True, null=True)
    stts_nikah = models.CharField(max_length=13, blank=True, null=True)
    agama = models.CharField(max_length=12, blank=True, null=True)
    tgl_daftar = models.DateField(blank=True, null=True)
    no_tlp = models.CharField(max_length=40, blank=True, null=True)
    umur = models.CharField(max_length=20)
    pnd = models.CharField(max_length=14)
    keluarga = models.CharField(max_length=7, blank=True, null=True)
    namakeluarga = models.CharField(max_length=50)
    kd_pj = models.ForeignKey('Penjab', on_delete = models.CASCADE, db_column='kd_pj')
    no_peserta = models.CharField(max_length=25, blank=True, null=True)
    kd_kel = models.ForeignKey(Kelurahan, on_delete = models.CASCADE, db_column='kd_kel')
    kd_kec = models.ForeignKey(Kecamatan, on_delete = models.CASCADE, db_column='kd_kec')
    kd_kab = models.ForeignKey(Kabupaten, on_delete = models.CASCADE, db_column='kd_kab')
    pekerjaanpj = models.CharField(max_length=35)
    alamatpj = models.CharField(max_length=100)
    kelurahanpj = models.CharField(max_length=60)
    kecamatanpj = models.CharField(max_length=60)
    kabupatenpj = models.CharField(max_length=60)
    perusahaan_pasien = models.ForeignKey('PerusahaanPasien', on_delete = models.CASCADE, db_column='perusahaan_pasien')
    suku_bangsa = models.ForeignKey('SukuBangsa', on_delete = models.CASCADE, db_column='suku_bangsa')
    bahasa_pasien = models.ForeignKey(BahasaPasien, on_delete = models.CASCADE, db_column='bahasa_pasien')
    cacat_fisik = models.ForeignKey(CacatFisik, on_delete = models.CASCADE, db_column='cacat_fisik')
    email = models.CharField(max_length=50)
    nip = models.CharField(max_length=30)
    kd_prop = models.ForeignKey('Propinsi', on_delete = models.CASCADE, db_column='kd_prop')
    propinsipj = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'pasien'
