# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    usere = models.TextField(blank=True, null=True)
    passworde = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'admin'


class AkunBayar(models.Model):
    nama_bayar = models.CharField(primary_key=True, max_length=50)
    kd_rek = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='kd_rek', blank=True, null=True)
    ppn = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'akun_bayar'


class AkunPiutang(models.Model):
    nama_bayar = models.CharField(primary_key=True, max_length=50)
    kd_rek = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='kd_rek', blank=True, null=True)
    kd_pj = models.ForeignKey('Penjab', on_delete = models.CASCADE, db_column='kd_pj', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'akun_piutang'
        unique_together = (('kd_rek', 'kd_pj'),)


class AmbilDankes(models.Model):
    id = models.OneToOneField('Pegawai', on_delete = models.CASCADE, db_column='id', primary_key=True)
    tanggal = models.DateField()
    ktg = models.CharField(max_length=50)
    dankes = models.FloatField()

    class Meta:
        managed = True
        db_table = 'ambil_dankes'
        unique_together = (('id', 'tanggal'),)


class AngsuranKoperasi(models.Model):
    id = models.OneToOneField('Pegawai', on_delete = models.CASCADE, db_column='id', primary_key=True)
    tanggal_pinjam = models.DateField()
    tanggal_angsur = models.DateField()
    pokok = models.FloatField()
    jasa = models.FloatField()

    class Meta:
        managed = True
        db_table = 'angsuran_koperasi'
        unique_together = (('id', 'tanggal_pinjam', 'tanggal_angsur'),)


class Antriapotek(models.Model):
    loket = models.IntegerField()
    antrian = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'antriapotek'


class Antriloket(models.Model):
    loket = models.IntegerField()
    antrian = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'antriloket'


class AplicareKetersediaanKamar(models.Model):
    kode_kelas_aplicare = models.CharField(primary_key=True, max_length=15)
    kd_bangsal = models.ForeignKey('Bangsal', on_delete = models.CASCADE, db_column='kd_bangsal')
    kelas = models.CharField(max_length=11)
    kapasitas = models.IntegerField(blank=True, null=True)
    tersedia = models.IntegerField(blank=True, null=True)
    tersediapria = models.IntegerField(blank=True, null=True)
    tersediawanita = models.IntegerField(blank=True, null=True)
    tersediapriawanita = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aplicare_ketersediaan_kamar'
        unique_together = (('kode_kelas_aplicare', 'kd_bangsal', 'kelas'),)


class AsuhanGizi(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tanggal = models.DateField()
    antropometri_bb = models.CharField(max_length=5, blank=True, null=True)
    antropometri_tb = models.CharField(max_length=5, blank=True, null=True)
    antropometri_imt = models.CharField(max_length=5, blank=True, null=True)
    antropometri_lla = models.CharField(max_length=5, blank=True, null=True)
    antropometri_tl = models.CharField(max_length=5, blank=True, null=True)
    antropometri_ulna = models.CharField(max_length=5)
    antropometri_bbideal = models.CharField(max_length=5)
    antropometri_bbperu = models.CharField(max_length=5)
    antropometri_tbperu = models.CharField(max_length=5)
    antropometri_bbpertb = models.CharField(max_length=5)
    antropometri_llaperu = models.CharField(max_length=5)
    biokimia = models.CharField(max_length=100, blank=True, null=True)
    fisik_klinis = models.CharField(max_length=100, blank=True, null=True)
    alergi_telur = models.CharField(max_length=5, blank=True, null=True)
    alergi_susu_sapi = models.CharField(max_length=5, blank=True, null=True)
    alergi_kacang = models.CharField(max_length=5, blank=True, null=True)
    alergi_gluten = models.CharField(max_length=5, blank=True, null=True)
    alergi_udang = models.CharField(max_length=5, blank=True, null=True)
    alergi_ikan = models.CharField(max_length=5, blank=True, null=True)
    alergi_hazelnut = models.CharField(max_length=5, blank=True, null=True)
    pola_makan = models.CharField(max_length=100, blank=True, null=True)
    riwayat_personal = models.CharField(max_length=100, blank=True, null=True)
    diagnosis = models.CharField(max_length=100, blank=True, null=True)
    intervensi_gizi = models.CharField(max_length=100, blank=True, null=True)
    monitoring_evaluasi = models.CharField(max_length=100, blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')

    class Meta:
        managed = True
        db_table = 'asuhan_gizi'
        unique_together = (('no_rawat', 'tanggal'),)


class Asuransi(models.Model):
    stts = models.CharField(primary_key=True, max_length=5)
    biaya = models.FloatField()

    class Meta:
        managed = True
        db_table = 'asuransi'


class AturanPakai(models.Model):
    tgl_perawatan = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    kode_brng = models.ForeignKey('Databarang', on_delete = models.CASCADE, db_column='kode_brng')
    aturan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aturan_pakai'
        unique_together = (('tgl_perawatan', 'jam', 'no_rawat', 'kode_brng'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, on_delete = models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete = models.CASCADE)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete = models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, on_delete = models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete = models.CASCADE)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, on_delete = models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete = models.CASCADE)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BahasaPasien(models.Model):
    nama_bahasa = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bahasa_pasien'


class Bangsal(models.Model):
    kd_bangsal = models.CharField(primary_key=True, max_length=5)
    nm_bangsal = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bangsal'


class Bank(models.Model):
    namabank = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = True
        db_table = 'bank'


class Barcode(models.Model):
    id = models.OneToOneField('Pegawai', on_delete = models.CASCADE, db_column='id', primary_key=True)
    barcode = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = True
        db_table = 'barcode'


class BayarPemesanan(models.Model):
    tgl_bayar = models.DateField(blank=True, null=True)
    no_faktur = models.ForeignKey('Pemesanan', on_delete = models.CASCADE, db_column='no_faktur', blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    besar_bayar = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    nama_bayar = models.ForeignKey(AkunBayar, on_delete = models.CASCADE, db_column='nama_bayar', blank=True, null=True)
    no_bukti = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bayar_pemesanan'
        unique_together = (('tgl_bayar', 'no_faktur'),)


class BayarPemesananNonMedis(models.Model):
    tgl_bayar = models.DateField(blank=True, null=True)
    no_faktur = models.ForeignKey('Ipsrspemesanan', on_delete = models.CASCADE, db_column='no_faktur', blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    besar_bayar = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    nama_bayar = models.ForeignKey(AkunBayar, on_delete = models.CASCADE, db_column='nama_bayar', blank=True, null=True)
    no_bukti = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bayar_pemesanan_non_medis'


class BayarPiutang(models.Model):
    tgl_bayar = models.DateField(primary_key=True)
    no_rkm_medis = models.ForeignKey('Pasien', on_delete = models.CASCADE, db_column='no_rkm_medis')
    besar_cicilan = models.FloatField()
    catatan = models.CharField(max_length=100)
    no_rawat = models.CharField(max_length=17)
    kd_rek = models.ForeignKey(AkunBayar, on_delete = models.CASCADE, db_column='kd_rek', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bayar_piutang'
        unique_together = (('tgl_bayar', 'no_rkm_medis', 'no_rawat'),)


class BeriBhpRadiologi(models.Model):
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    kode_brng = models.ForeignKey('Ipsrsbarang', on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat')
    jumlah = models.FloatField()
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'beri_bhp_radiologi'


class BeriObatOperasi(models.Model):
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    tanggal = models.DateTimeField()
    kd_obat = models.ForeignKey('ObatbhpOk', on_delete = models.CASCADE, db_column='kd_obat')
    hargasatuan = models.FloatField()
    jumlah = models.FloatField()

    class Meta:
        managed = True
        db_table = 'beri_obat_operasi'


class BerkasDigitalPerawatan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kode = models.ForeignKey('MasterBerkasDigital', on_delete = models.CASCADE, db_column='kode')
    lokasi_file = models.CharField(max_length=600)

    class Meta:
        managed = True
        db_table = 'berkas_digital_perawatan'
        unique_together = (('no_rawat', 'kode', 'lokasi_file'),)


class BerkasPegawai(models.Model):
    nik = models.ForeignKey('Pegawai', on_delete = models.CASCADE, db_column='nik')
    tgl_uploud = models.DateField()
    kode_berkas = models.ForeignKey('MasterBerkasPegawai', on_delete = models.CASCADE, db_column='kode_berkas')
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'berkas_pegawai'


class BiayaHarian(models.Model):
    kd_kamar = models.OneToOneField('Kamar', on_delete = models.CASCADE, db_column='kd_kamar', primary_key=True)
    nama_biaya = models.CharField(max_length=50)
    besar_biaya = models.FloatField()
    jml = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'biaya_harian'
        unique_together = (('kd_kamar', 'nama_biaya'),)


class BiayaSekali(models.Model):
    kd_kamar = models.OneToOneField('Kamar', on_delete = models.CASCADE, db_column='kd_kamar', primary_key=True)
    nama_biaya = models.CharField(max_length=50)
    besar_biaya = models.FloatField()

    class Meta:
        managed = True
        db_table = 'biaya_sekali'
        unique_together = (('kd_kamar', 'nama_biaya'),)


class Bidang(models.Model):
    nama = models.CharField(primary_key=True, max_length=15)

    class Meta:
        managed = True
        db_table = 'bidang'


class Billing(models.Model):
    noindex = models.IntegerField()
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    tgl_byr = models.DateField(blank=True, null=True)
    no = models.CharField(max_length=50)
    nm_perawatan = models.CharField(max_length=200)
    pemisah = models.CharField(max_length=1)
    biaya = models.FloatField()
    jumlah = models.FloatField()
    tambahan = models.FloatField()
    totalbiaya = models.FloatField()
    status = models.CharField(max_length=22, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'billing'


class BookingOperasi(models.Model):
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', blank=True, null=True)
    kode_paket = models.ForeignKey('PaketOperasi', on_delete = models.CASCADE, db_column='kode_paket', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    jam_mulai = models.TimeField(blank=True, null=True)
    jam_selesai = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=14, blank=True, null=True)
    kd_dokter = models.ForeignKey('Dokter', on_delete = models.CASCADE, db_column='kd_dokter', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'booking_operasi'


class BookingRegistrasi(models.Model):
    tanggal_booking = models.DateField(blank=True, null=True)
    jam_booking = models.TimeField(blank=True, null=True)
    no_rkm_medis = models.OneToOneField('Pasien', on_delete = models.CASCADE, db_column='no_rkm_medis', primary_key=True)
    tanggal_periksa = models.DateField()
    kd_dokter = models.ForeignKey('Dokter', on_delete = models.CASCADE, db_column='kd_dokter', blank=True, null=True)
    kd_poli = models.ForeignKey('Poliklinik', on_delete = models.CASCADE, db_column='kd_poli', blank=True, null=True)
    no_reg = models.CharField(max_length=8, blank=True, null=True)
    kd_pj = models.ForeignKey('Penjab', on_delete = models.CASCADE, db_column='kd_pj', blank=True, null=True)
    limit_reg = models.IntegerField(blank=True, null=True)
    waktu_kunjungan = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'booking_registrasi'
        unique_together = (('no_rkm_medis', 'tanggal_periksa'),)


class Bpjs(models.Model):
    stts = models.CharField(primary_key=True, max_length=5)
    biaya = models.FloatField()

    class Meta:
        managed = True
        db_table = 'bpjs'


class BpjsPrb(models.Model):
    no_sep = models.OneToOneField('BridgingSep', on_delete = models.CASCADE, db_column='no_sep', primary_key=True)
    prb = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bpjs_prb'


class BridgingDukcapil(models.Model):
    no_rkm_medis = models.OneToOneField('Pasien', on_delete = models.CASCADE, db_column='no_rkm_medis', primary_key=True)
    no_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bridging_dukcapil'


class BridgingInhealth(models.Model):
    no_sjp = models.CharField(primary_key=True, max_length=40)
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', blank=True, null=True)
    tglsep = models.DateTimeField(blank=True, null=True)
    tglrujukan = models.DateTimeField(blank=True, null=True)
    no_rujukan = models.CharField(max_length=30, blank=True, null=True)
    kdppkrujukan = models.CharField(max_length=12, blank=True, null=True)
    nmppkrujukan = models.CharField(max_length=200, blank=True, null=True)
    kdppkpelayanan = models.CharField(max_length=12, blank=True, null=True)
    nmppkpelayanan = models.CharField(max_length=200, blank=True, null=True)
    jnspelayanan = models.CharField(max_length=1, blank=True, null=True)
    catatan = models.CharField(max_length=100, blank=True, null=True)
    diagawal = models.CharField(max_length=10, blank=True, null=True)
    nmdiagnosaawal = models.CharField(max_length=100, blank=True, null=True)
    diagawal2 = models.CharField(max_length=10)
    nmdiagnosaawal2 = models.CharField(max_length=100)
    kdpolitujuan = models.CharField(max_length=5, blank=True, null=True)
    nmpolitujuan = models.CharField(max_length=50, blank=True, null=True)
    klsrawat = models.CharField(max_length=3, blank=True, null=True)
    klsdesc = models.CharField(max_length=50, blank=True, null=True)
    kdbu = models.CharField(max_length=12, blank=True, null=True)
    nmbu = models.CharField(max_length=200, blank=True, null=True)
    lakalantas = models.CharField(max_length=1, blank=True, null=True)
    lokasilaka = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=25, blank=True, null=True)
    nomr = models.CharField(max_length=15, blank=True, null=True)
    nama_pasien = models.CharField(max_length=100, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    jkel = models.CharField(max_length=9, blank=True, null=True)
    no_kartu = models.CharField(max_length=25, blank=True, null=True)
    tglpulang = models.DateTimeField(blank=True, null=True)
    plan = models.CharField(max_length=35)
    plandesc = models.CharField(max_length=100)
    idakomodasi = models.CharField(max_length=20, blank=True, null=True)
    tipesjp = models.CharField(max_length=35, blank=True, null=True)
    tipecob = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bridging_inhealth'


class BridgingRujukanBpjs(models.Model):
    no_sep = models.OneToOneField('BridgingSep', on_delete = models.CASCADE, db_column='no_sep', primary_key=True)
    tglrujukan = models.DateField(db_column='tglRujukan', blank=True, null=True)  # Field name made lowercase.
    ppkdirujuk = models.CharField(db_column='ppkDirujuk', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nm_ppkdirujuk = models.CharField(db_column='nm_ppkDirujuk', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jnspelayanan = models.CharField(db_column='jnsPelayanan', max_length=1, blank=True, null=True)  # Field name made lowercase.
    catatan = models.CharField(max_length=200, blank=True, null=True)
    diagrujukan = models.CharField(db_column='diagRujukan', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nama_diagrujukan = models.CharField(db_column='nama_diagRujukan', max_length=400, blank=True, null=True)  # Field name made lowercase.
    tiperujukan = models.CharField(db_column='tipeRujukan', max_length=14, blank=True, null=True)  # Field name made lowercase.
    polirujukan = models.CharField(db_column='poliRujukan', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nama_polirujukan = models.CharField(db_column='nama_poliRujukan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    no_rujukan = models.CharField(max_length=40, blank=True, null=True)
    user = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bridging_rujukan_bpjs'


class BridgingSep(models.Model):
    no_sep = models.CharField(primary_key=True, max_length=40)
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', blank=True, null=True)
    tglsep = models.DateField(blank=True, null=True)
    tglrujukan = models.DateField(blank=True, null=True)
    no_rujukan = models.CharField(max_length=40, blank=True, null=True)
    kdppkrujukan = models.CharField(max_length=12, blank=True, null=True)
    nmppkrujukan = models.CharField(max_length=200, blank=True, null=True)
    kdppkpelayanan = models.CharField(max_length=12, blank=True, null=True)
    nmppkpelayanan = models.CharField(max_length=200, blank=True, null=True)
    jnspelayanan = models.CharField(max_length=1, blank=True, null=True)
    catatan = models.CharField(max_length=100, blank=True, null=True)
    diagawal = models.CharField(max_length=10, blank=True, null=True)
    nmdiagnosaawal = models.CharField(max_length=400, blank=True, null=True)
    kdpolitujuan = models.CharField(max_length=15, blank=True, null=True)
    nmpolitujuan = models.CharField(max_length=50, blank=True, null=True)
    klsrawat = models.CharField(max_length=1, blank=True, null=True)
    lakalantas = models.CharField(max_length=1, blank=True, null=True)
    user = models.CharField(max_length=25, blank=True, null=True)
    nomr = models.CharField(max_length=15, blank=True, null=True)
    nama_pasien = models.CharField(max_length=100, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    peserta = models.CharField(max_length=100, blank=True, null=True)
    jkel = models.CharField(max_length=1, blank=True, null=True)
    no_kartu = models.CharField(max_length=25, blank=True, null=True)
    tglpulang = models.DateTimeField(blank=True, null=True)
    asal_rujukan = models.CharField(max_length=15)
    eksekutif = models.CharField(max_length=8)
    cob = models.CharField(max_length=8)
    penjamin = models.CharField(max_length=15)
    notelep = models.CharField(max_length=40)
    katarak = models.CharField(max_length=8)
    tglkkl = models.DateField()
    keterangankkl = models.CharField(max_length=100)
    suplesi = models.CharField(max_length=8)
    no_sep_suplesi = models.CharField(max_length=40)
    kdprop = models.CharField(max_length=10)
    nmprop = models.CharField(max_length=50)
    kdkab = models.CharField(max_length=10)
    nmkab = models.CharField(max_length=50)
    kdkec = models.CharField(max_length=10)
    nmkec = models.CharField(max_length=50)
    noskdp = models.CharField(max_length=6)
    kddpjp = models.CharField(max_length=10)
    nmdpdjp = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'bridging_sep'


class CacatFisik(models.Model):
    nama_cacat = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = True
        db_table = 'cacat_fisik'


class CatatanPasien(models.Model):
    no_rkm_medis = models.OneToOneField('Pasien', on_delete = models.CASCADE, db_column='no_rkm_medis', primary_key=True)
    catatan = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'catatan_pasien'


class CatatanPerawatan(models.Model):
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', blank=True, null=True)
    kd_dokter = models.ForeignKey('Dokter', on_delete = models.CASCADE, db_column='kd_dokter', blank=True, null=True)
    catatan = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'catatan_perawatan'


class ClosingKasir(models.Model):
    shift = models.CharField(primary_key=True, max_length=5)
    jam_masuk = models.TimeField()
    jam_pulang = models.TimeField()

    class Meta:
        managed = True
        db_table = 'closing_kasir'


class CssdBarang(models.Model):
    no_inventaris = models.OneToOneField('Inventaris', on_delete = models.CASCADE, db_column='no_inventaris', primary_key=True)
    jenis_barang = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cssd_barang'


class Dansos(models.Model):
    dana = models.FloatField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'dansos'


class DataBatch(models.Model):
    no_batch = models.CharField(primary_key=True, max_length=20)
    kode_brng = models.ForeignKey('Databarang', on_delete = models.CASCADE, db_column='kode_brng')
    tgl_beli = models.DateField()
    tgl_kadaluarsa = models.DateField()
    asal = models.CharField(max_length=10)
    no_faktur = models.CharField(max_length=20)
    dasar = models.FloatField()
    h_beli = models.FloatField(blank=True, null=True)
    ralan = models.FloatField(blank=True, null=True)
    kelas1 = models.FloatField(blank=True, null=True)
    kelas2 = models.FloatField(blank=True, null=True)
    kelas3 = models.FloatField(blank=True, null=True)
    utama = models.FloatField(blank=True, null=True)
    vip = models.FloatField(blank=True, null=True)
    vvip = models.FloatField(blank=True, null=True)
    beliluar = models.FloatField(blank=True, null=True)
    jualbebas = models.FloatField(blank=True, null=True)
    karyawan = models.FloatField(blank=True, null=True)
    jumlahbeli = models.FloatField()
    sisa = models.FloatField()

    class Meta:
        managed = True
        db_table = 'data_batch'
        unique_together = (('no_batch', 'kode_brng', 'no_faktur'),)


class DataHais(models.Model):
    tanggal = models.DateField(primary_key=True)
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    ett = models.IntegerField(db_column='ETT', blank=True, null=True)  # Field name made lowercase.
    cvl = models.IntegerField(db_column='CVL', blank=True, null=True)  # Field name made lowercase.
    ivl = models.IntegerField(db_column='IVL', blank=True, null=True)  # Field name made lowercase.
    uc = models.IntegerField(db_column='UC', blank=True, null=True)  # Field name made lowercase.
    vap = models.IntegerField(db_column='VAP', blank=True, null=True)  # Field name made lowercase.
    iad = models.IntegerField(db_column='IAD', blank=True, null=True)  # Field name made lowercase.
    pleb = models.IntegerField(db_column='PLEB', blank=True, null=True)  # Field name made lowercase.
    isk = models.IntegerField(db_column='ISK', blank=True, null=True)  # Field name made lowercase.
    ilo = models.IntegerField(db_column='ILO')  # Field name made lowercase.
    hap = models.IntegerField(db_column='HAP', blank=True, null=True)  # Field name made lowercase.
    tinea = models.IntegerField(db_column='Tinea', blank=True, null=True)  # Field name made lowercase.
    scabies = models.IntegerField(db_column='Scabies', blank=True, null=True)  # Field name made lowercase.
    deku = models.CharField(db_column='DEKU', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sputum = models.CharField(db_column='SPUTUM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    darah = models.CharField(db_column='DARAH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    urine = models.CharField(db_column='URINE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    antibiotik = models.CharField(db_column='ANTIBIOTIK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kd_kamar = models.ForeignKey('Kamar', on_delete = models.CASCADE, db_column='kd_kamar', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_hais'
        unique_together = (('tanggal', 'no_rawat'),)


class DataTb(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    id_tb_03 = models.CharField(max_length=30, blank=True, null=True)
    id_periode_laporan = models.CharField(max_length=20, blank=True, null=True)
    tanggal_buat_laporan = models.DateTimeField(blank=True, null=True)
    tahun_buat_laporan = models.TextField(blank=True, null=True)  # This field type is a guess.
    kd_wasor = models.IntegerField(blank=True, null=True)
    noregkab = models.IntegerField(blank=True, null=True)
    id_propinsi = models.CharField(max_length=15, blank=True, null=True)
    kd_kabupaten = models.CharField(max_length=15, blank=True, null=True)
    id_kecamatan = models.CharField(max_length=15, blank=True, null=True)
    id_kelurahan = models.CharField(max_length=15, blank=True, null=True)
    nama_rujukan = models.CharField(max_length=25, blank=True, null=True)
    sebutkan1 = models.CharField(max_length=100, blank=True, null=True)
    tipe_diagnosis = models.CharField(max_length=27, blank=True, null=True)
    klasifikasi_lokasi_anatomi = models.CharField(max_length=10, blank=True, null=True)
    klasifikasi_riwayat_pengobatan = models.CharField(max_length=45, blank=True, null=True)
    klasifikasi_status_hiv = models.CharField(max_length=15, blank=True, null=True)
    total_skoring_anak = models.CharField(max_length=15, blank=True, null=True)
    konfirmasiskoring5 = models.CharField(db_column='konfirmasiSkoring5', max_length=24, blank=True, null=True)  # Field name made lowercase.
    konfirmasiskoring6 = models.CharField(db_column='konfirmasiSkoring6', max_length=26, blank=True, null=True)  # Field name made lowercase.
    tanggal_mulai_pengobatan = models.DateField(blank=True, null=True)
    paduan_oat = models.CharField(max_length=500, blank=True, null=True)
    sumber_obat = models.CharField(max_length=13, blank=True, null=True)
    sebutkan = models.CharField(max_length=500, blank=True, null=True)
    sebelum_pengobatan_hasil_mikroskopis = models.CharField(max_length=15, blank=True, null=True)
    sebelum_pengobatan_hasil_tes_cepat = models.CharField(max_length=18, blank=True, null=True)
    sebelum_pengobatan_hasil_biakan = models.CharField(max_length=15, blank=True, null=True)
    noreglab_bulan_2 = models.CharField(max_length=15, blank=True, null=True)
    hasil_mikroskopis_bulan_2 = models.CharField(max_length=15, blank=True, null=True)
    noreglab_bulan_3 = models.CharField(max_length=15, blank=True, null=True)
    hasil_mikroskopis_bulan_3 = models.CharField(max_length=15, blank=True, null=True)
    noreglab_bulan_5 = models.CharField(max_length=15, blank=True, null=True)
    hasil_mikroskopis_bulan_5 = models.CharField(max_length=15, blank=True, null=True)
    akhir_pengobatan_noreglab = models.CharField(max_length=15, blank=True, null=True)
    akhir_pengobatan_hasil_mikroskopis = models.CharField(max_length=15, blank=True, null=True)
    tanggal_hasil_akhir_pengobatan = models.DateField(blank=True, null=True)
    hasil_akhir_pengobatan = models.CharField(max_length=18, blank=True, null=True)
    tanggal_dianjurkan_tes = models.DateField(blank=True, null=True)
    tanggal_tes_hiv = models.DateField(blank=True, null=True)
    hasil_tes_hiv = models.CharField(max_length=14, blank=True, null=True)
    ppk = models.CharField(max_length=5, blank=True, null=True)
    art = models.CharField(max_length=5, blank=True, null=True)
    tb_dm = models.CharField(max_length=5, blank=True, null=True)
    terapi_dm = models.CharField(max_length=12, blank=True, null=True)
    pindah_ro = models.CharField(max_length=5, blank=True, null=True)
    status_pengobatan = models.CharField(max_length=20, blank=True, null=True)
    foto_toraks = models.CharField(max_length=15, blank=True, null=True)
    toraks_tdk_dilakukan = models.CharField(max_length=112, blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    kode_icd_x = models.ForeignKey('Penyakit', on_delete = models.CASCADE, db_column='kode_icd_x', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_tb'


class DataTriaseIgd(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgl_kunjungan = models.DateTimeField()
    cara_masuk = models.CharField(max_length=10)
    alat_transportasi = models.CharField(max_length=7)
    alasan_kedatangan = models.CharField(max_length=14)
    keterangan_kedatangan = models.CharField(max_length=100)
    kode_kasus = models.ForeignKey('MasterTriaseMacamKasus', on_delete = models.CASCADE, db_column='kode_kasus')
    tekanan_darah = models.CharField(max_length=7)
    nadi = models.CharField(max_length=3)
    pernapasan = models.CharField(max_length=3)
    suhu = models.CharField(max_length=3)
    saturasi_o2 = models.CharField(max_length=3)
    nyeri = models.CharField(max_length=5)

    class Meta:
        managed = True
        db_table = 'data_triase_igd'


class DataTriaseIgddetailSkala1(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kode_skala1 = models.ForeignKey('MasterTriaseSkala1', on_delete = models.CASCADE, db_column='kode_skala1')

    class Meta:
        managed = True
        db_table = 'data_triase_igddetail_skala1'
        unique_together = (('no_rawat', 'kode_skala1'),)


class DataTriaseIgddetailSkala2(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kode_skala2 = models.ForeignKey('MasterTriaseSkala2', on_delete = models.CASCADE, db_column='kode_skala2')

    class Meta:
        managed = True
        db_table = 'data_triase_igddetail_skala2'
        unique_together = (('no_rawat', 'kode_skala2'),)


class DataTriaseIgddetailSkala3(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kode_skala3 = models.ForeignKey('MasterTriaseSkala3', on_delete = models.CASCADE, db_column='kode_skala3')

    class Meta:
        managed = True
        db_table = 'data_triase_igddetail_skala3'
        unique_together = (('no_rawat', 'kode_skala3'),)


class DataTriaseIgddetailSkala4(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kode_skala4 = models.ForeignKey('MasterTriaseSkala4', on_delete = models.CASCADE, db_column='kode_skala4')

    class Meta:
        managed = True
        db_table = 'data_triase_igddetail_skala4'
        unique_together = (('no_rawat', 'kode_skala4'),)


class DataTriaseIgddetailSkala5(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kode_skala5 = models.ForeignKey('MasterTriaseSkala5', on_delete = models.CASCADE, db_column='kode_skala5')

    class Meta:
        managed = True
        db_table = 'data_triase_igddetail_skala5'
        unique_together = (('no_rawat', 'kode_skala5'),)


class DataTriaseIgdprimer(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    keluhan_utama = models.CharField(max_length=400)
    kebutuhan_khusus = models.CharField(max_length=12)
    catatan = models.CharField(max_length=100)
    plan = models.CharField(max_length=16)
    tanggaltriase = models.DateTimeField()
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')

    class Meta:
        managed = True
        db_table = 'data_triase_igdprimer'


class DataTriaseIgdsekunder(models.Model):
    no_rawat = models.CharField(primary_key=True, max_length=17)
    anamnesa_singkat = models.CharField(max_length=400)
    catatan = models.CharField(max_length=100)
    plan = models.CharField(max_length=11)
    tanggaltriase = models.DateTimeField()
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')

    class Meta:
        managed = True
        db_table = 'data_triase_igdsekunder'


class Databarang(models.Model):
    kode_brng = models.CharField(primary_key=True, max_length=15)
    nama_brng = models.CharField(max_length=80, blank=True, null=True)
    kode_satbesar = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_satbesar')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat', blank=True, null=True)
    letak_barang = models.CharField(max_length=50, blank=True, null=True)
    dasar = models.FloatField()
    h_beli = models.FloatField(blank=True, null=True)
    ralan = models.FloatField(blank=True, null=True)
    kelas1 = models.FloatField(blank=True, null=True)
    kelas2 = models.FloatField(blank=True, null=True)
    kelas3 = models.FloatField(blank=True, null=True)
    utama = models.FloatField(blank=True, null=True)
    vip = models.FloatField(blank=True, null=True)
    vvip = models.FloatField(blank=True, null=True)
    beliluar = models.FloatField(blank=True, null=True)
    jualbebas = models.FloatField(blank=True, null=True)
    karyawan = models.FloatField(blank=True, null=True)
    stokminimal = models.FloatField(blank=True, null=True)
    kdjns = models.ForeignKey('Jenis', on_delete = models.CASCADE, db_column='kdjns', blank=True, null=True)
    isi = models.FloatField()
    kapasitas = models.FloatField()
    expire = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1)
    kode_industri = models.ForeignKey('Industrifarmasi', on_delete = models.CASCADE, db_column='kode_industri', blank=True, null=True)
    kode_kategori = models.ForeignKey('KategoriBarang', on_delete = models.CASCADE, db_column='kode_kategori', blank=True, null=True)
    kode_golongan = models.ForeignKey('GolonganBarang', on_delete = models.CASCADE, db_column='kode_golongan', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'databarang'


class Datasuplier(models.Model):
    kode_suplier = models.CharField(primary_key=True, max_length=5)
    nama_suplier = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=20, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    nama_bank = models.CharField(max_length=30, blank=True, null=True)
    rekening = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'datasuplier'


class Departemen(models.Model):
    dep_id = models.CharField(primary_key=True, max_length=4)
    nama = models.CharField(max_length=25)

    class Meta:
        managed = True
        db_table = 'departemen'


class Deposit(models.Model):
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    tgl_deposit = models.DateTimeField()
    besar_deposit = models.FloatField(blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')

    class Meta:
        managed = True
        db_table = 'deposit'


class DetailBeriDiet(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kd_kamar = models.ForeignKey('Kamar', on_delete = models.CASCADE, db_column='kd_kamar')
    tanggal = models.DateField()
    waktu = models.CharField(max_length=5)
    kd_diet = models.ForeignKey('Diet', on_delete = models.CASCADE, db_column='kd_diet')

    class Meta:
        managed = True
        db_table = 'detail_beri_diet'
        unique_together = (('no_rawat', 'kd_kamar', 'tanggal', 'waktu', 'kd_diet'),)


class DetailNotaInap(models.Model):
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', blank=True, null=True)
    nama_bayar = models.ForeignKey(AkunBayar, on_delete = models.CASCADE, db_column='nama_bayar', blank=True, null=True)
    besarppn = models.FloatField(blank=True, null=True)
    besar_bayar = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detail_nota_inap'


class DetailNotaJalan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    nama_bayar = models.ForeignKey(AkunBayar, on_delete = models.CASCADE, db_column='nama_bayar')
    besarppn = models.FloatField(blank=True, null=True)
    besar_bayar = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detail_nota_jalan'
        unique_together = (('no_rawat', 'nama_bayar'),)


class DetailObatRacikan(models.Model):
    tgl_perawatan = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    no_racik = models.CharField(max_length=2)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')

    class Meta:
        managed = True
        db_table = 'detail_obat_racikan'
        unique_together = (('tgl_perawatan', 'jam', 'no_rawat', 'no_racik', 'kode_brng'),)


class DetailObatRacikanJual(models.Model):
    nota_jual = models.OneToOneField('Penjualan', on_delete = models.CASCADE, db_column='nota_jual', primary_key=True)
    no_racik = models.CharField(max_length=2)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')

    class Meta:
        managed = True
        db_table = 'detail_obat_racikan_jual'
        unique_together = (('nota_jual', 'no_racik', 'kode_brng'),)


class DetailPemberianObat(models.Model):
    tgl_perawatan = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    h_beli = models.FloatField(blank=True, null=True)
    biaya_obat = models.FloatField(blank=True, null=True)
    jml = models.FloatField()
    embalase = models.FloatField(blank=True, null=True)
    tuslah = models.FloatField(blank=True, null=True)
    total = models.FloatField()
    status = models.CharField(max_length=5, blank=True, null=True)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal', blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'detail_pemberian_obat'
        unique_together = (('tgl_perawatan', 'jam', 'no_rawat', 'kode_brng', 'no_batch', 'no_faktur'),)


class DetailPengajuanBarangMedis(models.Model):
    no_pengajuan = models.ForeignKey('PengajuanBarangMedis', on_delete = models.CASCADE, db_column='no_pengajuan')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pengajuan = models.FloatField(blank=True, null=True)
    total = models.FloatField()
    jumlah2 = models.FloatField()

    class Meta:
        managed = True
        db_table = 'detail_pengajuan_barang_medis'


class DetailPengajuanBarangNonmedis(models.Model):
    no_pengajuan = models.ForeignKey('PengajuanBarangNonmedis', on_delete = models.CASCADE, db_column='no_pengajuan')
    kode_brng = models.ForeignKey('Ipsrsbarang', on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pengajuan = models.FloatField(blank=True, null=True)
    total = models.FloatField()

    class Meta:
        managed = True
        db_table = 'detail_pengajuan_barang_nonmedis'


class DetailPengeluaranObatBhp(models.Model):
    no_keluar = models.ForeignKey('PengeluaranObatBhp', on_delete = models.CASCADE, db_column='no_keluar')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat')
    no_batch = models.CharField(max_length=20, blank=True, null=True)
    jumlah = models.FloatField()
    harga_beli = models.FloatField()
    total = models.FloatField()
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'detail_pengeluaran_obat_bhp'


class DetailPeriksaLab(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey('JnsPerawatanLab', on_delete = models.CASCADE, db_column='kd_jenis_prw')
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    id_template = models.ForeignKey('TemplateLaboratorium', on_delete = models.CASCADE, db_column='id_template')
    nilai = models.CharField(max_length=60)
    nilai_rujukan = models.CharField(max_length=30)
    keterangan = models.CharField(max_length=60)
    bagian_rs = models.FloatField()
    bhp = models.FloatField()
    bagian_perujuk = models.FloatField()
    bagian_dokter = models.FloatField()
    bagian_laborat = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_item = models.FloatField()

    class Meta:
        managed = True
        db_table = 'detail_periksa_lab'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'tgl_periksa', 'jam', 'id_template'),)


class DetailPermintaanMedis(models.Model):
    no_permintaan = models.ForeignKey('PermintaanMedis', on_delete = models.CASCADE, db_column='no_permintaan', blank=True, null=True)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng', blank=True, null=True)
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detail_permintaan_medis'


class DetailPermintaanNonMedis(models.Model):
    no_permintaan = models.ForeignKey('PermintaanNonMedis', on_delete = models.CASCADE, db_column='no_permintaan', blank=True, null=True)
    kode_brng = models.ForeignKey('Ipsrsbarang', on_delete = models.CASCADE, db_column='kode_brng', blank=True, null=True)
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detail_permintaan_non_medis'


class DetailPiutangPasien(models.Model):
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', blank=True, null=True)
    nama_bayar = models.ForeignKey(AkunPiutang, on_delete = models.CASCADE, db_column='nama_bayar', blank=True, null=True)
    kd_pj = models.ForeignKey('Penjab', on_delete = models.CASCADE, db_column='kd_pj', blank=True, null=True)
    totalpiutang = models.FloatField(blank=True, null=True)
    sisapiutang = models.FloatField(blank=True, null=True)
    tgltempo = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detail_piutang_pasien'


class DetailSuratPemesananMedis(models.Model):
    no_pemesanan = models.ForeignKey('SuratPemesananMedis', on_delete = models.CASCADE, db_column='no_pemesanan')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pesan = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()
    jumlah2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detail_surat_pemesanan_medis'


class DetailSuratPemesananNonMedis(models.Model):
    no_pemesanan = models.ForeignKey('SuratPemesananNonMedis', on_delete = models.CASCADE, db_column='no_pemesanan')
    kode_brng = models.ForeignKey('Ipsrsbarang', on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pesan = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = True
        db_table = 'detail_surat_pemesanan_non_medis'


class Detailbeli(models.Model):
    no_faktur = models.ForeignKey('Pembelian', on_delete = models.CASCADE, db_column='no_faktur')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()
    no_batch = models.CharField(max_length=20)
    jumlah2 = models.FloatField(blank=True, null=True)
    kadaluarsa = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detailbeli'


class DetailhibahObatBhp(models.Model):
    no_hibah = models.ForeignKey('HibahObatBhp', on_delete = models.CASCADE, db_column='no_hibah')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_hibah = models.FloatField(blank=True, null=True)
    subtotalhibah = models.FloatField(blank=True, null=True)
    h_diakui = models.FloatField()
    subtotaldiakui = models.FloatField()
    no_batch = models.CharField(max_length=20)
    jumlah2 = models.FloatField(blank=True, null=True)
    kadaluarsa = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detailhibah_obat_bhp'


class Detailjual(models.Model):
    nota_jual = models.ForeignKey('Penjualan', on_delete = models.CASCADE, db_column='nota_jual')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.CharField(max_length=4, blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField(blank=True, null=True)
    bsr_dis = models.FloatField(blank=True, null=True)
    tambahan = models.FloatField(blank=True, null=True)
    embalase = models.FloatField()
    tuslah = models.FloatField()
    aturan_pakai = models.CharField(max_length=150)
    total = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'detailjual'


class Detailjurnal(models.Model):
    no_jurnal = models.ForeignKey('Jurnal', on_delete = models.CASCADE, db_column='no_jurnal', blank=True, null=True)
    kd_rek = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='kd_rek', blank=True, null=True)
    debet = models.FloatField(blank=True, null=True)
    kredit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detailjurnal'


class Detailpesan(models.Model):
    no_faktur = models.ForeignKey('Pemesanan', on_delete = models.CASCADE, db_column='no_faktur')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pesan = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()
    no_batch = models.CharField(max_length=20)
    jumlah2 = models.FloatField(blank=True, null=True)
    kadaluarsa = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detailpesan'


class Detailpiutang(models.Model):
    nota_piutang = models.ForeignKey('Piutang', on_delete = models.CASCADE, db_column='nota_piutang')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.CharField(max_length=4, blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField(blank=True, null=True)
    bsr_dis = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)
    aturan_pakai = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'detailpiutang'


class Detreturbeli(models.Model):
    no_retur_beli = models.ForeignKey('Returbeli', on_delete = models.CASCADE, db_column='no_retur_beli')
    no_faktur = models.CharField(max_length=20)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.CharField(max_length=4, blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jml_beli = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    jml_retur2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detreturbeli'


class Detreturjual(models.Model):
    no_retur_jual = models.ForeignKey('Returjual', on_delete = models.CASCADE, db_column='no_retur_jual')
    nota_jual = models.CharField(max_length=20)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.CharField(max_length=4, blank=True, null=True)
    jml_jual = models.FloatField(blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'detreturjual'


class Detreturpiutang(models.Model):
    no_retur_piutang = models.ForeignKey('Returpiutang', on_delete = models.CASCADE, db_column='no_retur_piutang')
    nota_piutang = models.CharField(max_length=20)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.CharField(max_length=4, blank=True, null=True)
    jml_piutang = models.FloatField(blank=True, null=True)
    h_piutang = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'detreturpiutang'


class DiagnosaPasien(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kd_penyakit = models.ForeignKey('Penyakit', on_delete = models.CASCADE, db_column='kd_penyakit')
    status = models.CharField(max_length=5)
    prioritas = models.IntegerField()
    status_penyakit = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'diagnosa_pasien'
        unique_together = (('no_rawat', 'kd_penyakit', 'status'),)


class Diet(models.Model):
    kd_diet = models.CharField(primary_key=True, max_length=3)
    nama_diet = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'diet'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete = models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete = models.CASCADE)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class Dokter(models.Model):
    kd_dokter = models.OneToOneField('Pegawai', on_delete = models.CASCADE, db_column='kd_dokter', primary_key=True)
    nm_dokter = models.CharField(max_length=50, blank=True, null=True)
    jk = models.CharField(max_length=1, blank=True, null=True)
    tmp_lahir = models.CharField(max_length=20, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    gol_drh = models.CharField(max_length=2, blank=True, null=True)
    agama = models.CharField(max_length=12, blank=True, null=True)
    almt_tgl = models.CharField(max_length=60, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    stts_nikah = models.CharField(max_length=7, blank=True, null=True)
    kd_sps = models.ForeignKey('Spesialis', on_delete = models.CASCADE, db_column='kd_sps', blank=True, null=True)
    alumni = models.CharField(max_length=60, blank=True, null=True)
    no_ijn_praktek = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'dokter'


class DpjpRanap(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')

    class Meta:
        managed = True
        db_table = 'dpjp_ranap'
        unique_together = (('no_rawat', 'kd_dokter'),)


class EmergencyIndex(models.Model):
    kode_emergency = models.CharField(primary_key=True, max_length=3)
    nama_emergency = models.CharField(max_length=200, blank=True, null=True)
    indek = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'emergency_index'


class EvaluasiKinerja(models.Model):
    kode_evaluasi = models.CharField(primary_key=True, max_length=3)
    nama_evaluasi = models.CharField(max_length=200, blank=True, null=True)
    indek = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'evaluasi_kinerja'


class EvaluasiKinerjaPegawai(models.Model):
    id = models.OneToOneField('Pegawai', on_delete = models.CASCADE, db_column='id', primary_key=True)
    kode_evaluasi = models.ForeignKey(EvaluasiKinerja, on_delete = models.CASCADE, db_column='kode_evaluasi')
    tahun = models.TextField()  # This field type is a guess.
    bulan = models.IntegerField()
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'evaluasi_kinerja_pegawai'
        unique_together = (('id', 'kode_evaluasi', 'tahun', 'bulan'),)


class Gambar(models.Model):
    inde = models.IntegerField(primary_key=True)
    bpjs = models.TextField()

    class Meta:
        managed = True
        db_table = 'gambar'


class GambarRadiologi(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    lokasi_gambar = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'gambar_radiologi'
        unique_together = (('no_rawat', 'tgl_periksa', 'jam', 'lokasi_gambar'),)


class GolonganBarang(models.Model):
    kode = models.CharField(primary_key=True, max_length=4)
    nama = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'golongan_barang'


class GolonganPolri(models.Model):
    nama_golongan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'golongan_polri'


class GolonganTni(models.Model):
    nama_golongan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'golongan_tni'


class Gudangbarang(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')
    stok = models.FloatField()
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'gudangbarang'
        unique_together = (('kode_brng', 'kd_bangsal', 'no_batch', 'no_faktur'),)


class HarianKurangiBulanan(models.Model):
    harian = models.IntegerField()
    bulanan = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'harian_kurangi_bulanan'


class HasilRadiologi(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    hasil = models.TextField()

    class Meta:
        managed = True
        db_table = 'hasil_radiologi'
        unique_together = (('no_rawat', 'tgl_periksa', 'jam'),)


class Hemodialisa(models.Model):
    tanggal = models.DateTimeField(primary_key=True)
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    kd_penyakit = models.ForeignKey('Penyakit', on_delete = models.CASCADE, db_column='kd_penyakit')
    lama = models.IntegerField()
    dialist = models.CharField(max_length=30)
    penarikan = models.FloatField()
    akses = models.CharField(max_length=30)
    transfusi = models.FloatField()
    ureum = models.CharField(max_length=10)
    hb = models.CharField(max_length=10)
    hsbag = models.CharField(max_length=10)
    creatinin = models.CharField(max_length=10)
    gds = models.CharField(max_length=10)
    ctbt = models.CharField(max_length=10)
    lain = models.CharField(max_length=200)
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')

    class Meta:
        managed = True
        db_table = 'hemodialisa'
        unique_together = (('tanggal', 'no_rawat'),)


class HibahObatBhp(models.Model):
    no_hibah = models.CharField(primary_key=True, max_length=20)
    kode_pemberi = models.ForeignKey('Pemberihibah', on_delete = models.CASCADE, db_column='kode_pemberi', blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    tgl_hibah = models.DateField(blank=True, null=True)
    totalhibah = models.FloatField()
    totalnilai = models.FloatField()
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')

    class Meta:
        managed = True
        db_table = 'hibah_obat_bhp'


class Icd9(models.Model):
    kode = models.CharField(primary_key=True, max_length=8)
    deskripsi_panjang = models.CharField(max_length=250, blank=True, null=True)
    deskripsi_pendek = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'icd9'


class InacbgCoderNik(models.Model):
    nik = models.OneToOneField('Pegawai', on_delete = models.CASCADE, db_column='nik', primary_key=True)
    no_ik = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inacbg_coder_nik'


class InacbgDataTerkirim(models.Model):
    no_sep = models.OneToOneField(BridgingSep, on_delete = models.CASCADE, db_column='no_sep', primary_key=True)
    nik = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inacbg_data_terkirim'


class InacbgDataTerkirim2(models.Model):
    no_sep = models.OneToOneField('InacbgKlaimBaru2', on_delete = models.CASCADE, db_column='no_sep', primary_key=True)
    nik = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inacbg_data_terkirim2'


class InacbgGroupingStage1(models.Model):
    no_sep = models.OneToOneField(BridgingSep, on_delete = models.CASCADE, db_column='no_sep', primary_key=True)
    code_cbg = models.CharField(max_length=10, blank=True, null=True)
    deskripsi = models.CharField(max_length=200, blank=True, null=True)
    tarif = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inacbg_grouping_stage1'


class InacbgGroupingStage12(models.Model):
    no_sep = models.OneToOneField('InacbgKlaimBaru2', on_delete = models.CASCADE, db_column='no_sep', primary_key=True)
    code_cbg = models.CharField(max_length=10, blank=True, null=True)
    deskripsi = models.CharField(max_length=200, blank=True, null=True)
    tarif = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inacbg_grouping_stage12'


class InacbgKlaimBaru(models.Model):
    no_sep = models.OneToOneField(BridgingSep, on_delete = models.CASCADE, db_column='no_sep', primary_key=True)
    patient_id = models.CharField(max_length=30, blank=True, null=True)
    admission_id = models.CharField(max_length=30, blank=True, null=True)
    hospital_admission_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inacbg_klaim_baru'


class InacbgKlaimBaru2(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    no_sep = models.CharField(unique=True, max_length=40)
    patient_id = models.CharField(max_length=30, blank=True, null=True)
    admission_id = models.CharField(max_length=30, blank=True, null=True)
    hospital_admission_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inacbg_klaim_baru2'


class Indekref(models.Model):
    kdindex = models.ForeignKey(Departemen, on_delete = models.CASCADE, db_column='kdindex')
    n = models.FloatField()
    ttl = models.FloatField()

    class Meta:
        managed = True
        db_table = 'indekref'


class Indexins(models.Model):
    dep = models.OneToOneField(Departemen, on_delete = models.CASCADE, primary_key=True)
    persen = models.FloatField()

    class Meta:
        managed = True
        db_table = 'indexins'


class Indextotal(models.Model):
    kdindex = models.ForeignKey(Departemen, on_delete = models.CASCADE, db_column='kdindex')
    ttl = models.FloatField()

    class Meta:
        managed = True
        db_table = 'indextotal'


class Industrifarmasi(models.Model):
    kode_industri = models.CharField(primary_key=True, max_length=5)
    nama_industri = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=20, blank=True, null=True)
    no_telp = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'industrifarmasi'


class InhealthJenpelRuangRawat(models.Model):
    kd_kamar = models.OneToOneField('Kamar', on_delete = models.CASCADE, db_column='kd_kamar', primary_key=True)
    kode_jenpel_ruang_rawat = models.CharField(max_length=20)
    nama_jenpel_ruang_rawat = models.CharField(max_length=100, blank=True, null=True)
    tarif = models.FloatField()

    class Meta:
        managed = True
        db_table = 'inhealth_jenpel_ruang_rawat'


class InhealthMapingDokter(models.Model):
    kd_dokter = models.OneToOneField(Dokter, on_delete = models.CASCADE, db_column='kd_dokter', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inhealth_maping_dokter'


class InhealthMapingPoli(models.Model):
    kd_poli_rs = models.OneToOneField('Poliklinik', on_delete = models.CASCADE, db_column='kd_poli_rs', primary_key=True)
    kd_poli_inhealth = models.CharField(max_length=15, blank=True, null=True)
    nm_poli_inhealth = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inhealth_maping_poli'


class InhealthTindakanLaborat(models.Model):
    kd_jenis_prw = models.OneToOneField('JnsPerawatanLab', on_delete = models.CASCADE, db_column='kd_jenis_prw', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inhealth_tindakan_laborat'


class InhealthTindakanOperasi(models.Model):
    kode_paket = models.OneToOneField('PaketOperasi', on_delete = models.CASCADE, db_column='kode_paket', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inhealth_tindakan_operasi'


class InhealthTindakanRadiologi(models.Model):
    kd_jenis_prw = models.OneToOneField('JnsPerawatanRadiologi', on_delete = models.CASCADE, db_column='kd_jenis_prw', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inhealth_tindakan_radiologi'


class InhealthTindakanRalan(models.Model):
    kd_jenis_prw = models.OneToOneField('JnsPerawatan', on_delete = models.CASCADE, db_column='kd_jenis_prw', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inhealth_tindakan_ralan'


class InhealthTindakanRanap(models.Model):
    kd_jenis_prw = models.OneToOneField('JnsPerawatanInap', on_delete = models.CASCADE, db_column='kd_jenis_prw', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inhealth_tindakan_ranap'


class InsidenKeselamatan(models.Model):
    kode_insiden = models.CharField(primary_key=True, max_length=5)
    nama_insiden = models.CharField(max_length=100)
    jenis_insiden = models.CharField(max_length=8)
    dampak = models.CharField(max_length=19)

    class Meta:
        managed = True
        db_table = 'insiden_keselamatan'


class InsidenKeselamatanPasien(models.Model):
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    tgl_kejadian = models.DateField()
    jam_kejadian = models.TimeField()
    tgl_lapor = models.DateField()
    jam_lapor = models.TimeField()
    kode_insiden = models.ForeignKey(InsidenKeselamatan, on_delete = models.CASCADE, db_column='kode_insiden')
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')
    lokasi = models.CharField(max_length=60)
    kronologis = models.CharField(max_length=200)
    unit_terkait = models.CharField(max_length=60)
    akibat = models.CharField(max_length=150)
    tindakan_insiden = models.CharField(max_length=150)
    identifikasi_masalah = models.CharField(max_length=150)
    rtl = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'insiden_keselamatan_pasien'


class Inventaris(models.Model):
    no_inventaris = models.CharField(primary_key=True, max_length=30)
    kode_barang = models.ForeignKey('InventarisBarang', on_delete = models.CASCADE, db_column='kode_barang', blank=True, null=True)
    asal_barang = models.CharField(max_length=7, blank=True, null=True)
    tgl_pengadaan = models.DateField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    status_barang = models.CharField(max_length=9, blank=True, null=True)
    id_ruang = models.ForeignKey('InventarisRuang', on_delete = models.CASCADE, db_column='id_ruang', blank=True, null=True)
    no_rak = models.CharField(max_length=3, blank=True, null=True)
    no_box = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inventaris'


class InventarisBarang(models.Model):
    kode_barang = models.CharField(primary_key=True, max_length=20)
    nama_barang = models.CharField(max_length=60, blank=True, null=True)
    jml_barang = models.IntegerField(blank=True, null=True)
    kode_produsen = models.ForeignKey('InventarisProdusen', on_delete = models.CASCADE, db_column='kode_produsen', blank=True, null=True)
    id_merk = models.ForeignKey('InventarisMerk', on_delete = models.CASCADE, db_column='id_merk', blank=True, null=True)
    thn_produksi = models.TextField(blank=True, null=True)  # This field type is a guess.
    isbn = models.CharField(max_length=20, blank=True, null=True)
    id_kategori = models.ForeignKey('InventarisKategori', on_delete = models.CASCADE, db_column='id_kategori', blank=True, null=True)
    id_jenis = models.ForeignKey('InventarisJenis', on_delete = models.CASCADE, db_column='id_jenis', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inventaris_barang'


class InventarisJenis(models.Model):
    id_jenis = models.CharField(primary_key=True, max_length=10)
    nama_jenis = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inventaris_jenis'


class InventarisKategori(models.Model):
    id_kategori = models.CharField(primary_key=True, max_length=10)
    nama_kategori = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inventaris_kategori'


class InventarisMerk(models.Model):
    id_merk = models.CharField(primary_key=True, max_length=10)
    nama_merk = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'inventaris_merk'


class InventarisPeminjaman(models.Model):
    peminjam = models.CharField(primary_key=True, max_length=50)
    tlp = models.CharField(max_length=13)
    no_inventaris = models.ForeignKey(Inventaris, on_delete = models.CASCADE, db_column='no_inventaris')
    tgl_pinjam = models.DateField()
    tgl_kembali = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')
    status_pinjam = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inventaris_peminjaman'
        unique_together = (('peminjam', 'no_inventaris', 'tgl_pinjam', 'nip'),)


class InventarisProdusen(models.Model):
    kode_produsen = models.CharField(primary_key=True, max_length=10)
    nama_produsen = models.CharField(max_length=40, blank=True, null=True)
    alamat_produsen = models.CharField(max_length=70, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    website_produsen = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'inventaris_produsen'


class InventarisRuang(models.Model):
    id_ruang = models.CharField(primary_key=True, max_length=5)
    nama_ruang = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'inventaris_ruang'


class Ipsrsbarang(models.Model):
    kode_brng = models.CharField(primary_key=True, max_length=15)
    nama_brng = models.CharField(max_length=80)
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat')
    jenis = models.ForeignKey('Ipsrsjenisbarang', on_delete = models.CASCADE, db_column='jenis', blank=True, null=True)
    stok = models.FloatField()
    harga = models.FloatField()
    status = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'ipsrsbarang'


class Ipsrsdetailbeli(models.Model):
    no_faktur = models.ForeignKey('Ipsrspembelian', on_delete = models.CASCADE, db_column='no_faktur')
    kode_brng = models.ForeignKey(Ipsrsbarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat')
    jumlah = models.FloatField()
    harga = models.FloatField()
    subtotal = models.FloatField()
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = True
        db_table = 'ipsrsdetailbeli'


class Ipsrsdetailpengeluaran(models.Model):
    no_keluar = models.ForeignKey('Ipsrspengeluaran', on_delete = models.CASCADE, db_column='no_keluar')
    kode_brng = models.ForeignKey(Ipsrsbarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat')
    jumlah = models.FloatField()
    harga = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = True
        db_table = 'ipsrsdetailpengeluaran'


class Ipsrsdetailpesan(models.Model):
    no_faktur = models.ForeignKey('Ipsrspemesanan', on_delete = models.CASCADE, db_column='no_faktur')
    kode_brng = models.ForeignKey(Ipsrsbarang, on_delete = models.CASCADE, db_column='kode_brng')
    kode_sat = models.ForeignKey('Kodesatuan', on_delete = models.CASCADE, db_column='kode_sat')
    jumlah = models.FloatField()
    harga = models.FloatField()
    subtotal = models.FloatField()
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = True
        db_table = 'ipsrsdetailpesan'


class Ipsrsjenisbarang(models.Model):
    kd_jenis = models.CharField(primary_key=True, max_length=5)
    nm_jenis = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ipsrsjenisbarang'


class Ipsrsopname(models.Model):
    kode_brng = models.ForeignKey(Ipsrsbarang, on_delete = models.CASCADE, db_column='kode_brng')
    h_beli = models.FloatField(blank=True, null=True)
    tanggal = models.DateField()
    stok = models.IntegerField()
    real = models.IntegerField()
    selisih = models.IntegerField()
    nomihilang = models.FloatField()
    keterangan = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'ipsrsopname'


class Ipsrspembelian(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=15)
    kode_suplier = models.ForeignKey('Ipsrssuplier', on_delete = models.CASCADE, db_column='kode_suplier')
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')
    tgl_beli = models.DateField()
    subtotal = models.FloatField()
    potongan = models.FloatField()
    total = models.FloatField()
    ppn = models.FloatField(blank=True, null=True)
    meterai = models.FloatField(blank=True, null=True)
    tagihan = models.FloatField(blank=True, null=True)
    kd_rek = models.ForeignKey(AkunBayar, on_delete = models.CASCADE, db_column='kd_rek', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ipsrspembelian'


class Ipsrspemesanan(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=20)
    no_order = models.CharField(max_length=20)
    kode_suplier = models.ForeignKey('Ipsrssuplier', on_delete = models.CASCADE, db_column='kode_suplier', blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    tgl_pesan = models.DateField(blank=True, null=True)
    tgl_faktur = models.DateField(blank=True, null=True)
    tgl_tempo = models.DateField(blank=True, null=True)
    total1 = models.FloatField()
    potongan = models.FloatField()
    total2 = models.FloatField()
    ppn = models.FloatField()
    meterai = models.FloatField(blank=True, null=True)
    tagihan = models.FloatField()
    status = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ipsrspemesanan'


class Ipsrspengeluaran(models.Model):
    no_keluar = models.CharField(primary_key=True, max_length=15)
    tanggal = models.DateField()
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')
    keterangan = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'ipsrspengeluaran'


class Ipsrssuplier(models.Model):
    kode_suplier = models.CharField(primary_key=True, max_length=5)
    nama_suplier = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=20, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    nama_bank = models.CharField(max_length=30, blank=True, null=True)
    rekening = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ipsrssuplier'


class Jabatan(models.Model):
    kd_jbtn = models.CharField(primary_key=True, max_length=4)
    nm_jbtn = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jabatan'


class JabatanPolri(models.Model):
    nama_jabatan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jabatan_polri'


class JabatanTni(models.Model):
    nama_jabatan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jabatan_tni'


class Jadwal(models.Model):
    kd_dokter = models.OneToOneField(Dokter, on_delete = models.CASCADE, db_column='kd_dokter', primary_key=True)
    hari_kerja = models.CharField(max_length=6)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField(blank=True, null=True)
    kd_poli = models.ForeignKey('Poliklinik', on_delete = models.CASCADE, db_column='kd_poli', blank=True, null=True)
    kuota = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jadwal'
        unique_together = (('kd_dokter', 'hari_kerja'),)


class JadwalPegawai(models.Model):
    id = models.OneToOneField('Pegawai', on_delete = models.CASCADE, db_column='id', primary_key=True)
    tahun = models.TextField()  # This field type is a guess.
    bulan = models.CharField(max_length=2)
    h1 = models.CharField(max_length=13)
    h2 = models.CharField(max_length=13)
    h3 = models.CharField(max_length=13)
    h4 = models.CharField(max_length=13)
    h5 = models.CharField(max_length=13)
    h6 = models.CharField(max_length=13)
    h7 = models.CharField(max_length=13)
    h8 = models.CharField(max_length=13)
    h9 = models.CharField(max_length=13)
    h10 = models.CharField(max_length=13)
    h11 = models.CharField(max_length=13)
    h12 = models.CharField(max_length=13)
    h13 = models.CharField(max_length=13)
    h14 = models.CharField(max_length=13)
    h15 = models.CharField(max_length=13)
    h16 = models.CharField(max_length=13)
    h17 = models.CharField(max_length=13)
    h18 = models.CharField(max_length=13)
    h19 = models.CharField(max_length=13)
    h20 = models.CharField(max_length=13)
    h21 = models.CharField(max_length=13)
    h22 = models.CharField(max_length=13)
    h23 = models.CharField(max_length=13)
    h24 = models.CharField(max_length=13)
    h25 = models.CharField(max_length=13)
    h26 = models.CharField(max_length=13)
    h27 = models.CharField(max_length=13)
    h28 = models.CharField(max_length=13)
    h29 = models.CharField(max_length=13)
    h30 = models.CharField(max_length=13)
    h31 = models.CharField(max_length=13)

    class Meta:
        managed = True
        db_table = 'jadwal_pegawai'
        unique_together = (('id', 'tahun', 'bulan'),)


class JadwalTambahan(models.Model):
    id = models.OneToOneField('Pegawai', on_delete = models.CASCADE, db_column='id', primary_key=True)
    tahun = models.TextField()  # This field type is a guess.
    bulan = models.CharField(max_length=2)
    h1 = models.CharField(max_length=13)
    h2 = models.CharField(max_length=13)
    h3 = models.CharField(max_length=13)
    h4 = models.CharField(max_length=13)
    h5 = models.CharField(max_length=13)
    h6 = models.CharField(max_length=13)
    h7 = models.CharField(max_length=13)
    h8 = models.CharField(max_length=13)
    h9 = models.CharField(max_length=13)
    h10 = models.CharField(max_length=13)
    h11 = models.CharField(max_length=13)
    h12 = models.CharField(max_length=13)
    h13 = models.CharField(max_length=13)
    h14 = models.CharField(max_length=13)
    h15 = models.CharField(max_length=13)
    h16 = models.CharField(max_length=13)
    h17 = models.CharField(max_length=13)
    h18 = models.CharField(max_length=13)
    h19 = models.CharField(max_length=13)
    h20 = models.CharField(max_length=13)
    h21 = models.CharField(max_length=13)
    h22 = models.CharField(max_length=13)
    h23 = models.CharField(max_length=13)
    h24 = models.CharField(max_length=13)
    h25 = models.CharField(max_length=13)
    h26 = models.CharField(max_length=13)
    h27 = models.CharField(max_length=13)
    h28 = models.CharField(max_length=13)
    h29 = models.CharField(max_length=13)
    h30 = models.CharField(max_length=13)
    h31 = models.CharField(max_length=13)

    class Meta:
        managed = True
        db_table = 'jadwal_tambahan'
        unique_together = (('id', 'tahun', 'bulan'),)


class JamJaga(models.Model):
    no_id = models.AutoField(primary_key=True)
    dep = models.ForeignKey(Departemen, on_delete = models.CASCADE)
    shift = models.CharField(max_length=13)
    jam_masuk = models.TimeField()
    jam_pulang = models.TimeField()

    class Meta:
        managed = True
        db_table = 'jam_jaga'
        unique_together = (('dep', 'shift'),)


class JamMasuk(models.Model):
    shift = models.CharField(primary_key=True, max_length=13)
    jam_masuk = models.TimeField()
    jam_pulang = models.TimeField()

    class Meta:
        managed = True
        db_table = 'jam_masuk'


class Jamsostek(models.Model):
    stts = models.CharField(primary_key=True, max_length=5)
    biaya = models.FloatField()

    class Meta:
        managed = True
        db_table = 'jamsostek'


class JasaLain(models.Model):
    thn = models.TextField(primary_key=True)  # This field type is a guess.
    bln = models.IntegerField()
    id = models.ForeignKey('Pegawai', on_delete = models.CASCADE, db_column='id')
    bsr_jasa = models.FloatField()
    ktg = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'jasa_lain'
        unique_together = (('thn', 'bln', 'id', 'bsr_jasa', 'ktg'),)


class Jenis(models.Model):
    kdjns = models.CharField(primary_key=True, max_length=4)
    nama = models.CharField(max_length=30)
    keterangan = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'jenis'


class Jgmlm(models.Model):
    tgl = models.DateField(primary_key=True)
    id = models.ForeignKey('Pegawai', on_delete = models.CASCADE, db_column='id')
    jml = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'jgmlm'
        unique_together = (('tgl', 'id'),)


class JnjJabatan(models.Model):
    kode = models.CharField(primary_key=True, max_length=10)
    nama = models.CharField(max_length=50)
    tnj = models.FloatField()
    indek = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'jnj_jabatan'


class JnsPerawatan(models.Model):
    kd_jenis_prw = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80, blank=True, null=True)
    kd_kategori = models.ForeignKey('KategoriPerawatan', on_delete = models.CASCADE, db_column='kd_kategori', blank=True, null=True)
    material = models.FloatField(blank=True, null=True)
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField(blank=True, null=True)
    tarif_tindakanpr = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    total_byrdr = models.FloatField(blank=True, null=True)
    total_byrpr = models.FloatField(blank=True, null=True)
    total_byrdrpr = models.FloatField()
    kd_pj = models.ForeignKey('Penjab', on_delete = models.CASCADE, db_column='kd_pj')
    kd_poli = models.ForeignKey('Poliklinik', on_delete = models.CASCADE, db_column='kd_poli')
    status = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'jns_perawatan'


class JnsPerawatanInap(models.Model):
    kd_jenis_prw = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80, blank=True, null=True)
    kd_kategori = models.ForeignKey('KategoriPerawatan', on_delete = models.CASCADE, db_column='kd_kategori')
    material = models.FloatField(blank=True, null=True)
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField(blank=True, null=True)
    tarif_tindakanpr = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    total_byrdr = models.FloatField(blank=True, null=True)
    total_byrpr = models.FloatField(blank=True, null=True)
    total_byrdrpr = models.FloatField()
    kd_pj = models.ForeignKey('Penjab', on_delete = models.CASCADE, db_column='kd_pj')
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')
    status = models.CharField(max_length=1)
    kelas = models.CharField(max_length=11)

    class Meta:
        managed = True
        db_table = 'jns_perawatan_inap'


class JnsPerawatanLab(models.Model):
    kd_jenis_prw = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80, blank=True, null=True)
    bagian_rs = models.FloatField(blank=True, null=True)
    bhp = models.FloatField()
    tarif_perujuk = models.FloatField()
    tarif_tindakan_dokter = models.FloatField()
    tarif_tindakan_petugas = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    total_byr = models.FloatField(blank=True, null=True)
    kd_pj = models.ForeignKey('Penjab', on_delete = models.CASCADE, db_column='kd_pj')
    status = models.CharField(max_length=1)
    kelas = models.CharField(max_length=11)

    class Meta:
        managed = True
        db_table = 'jns_perawatan_lab'


class JnsPerawatanRadiologi(models.Model):
    kd_jenis_prw = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80, blank=True, null=True)
    bagian_rs = models.FloatField(blank=True, null=True)
    bhp = models.FloatField()
    tarif_perujuk = models.FloatField()
    tarif_tindakan_dokter = models.FloatField()
    tarif_tindakan_petugas = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    total_byr = models.FloatField(blank=True, null=True)
    kd_pj = models.ForeignKey('Penjab', on_delete = models.CASCADE, db_column='kd_pj')
    status = models.CharField(max_length=1)
    kelas = models.CharField(max_length=11)

    class Meta:
        managed = True
        db_table = 'jns_perawatan_radiologi'


class JnsPerawatanUtd(models.Model):
    kd_jenis_prw = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80, blank=True, null=True)
    bagian_rs = models.FloatField(blank=True, null=True)
    bhp = models.FloatField(blank=True, null=True)
    tarif_perujuk = models.FloatField(blank=True, null=True)
    tarif_tindakan_dokter = models.FloatField(blank=True, null=True)
    tarif_tindakan_petugas = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    manajemen = models.FloatField(blank=True, null=True)
    total_byr = models.FloatField(blank=True, null=True)
    kd_pj = models.ForeignKey('Penjab', on_delete = models.CASCADE, db_column='kd_pj', blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jns_perawatan_utd'


class Jumpasien(models.Model):
    thn = models.TextField(primary_key=True)  # This field type is a guess.
    bln = models.IntegerField()
    id = models.ForeignKey('Pegawai', on_delete = models.CASCADE, db_column='id')
    jml = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'jumpasien'
        unique_together = (('thn', 'bln', 'id'),)


class Jurnal(models.Model):
    no_jurnal = models.CharField(primary_key=True, max_length=20)
    no_bukti = models.CharField(max_length=20, blank=True, null=True)
    tgl_jurnal = models.DateField(blank=True, null=True)
    jenis = models.CharField(max_length=1, blank=True, null=True)
    keterangan = models.CharField(max_length=350, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jurnal'


class K3RsBagianTubuh(models.Model):
    kode_bagian = models.CharField(primary_key=True, max_length=5)
    bagian_tubuh = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'k3rs_bagian_tubuh'


class K3RsDampakCidera(models.Model):
    kode_dampak = models.CharField(primary_key=True, max_length=5)
    dampak_cidera = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'k3rs_dampak_cidera'


class K3RsJenisCidera(models.Model):
    kode_cidera = models.CharField(primary_key=True, max_length=5)
    jenis_cidera = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'k3rs_jenis_cidera'


class K3RsJenisLuka(models.Model):
    kode_luka = models.CharField(primary_key=True, max_length=5)
    jenis_luka = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'k3rs_jenis_luka'


class K3RsJenisPekerjaan(models.Model):
    kode_pekerjaan = models.CharField(primary_key=True, max_length=5)
    jenis_pekerjaan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'k3rs_jenis_pekerjaan'


class K3RsLokasiKejadian(models.Model):
    kode_lokasi = models.CharField(primary_key=True, max_length=5)
    lokasi_kejadian = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'k3rs_lokasi_kejadian'


class K3RsPenyebab(models.Model):
    kode_penyebab = models.CharField(primary_key=True, max_length=5)
    penyebab_kecelakaan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'k3rs_penyebab'


class K3RsPeristiwa(models.Model):
    no_k3rs = models.CharField(primary_key=True, max_length=20)
    tgl_insiden = models.DateField()
    waktu_insiden = models.TimeField()
    kode_pekerjaan = models.ForeignKey(K3RsJenisPekerjaan, on_delete = models.CASCADE, db_column='kode_pekerjaan')
    tgl_pelaporan = models.DateField()
    waktu_pelaporan = models.TimeField()
    kode_lokasi = models.ForeignKey(K3RsLokasiKejadian, on_delete = models.CASCADE, db_column='kode_lokasi')
    kronologi_kejadian = models.CharField(max_length=300)
    kode_penyebab = models.ForeignKey(K3RsPenyebab, on_delete = models.CASCADE, db_column='kode_penyebab')
    nik = models.ForeignKey('Pegawai', on_delete = models.CASCADE, db_column='nik')
    kategori_cidera = models.CharField(max_length=6)
    kode_cidera = models.ForeignKey(K3RsJenisCidera, on_delete = models.CASCADE, db_column='kode_cidera')
    kode_luka = models.ForeignKey(K3RsJenisLuka, on_delete = models.CASCADE, db_column='kode_luka')
    kode_bagian = models.ForeignKey(K3RsBagianTubuh, on_delete = models.CASCADE, db_column='kode_bagian')
    lt = models.IntegerField()
    penyebab_langsung_kondisi = models.CharField(max_length=100)
    penyebab_langsung_tindakan = models.CharField(max_length=100)
    penyebab_tidak_langsung_pribadi = models.CharField(max_length=100)
    penyebab_tidak_langsung_pekerjaan = models.CharField(max_length=100)
    barang_bukti = models.CharField(max_length=5)
    kode_dampak = models.ForeignKey(K3RsDampakCidera, on_delete = models.CASCADE, db_column='kode_dampak')
    nik_pelapor = models.ForeignKey('Pegawai', on_delete = models.CASCADE, db_column='nik_pelapor')
    perbaikan_jenis_tindakan = models.CharField(max_length=19)
    perbaikan_rencana_tindakan = models.CharField(max_length=200)
    perbaikan_target = models.DateField()
    perbaikan_wewenang = models.CharField(max_length=100)
    nik_timk3 = models.ForeignKey('Pegawai', on_delete = models.CASCADE, db_column='nik_timk3')
    catatan = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'k3rs_peristiwa'


class Kabupaten(models.Model):
    kd_kab = models.AutoField(primary_key=True)
    nm_kab = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = True
        db_table = 'kabupaten'


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


class KamarInap(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kd_kamar = models.ForeignKey(Kamar, on_delete = models.CASCADE, db_column='kd_kamar')
    trf_kamar = models.FloatField(blank=True, null=True)
    diagnosa_awal = models.CharField(max_length=100, blank=True, null=True)
    diagnosa_akhir = models.CharField(max_length=100, blank=True, null=True)
    tgl_masuk = models.DateField()
    jam_masuk = models.TimeField()
    tgl_keluar = models.DateField(blank=True, null=True)
    jam_keluar = models.TimeField(blank=True, null=True)
    lama = models.FloatField(blank=True, null=True)
    ttl_biaya = models.FloatField(blank=True, null=True)
    stts_pulang = models.CharField(max_length=23)

    class Meta:
        managed = True
        db_table = 'kamar_inap'
        unique_together = (('no_rawat', 'tgl_masuk', 'jam_masuk'),)


class Kasift(models.Model):
    id = models.OneToOneField('Pegawai', on_delete = models.CASCADE, db_column='id', primary_key=True)
    jmlks = models.BigIntegerField()
    bsr = models.FloatField()

    class Meta:
        managed = True
        db_table = 'kasift'


class KategoriBarang(models.Model):
    kode = models.CharField(primary_key=True, max_length=4)
    nama = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kategori_barang'


class KategoriPemasukanLain(models.Model):
    kode_kategori = models.CharField(primary_key=True, max_length=5)
    nama_kategori = models.CharField(max_length=40, blank=True, null=True)
    kd_rek = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='kd_rek', blank=True, null=True)
    kd_rek2 = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='kd_rek2', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kategori_pemasukan_lain'


class KategoriPengeluaranHarian(models.Model):
    kode_kategori = models.CharField(primary_key=True, max_length=5)
    nama_kategori = models.CharField(max_length=40, blank=True, null=True)
    kd_rek = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='kd_rek', blank=True, null=True)
    kd_rek2 = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='kd_rek2', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kategori_pengeluaran_harian'


class KategoriPenyakit(models.Model):
    kd_ktg = models.CharField(primary_key=True, max_length=8)
    nm_kategori = models.CharField(max_length=30, blank=True, null=True)
    ciri_umum = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kategori_penyakit'


class KategoriPerawatan(models.Model):
    kd_kategori = models.CharField(primary_key=True, max_length=5)
    nm_kategori = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kategori_perawatan'


class Keanggotaan(models.Model):
    id = models.OneToOneField('Pegawai', on_delete = models.CASCADE, db_column='id', primary_key=True)
    koperasi = models.ForeignKey('Koperasi', on_delete = models.CASCADE, db_column='koperasi')
    jamsostek = models.ForeignKey(Jamsostek, on_delete = models.CASCADE, db_column='jamsostek')
    bpjs = models.ForeignKey(Bpjs, on_delete = models.CASCADE, db_column='bpjs')

    class Meta:
        managed = True
        db_table = 'keanggotaan'


class Kecamatan(models.Model):
    kd_kec = models.AutoField(primary_key=True)
    nm_kec = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = True
        db_table = 'kecamatan'


class KelompokJabatan(models.Model):
    kode_kelompok = models.CharField(primary_key=True, max_length=3)
    nama_kelompok = models.CharField(max_length=100, blank=True, null=True)
    indek = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kelompok_jabatan'


class Kelurahan(models.Model):
    kd_kel = models.AutoField(primary_key=True)
    nm_kel = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = True
        db_table = 'kelurahan'


class KeslingLimbahB3Medis(models.Model):
    nip = models.OneToOneField('Petugas', on_delete = models.CASCADE, db_column='nip', primary_key=True)
    tanggal = models.DateTimeField()
    jmllimbah = models.FloatField(blank=True, null=True)
    tujuan_penyerahan = models.CharField(max_length=50, blank=True, null=True)
    bukti_dokumen = models.CharField(max_length=20, blank=True, null=True)
    sisa_di_tps = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kesling_limbah_b3medis'
        unique_together = (('nip', 'tanggal'),)


class KeslingLimbahDomestik(models.Model):
    nip = models.OneToOneField('Petugas', on_delete = models.CASCADE, db_column='nip', primary_key=True)
    tanggal = models.DateTimeField()
    jumlahlimbah = models.FloatField(blank=True, null=True)
    tanggalangkut = models.DateTimeField(blank=True, null=True)
    keterangan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kesling_limbah_domestik'
        unique_together = (('nip', 'tanggal'),)


class KeslingMutuAirLimbah(models.Model):
    nip = models.OneToOneField('Petugas', on_delete = models.CASCADE, db_column='nip', primary_key=True)
    tanggal = models.DateTimeField()
    meteran = models.FloatField(blank=True, null=True)
    jumlahharian = models.FloatField(blank=True, null=True)
    ph = models.FloatField(blank=True, null=True)
    suhu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kesling_mutu_air_limbah'
        unique_together = (('nip', 'tanggal'),)


class KeslingPemakaianAirPdam(models.Model):
    nip = models.OneToOneField('Petugas', on_delete = models.CASCADE, db_column='nip', primary_key=True)
    tanggal = models.DateTimeField()
    meteran = models.FloatField(blank=True, null=True)
    jumlahharian = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kesling_pemakaian_air_pdam'
        unique_together = (('nip', 'tanggal'),)


class KeslingPestControl(models.Model):
    nip = models.OneToOneField('Petugas', on_delete = models.CASCADE, db_column='nip', primary_key=True)
    tanggal = models.DateTimeField()
    rincian_kegiatan = models.TextField(blank=True, null=True)
    rekomendasi = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kesling_pest_control'
        unique_together = (('nip', 'tanggal'),)


class Ketidakhadiran(models.Model):
    tgl = models.DateField(primary_key=True)
    id = models.ForeignKey('Pegawai', on_delete = models.CASCADE, db_column='id')
    jns = models.CharField(max_length=1)
    ktg = models.CharField(max_length=40)
    jml = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ketidakhadiran'
        unique_together = (('tgl', 'id', 'jns'),)


class Kodesatuan(models.Model):
    kode_sat = models.CharField(primary_key=True, max_length=4)
    satuan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'kodesatuan'


class KonverSat(models.Model):
    nilai = models.FloatField(primary_key=True)
    kode_sat = models.ForeignKey(Kodesatuan, on_delete = models.CASCADE, db_column='kode_sat')
    nilai_konversi = models.FloatField()
    sat_konversi = models.CharField(max_length=4)

    class Meta:
        managed = True
        db_table = 'konver_sat'
        unique_together = (('nilai', 'kode_sat', 'nilai_konversi', 'sat_konversi'),)


class Koperasi(models.Model):
    stts = models.CharField(primary_key=True, max_length=5)
    wajib = models.FloatField()

    class Meta:
        managed = True
        db_table = 'koperasi'


class LaporanOperasi(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    diagnosa_preop = models.CharField(max_length=100)
    diagnosa_postop = models.CharField(max_length=100)
    jaringan_dieksekusi = models.CharField(max_length=100)
    selesaioperasi = models.DateTimeField()
    permintaan_pa = models.CharField(max_length=5)
    laporan_operasi = models.TextField()

    class Meta:
        managed = True
        db_table = 'laporan_operasi'
        unique_together = (('no_rawat', 'tanggal'),)


class LogDukcapilAceh(models.Model):
    no_ktp = models.CharField(primary_key=True, max_length=20)
    tanggal = models.DateTimeField()
    user = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'log_dukcapil_aceh'
        unique_together = (('no_ktp', 'tanggal', 'user'),)


class MapingDokterDpjpvclaim(models.Model):
    kd_dokter = models.OneToOneField(Dokter, on_delete = models.CASCADE, db_column='kd_dokter', primary_key=True)
    kd_dokter_bpjs = models.CharField(max_length=20, blank=True, null=True)
    nm_dokter_bpjs = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maping_dokter_dpjpvclaim'


class MapingDokterPcare(models.Model):
    kd_dokter = models.OneToOneField(Dokter, on_delete = models.CASCADE, db_column='kd_dokter', primary_key=True)
    kd_dokter_pcare = models.CharField(max_length=20, blank=True, null=True)
    nm_dokter_pcare = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maping_dokter_pcare'


class MapingObatPcare(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    kode_brng_pcare = models.CharField(max_length=15)
    nama_brng_pcare = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maping_obat_pcare'


class MapingPoliBpjs(models.Model):
    kd_poli_rs = models.OneToOneField('Poliklinik', on_delete = models.CASCADE, db_column='kd_poli_rs', primary_key=True)
    kd_poli_bpjs = models.CharField(max_length=15)
    nm_poli_bpjs = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'maping_poli_bpjs'


class MapingPoliklinikPcare(models.Model):
    kd_poli_rs = models.OneToOneField('Poliklinik', on_delete = models.CASCADE, db_column='kd_poli_rs', primary_key=True)
    kd_poli_pcare = models.CharField(max_length=5, blank=True, null=True)
    nm_poli_pcare = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maping_poliklinik_pcare'


class MapingTindakanPcare(models.Model):
    kd_jenis_prw = models.OneToOneField(JnsPerawatan, on_delete = models.CASCADE, db_column='kd_jenis_prw', primary_key=True)
    kd_tindakan_pcare = models.CharField(max_length=15, blank=True, null=True)
    nm_tindakan_pcare = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maping_tindakan_pcare'


class MapingTindakanRanapPcare(models.Model):
    kd_jenis_prw = models.OneToOneField(JnsPerawatanInap, on_delete = models.CASCADE, db_column='kd_jenis_prw', primary_key=True)
    kd_tindakan_pcare = models.CharField(max_length=15, blank=True, null=True)
    nm_tindakan_pcare = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'maping_tindakan_ranap_pcare'


class MasterAturanPakai(models.Model):
    aturan = models.CharField(primary_key=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'master_aturan_pakai'


class MasterBerkasDigital(models.Model):
    kode = models.CharField(primary_key=True, max_length=10)
    nama = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'master_berkas_digital'


class MasterBerkasPegawai(models.Model):
    kode = models.CharField(primary_key=True, max_length=10)
    kategori = models.CharField(max_length=31)
    nama_berkas = models.CharField(max_length=300)
    no_urut = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'master_berkas_pegawai'


class MasterTindakan(models.Model):
    nama = models.CharField(unique=True, max_length=50)
    jm = models.FloatField()
    jns = models.CharField(max_length=12)

    class Meta:
        managed = True
        db_table = 'master_tindakan'


class MasterTriaseMacamKasus(models.Model):
    kode_kasus = models.CharField(primary_key=True, max_length=3)
    macam_kasus = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'master_triase_macam_kasus'


class MasterTriasePemeriksaan(models.Model):
    kode_pemeriksaan = models.CharField(primary_key=True, max_length=3)
    nama_pemeriksaan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'master_triase_pemeriksaan'


class MasterTriaseSkala1(models.Model):
    kode_pemeriksaan = models.ForeignKey(MasterTriasePemeriksaan, on_delete = models.CASCADE, db_column='kode_pemeriksaan')
    kode_skala1 = models.CharField(primary_key=True, max_length=3)
    pengkajian_skala1 = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'master_triase_skala1'


class MasterTriaseSkala2(models.Model):
    kode_pemeriksaan = models.ForeignKey(MasterTriasePemeriksaan, on_delete = models.CASCADE, db_column='kode_pemeriksaan')
    kode_skala2 = models.CharField(primary_key=True, max_length=3)
    pengkajian_skala2 = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'master_triase_skala2'


class MasterTriaseSkala3(models.Model):
    kode_pemeriksaan = models.ForeignKey(MasterTriasePemeriksaan, on_delete = models.CASCADE, db_column='kode_pemeriksaan')
    kode_skala3 = models.CharField(primary_key=True, max_length=3)
    pengkajian_skala3 = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'master_triase_skala3'


class MasterTriaseSkala4(models.Model):
    kode_pemeriksaan = models.ForeignKey(MasterTriasePemeriksaan, on_delete = models.CASCADE, db_column='kode_pemeriksaan')
    kode_skala4 = models.CharField(primary_key=True, max_length=3)
    pengkajian_skala4 = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'master_triase_skala4'


class MasterTriaseSkala5(models.Model):
    kode_pemeriksaan = models.ForeignKey(MasterTriasePemeriksaan, on_delete = models.CASCADE, db_column='kode_pemeriksaan')
    kode_skala5 = models.CharField(primary_key=True, max_length=3)
    pengkajian_skala5 = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'master_triase_skala5'


class MasterTunjanganBulanan(models.Model):
    nama = models.CharField(max_length=60)
    tnj = models.FloatField()

    class Meta:
        managed = True
        db_table = 'master_tunjangan_bulanan'


class MasterTunjanganHarian(models.Model):
    nama = models.CharField(max_length=40)
    tnj = models.FloatField()

    class Meta:
        managed = True
        db_table = 'master_tunjangan_harian'


class MatrikAkunJnsPerawatan(models.Model):
    kd_jenis_prw = models.OneToOneField(JnsPerawatan, on_delete = models.CASCADE, db_column='kd_jenis_prw', primary_key=True)
    pendapatan_tindakan = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='pendapatan_tindakan', blank=True, null=True)
    beban_jasa_dokter = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='beban_jasa_dokter', blank=True, null=True)
    utang_jasa_dokter = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='utang_jasa_dokter', blank=True, null=True)
    beban_jasa_paramedis = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='beban_jasa_paramedis', blank=True, null=True)
    utang_jasa_paramedis = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='utang_jasa_paramedis', blank=True, null=True)
    beban_kso = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='beban_kso', blank=True, null=True)
    utang_kso = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='utang_kso', blank=True, null=True)
    hpp_persediaan = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='hpp_persediaan', blank=True, null=True)
    persediaan_bhp = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='persediaan_bhp', blank=True, null=True)
    beban_jasa_sarana = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='beban_jasa_sarana', blank=True, null=True)
    utang_jasa_sarana = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='utang_jasa_sarana', blank=True, null=True)
    beban_menejemen = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='beban_menejemen', blank=True, null=True)
    utang_menejemen = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='utang_menejemen', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'matrik_akun_jns_perawatan'


class MatrikAkunJnsPerawatanInap(models.Model):
    kd_jenis_prw = models.OneToOneField(JnsPerawatanInap, on_delete = models.CASCADE, db_column='kd_jenis_prw', primary_key=True)
    pendapatan_tindakan = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='pendapatan_tindakan', blank=True, null=True)
    beban_jasa_dokter = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='beban_jasa_dokter', blank=True, null=True)
    utang_jasa_dokter = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='utang_jasa_dokter', blank=True, null=True)
    beban_jasa_paramedis = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='beban_jasa_paramedis', blank=True, null=True)
    utang_jasa_paramedis = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='utang_jasa_paramedis', blank=True, null=True)
    beban_kso = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='beban_kso', blank=True, null=True)
    utang_kso = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='utang_kso', blank=True, null=True)
    hpp_persediaan = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='hpp_persediaan', blank=True, null=True)
    persediaan_bhp = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='persediaan_bhp', blank=True, null=True)
    beban_jasa_sarana = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='beban_jasa_sarana', blank=True, null=True)
    utang_jasa_sarana = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='utang_jasa_sarana', blank=True, null=True)
    beban_menejemen = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='beban_menejemen', blank=True, null=True)
    utang_menejemen = models.ForeignKey('Rekening', on_delete = models.CASCADE, db_column='utang_menejemen', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'matrik_akun_jns_perawatan_inap'


class MetodeRacik(models.Model):
    kd_racik = models.CharField(primary_key=True, max_length=3)
    nm_racik = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'metode_racik'


class MonitoringAsuhanGizi(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    monitoring = models.CharField(max_length=200, blank=True, null=True)
    evaluasi = models.CharField(max_length=200, blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'monitoring_asuhan_gizi'
        unique_together = (('no_rawat', 'tanggal'),)


class MutasiBerkas(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    status = models.CharField(max_length=14, blank=True, null=True)
    dikirim = models.DateTimeField(blank=True, null=True)
    diterima = models.DateTimeField(blank=True, null=True)
    kembali = models.DateTimeField(blank=True, null=True)
    tidakada = models.DateTimeField(blank=True, null=True)
    ranap = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'mutasi_berkas'


class Mutasibarang(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    jml = models.FloatField()
    harga = models.FloatField()
    kd_bangsaldari = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsaldari')
    kd_bangsalke = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsalke')
    tanggal = models.DateTimeField()
    keterangan = models.CharField(max_length=60)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'mutasibarang'
        unique_together = (('kode_brng', 'kd_bangsaldari', 'kd_bangsalke', 'tanggal', 'no_batch', 'no_faktur'),)


class NotaInap(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    no_nota = models.CharField(unique=True, max_length=17, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)
    uang_muka = models.FloatField(db_column='Uang_Muka', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'nota_inap'


class NotaJalan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    no_nota = models.CharField(unique=True, max_length=17, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)
    jasa_medik_dokter_tindakan_ralan = models.FloatField(db_column='Jasa_Medik_Dokter_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    jasa_medik_paramedis_tindakan_ralan = models.FloatField(db_column='Jasa_Medik_Paramedis_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    kso_tindakan_ralan = models.FloatField(db_column='KSO_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    jasa_medik_dokter_laborat_ralan = models.FloatField(db_column='Jasa_Medik_Dokter_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    jasa_medik_petugas_laborat_ralan = models.FloatField(db_column='Jasa_Medik_Petugas_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    kso_laborat_ralan = models.FloatField(db_column='Kso_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    persediaan_laborat_rawat_jalan = models.FloatField(db_column='Persediaan_Laborat_Rawat_Jalan', blank=True, null=True)  # Field name made lowercase.
    jasa_medik_dokter_radiologi_ralan = models.FloatField(db_column='Jasa_Medik_Dokter_Radiologi_Ralan', blank=True, null=True)  # Field name made lowercase.
    jasa_medik_petugas_radiologi_ralan = models.FloatField(db_column='Jasa_Medik_Petugas_Radiologi_Ralan', blank=True, null=True)  # Field name made lowercase.
    kso_radiologi_ralan = models.FloatField(db_column='Kso_Radiologi_Ralan', blank=True, null=True)  # Field name made lowercase.
    persediaan_radiologi_rawat_jalan = models.FloatField(db_column='Persediaan_Radiologi_Rawat_Jalan', blank=True, null=True)  # Field name made lowercase.
    obat_rawat_jalan = models.FloatField(db_column='Obat_Rawat_Jalan', blank=True, null=True)  # Field name made lowercase.
    jasa_medik_dokter_operasi_ralan = models.FloatField(db_column='Jasa_Medik_Dokter_Operasi_Ralan', blank=True, null=True)  # Field name made lowercase.
    jasa_medik_paramedis_operasi_ralan = models.FloatField(db_column='Jasa_Medik_Paramedis_Operasi_Ralan', blank=True, null=True)  # Field name made lowercase.
    obat_operasi_ralan = models.FloatField(db_column='Obat_Operasi_Ralan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'nota_jalan'


class ObatPenyakit(models.Model):
    kd_penyakit = models.OneToOneField('Penyakit', on_delete = models.CASCADE, db_column='kd_penyakit', primary_key=True)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    referensi = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'obat_penyakit'
        unique_together = (('kd_penyakit', 'kode_brng'),)


class ObatRacikan(models.Model):
    tgl_perawatan = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    no_racik = models.CharField(max_length=2)
    nama_racik = models.CharField(max_length=100)
    kd_racik = models.ForeignKey(MetodeRacik, on_delete = models.CASCADE, db_column='kd_racik')
    jml_dr = models.IntegerField()
    aturan_pakai = models.CharField(max_length=150)
    keterangan = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'obat_racikan'
        unique_together = (('tgl_perawatan', 'jam', 'no_rawat', 'no_racik'),)


class ObatRacikanJual(models.Model):
    nota_jual = models.OneToOneField('Penjualan', on_delete = models.CASCADE, db_column='nota_jual', primary_key=True)
    no_racik = models.CharField(max_length=2)
    nama_racik = models.CharField(max_length=100)
    kd_racik = models.ForeignKey(MetodeRacik, on_delete = models.CASCADE, db_column='kd_racik')
    jml_dr = models.IntegerField()
    aturan_pakai = models.CharField(max_length=150)
    keterangan = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'obat_racikan_jual'
        unique_together = (('nota_jual', 'no_racik'),)


class ObatbhpOk(models.Model):
    kd_obat = models.CharField(primary_key=True, max_length=15)
    nm_obat = models.CharField(max_length=50)
    kode_sat = models.ForeignKey(Kodesatuan, on_delete = models.CASCADE, db_column='kode_sat')
    hargasatuan = models.FloatField()

    class Meta:
        managed = True
        db_table = 'obatbhp_ok'


class Operasi(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgl_operasi = models.DateTimeField()
    jenis_anasthesi = models.CharField(max_length=8)
    kategori = models.CharField(max_length=9, blank=True, null=True)
    operator1 = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='operator1')
    operator2 = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='operator2')
    operator3 = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='operator3')
    asisten_operator1 = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='asisten_operator1')
    asisten_operator2 = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='asisten_operator2')
    asisten_operator3 = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='asisten_operator3', blank=True, null=True)
    instrumen = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='instrumen', blank=True, null=True)
    dokter_anak = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='dokter_anak')
    perawaat_resusitas = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='perawaat_resusitas')
    dokter_anestesi = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='dokter_anestesi')
    asisten_anestesi = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='asisten_anestesi')
    asisten_anestesi2 = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='asisten_anestesi2', blank=True, null=True)
    bidan = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='bidan')
    bidan2 = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='bidan2', blank=True, null=True)
    bidan3 = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='bidan3', blank=True, null=True)
    perawat_luar = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='perawat_luar')
    omloop = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='omloop', blank=True, null=True)
    omloop2 = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='omloop2', blank=True, null=True)
    omloop3 = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='omloop3', blank=True, null=True)
    omloop4 = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='omloop4', blank=True, null=True)
    omloop5 = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='omloop5', blank=True, null=True)
    dokter_pjanak = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='dokter_pjanak', blank=True, null=True)
    dokter_umum = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='dokter_umum', blank=True, null=True)
    kode_paket = models.ForeignKey('PaketOperasi', on_delete = models.CASCADE, db_column='kode_paket')
    biayaoperator1 = models.FloatField()
    biayaoperator2 = models.FloatField()
    biayaoperator3 = models.FloatField()
    biayaasisten_operator1 = models.FloatField()
    biayaasisten_operator2 = models.FloatField()
    biayaasisten_operator3 = models.FloatField(blank=True, null=True)
    biayainstrumen = models.FloatField(blank=True, null=True)
    biayadokter_anak = models.FloatField()
    biayaperawaat_resusitas = models.FloatField()
    biayadokter_anestesi = models.FloatField()
    biayaasisten_anestesi = models.FloatField()
    biayaasisten_anestesi2 = models.FloatField(blank=True, null=True)
    biayabidan = models.FloatField()
    biayabidan2 = models.FloatField(blank=True, null=True)
    biayabidan3 = models.FloatField(blank=True, null=True)
    biayaperawat_luar = models.FloatField()
    biayaalat = models.FloatField()
    biayasewaok = models.FloatField()
    akomodasi = models.FloatField(blank=True, null=True)
    bagian_rs = models.FloatField()
    biaya_omloop = models.FloatField(blank=True, null=True)
    biaya_omloop2 = models.FloatField(blank=True, null=True)
    biaya_omloop3 = models.FloatField(blank=True, null=True)
    biaya_omloop4 = models.FloatField(blank=True, null=True)
    biaya_omloop5 = models.FloatField(blank=True, null=True)
    biayasarpras = models.FloatField(blank=True, null=True)
    biaya_dokter_pjanak = models.FloatField(blank=True, null=True)
    biaya_dokter_umum = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'operasi'
        unique_together = (('no_rawat', 'tgl_operasi', 'kode_paket'),)


class Opname(models.Model):
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    h_beli = models.FloatField(blank=True, null=True)
    tanggal = models.DateField()
    stok = models.FloatField()
    real = models.FloatField()
    selisih = models.FloatField()
    nomihilang = models.FloatField()
    lebih = models.FloatField()
    nomilebih = models.FloatField()
    keterangan = models.CharField(max_length=60)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'opname'


class PaketOperasi(models.Model):
    kode_paket = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80)
    kategori = models.CharField(max_length=9, blank=True, null=True)
    operator1 = models.FloatField()
    operator2 = models.FloatField()
    operator3 = models.FloatField()
    asisten_operator1 = models.FloatField(blank=True, null=True)
    asisten_operator2 = models.FloatField()
    asisten_operator3 = models.FloatField(blank=True, null=True)
    instrumen = models.FloatField(blank=True, null=True)
    dokter_anak = models.FloatField()
    perawaat_resusitas = models.FloatField()
    dokter_anestesi = models.FloatField()
    asisten_anestesi = models.FloatField()
    asisten_anestesi2 = models.FloatField(blank=True, null=True)
    bidan = models.FloatField()
    bidan2 = models.FloatField(blank=True, null=True)
    bidan3 = models.FloatField(blank=True, null=True)
    perawat_luar = models.FloatField()
    sewa_ok = models.FloatField()
    alat = models.FloatField()
    akomodasi = models.FloatField(blank=True, null=True)
    bagian_rs = models.FloatField()
    omloop = models.FloatField()
    omloop2 = models.FloatField(blank=True, null=True)
    omloop3 = models.FloatField(blank=True, null=True)
    omloop4 = models.FloatField(blank=True, null=True)
    omloop5 = models.FloatField(blank=True, null=True)
    sarpras = models.FloatField(blank=True, null=True)
    dokter_pjanak = models.FloatField(blank=True, null=True)
    dokter_umum = models.FloatField(blank=True, null=True)
    kd_pj = models.ForeignKey('Penjab', on_delete = models.CASCADE, db_column='kd_pj', blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    kelas = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'paket_operasi'


class PangkatPolri(models.Model):
    nama_pangkat = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pangkat_polri'


class PangkatTni(models.Model):
    nama_pangkat = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pangkat_tni'


class Parkir(models.Model):
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    nomer_kartu = models.CharField(max_length=5, blank=True, null=True)
    kd_parkir = models.ForeignKey('ParkirJenis', on_delete = models.CASCADE, db_column='kd_parkir', blank=True, null=True)
    no_kendaraan = models.CharField(primary_key=True, max_length=15)
    tgl_masuk = models.DateField()
    jam_masuk = models.TimeField()
    tgl_keluar = models.DateField(blank=True, null=True)
    jam_keluar = models.TimeField(blank=True, null=True)
    lama_parkir = models.IntegerField(blank=True, null=True)
    ttl_biaya = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'parkir'
        unique_together = (('no_kendaraan', 'tgl_masuk', 'jam_masuk'),)


class ParkirBarcode(models.Model):
    kode_barcode = models.CharField(primary_key=True, max_length=15)
    nomer_kartu = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = True
        db_table = 'parkir_barcode'


class ParkirJenis(models.Model):
    kd_parkir = models.CharField(primary_key=True, max_length=5)
    jns_parkir = models.CharField(max_length=50)
    biaya = models.FloatField()
    jenis = models.CharField(max_length=6)

    class Meta:
        managed = True
        db_table = 'parkir_jenis'


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


class PasienBayi(models.Model):
    no_rkm_medis = models.OneToOneField(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis', primary_key=True)
    umur_ibu = models.CharField(max_length=8)
    nama_ayah = models.CharField(max_length=50)
    umur_ayah = models.CharField(max_length=8)
    berat_badan = models.CharField(max_length=10)
    panjang_badan = models.CharField(max_length=10)
    lingkar_kepala = models.CharField(max_length=10)
    proses_lahir = models.CharField(max_length=60)
    anakke = models.CharField(max_length=2)
    jam_lahir = models.TimeField()
    keterangan = models.CharField(max_length=50)
    diagnosa = models.CharField(max_length=60, blank=True, null=True)
    penyulit_kehamilan = models.CharField(max_length=60, blank=True, null=True)
    ketuban = models.CharField(max_length=60, blank=True, null=True)
    lingkar_perut = models.CharField(max_length=10, blank=True, null=True)
    lingkar_dada = models.CharField(max_length=10, blank=True, null=True)
    penolong = models.ForeignKey('Pegawai', on_delete = models.CASCADE, db_column='penolong', blank=True, null=True)
    no_skl = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pasien_bayi'


class PasienMati(models.Model):
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)
    no_rkm_medis = models.OneToOneField(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis', primary_key=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    temp_meninggal = models.CharField(max_length=24, blank=True, null=True)
    icd1 = models.CharField(max_length=20, blank=True, null=True)
    icd2 = models.CharField(max_length=20, blank=True, null=True)
    icd3 = models.CharField(max_length=20, blank=True, null=True)
    icd4 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pasien_mati'


class PasienPolri(models.Model):
    no_rkm_medis = models.OneToOneField(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis', primary_key=True)
    golongan_polri = models.ForeignKey(GolonganPolri, on_delete = models.CASCADE, db_column='golongan_polri')
    pangkat_polri = models.ForeignKey(PangkatPolri, on_delete = models.CASCADE, db_column='pangkat_polri')
    satuan_polri = models.ForeignKey('SatuanPolri', on_delete = models.CASCADE, db_column='satuan_polri')
    jabatan_polri = models.ForeignKey(JabatanPolri, on_delete = models.CASCADE, db_column='jabatan_polri')

    class Meta:
        managed = True
        db_table = 'pasien_polri'


class PasienTni(models.Model):
    no_rkm_medis = models.OneToOneField(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis', primary_key=True)
    golongan_tni = models.ForeignKey(GolonganTni, on_delete = models.CASCADE, db_column='golongan_tni')
    pangkat_tni = models.ForeignKey(PangkatTni, on_delete = models.CASCADE, db_column='pangkat_tni')
    satuan_tni = models.ForeignKey('SatuanTni', on_delete = models.CASCADE, db_column='satuan_tni')
    jabatan_tni = models.ForeignKey(JabatanTni, on_delete = models.CASCADE, db_column='jabatan_tni')

    class Meta:
        managed = True
        db_table = 'pasien_tni'


class PasswordAsuransi(models.Model):
    kd_pj = models.OneToOneField('Penjab', on_delete = models.CASCADE, db_column='kd_pj', primary_key=True)
    usere = models.CharField(max_length=700, blank=True, null=True)
    passworde = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'password_asuransi'
        unique_together = (('usere', 'passworde'),)


class PcareKegiatanKelompok(models.Model):
    eduid = models.CharField(db_column='eduId', primary_key=True, max_length=15)  # Field name made lowercase.
    clubid = models.CharField(db_column='clubId', max_length=5, blank=True, null=True)  # Field name made lowercase.
    namaclub = models.CharField(db_column='namaClub', max_length=100)  # Field name made lowercase.
    tglpelayanan = models.DateField(db_column='tglPelayanan', blank=True, null=True)  # Field name made lowercase.
    nmkegiatan = models.CharField(db_column='nmKegiatan', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nmkelompok = models.CharField(db_column='nmKelompok', max_length=30, blank=True, null=True)  # Field name made lowercase.
    materi = models.CharField(max_length=100, blank=True, null=True)
    pembicara = models.CharField(max_length=50, blank=True, null=True)
    lokasi = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    biaya = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pcare_kegiatan_kelompok'


class PcareKunjunganUmum(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    nokunjungan = models.CharField(db_column='noKunjungan', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tgldaftar = models.DateField(db_column='tglDaftar', blank=True, null=True)  # Field name made lowercase.
    no_rkm_medis = models.CharField(max_length=15, blank=True, null=True)
    nm_pasien = models.CharField(max_length=40, blank=True, null=True)
    nokartu = models.CharField(db_column='noKartu', max_length=25, blank=True, null=True)  # Field name made lowercase.
    kdpoli = models.CharField(db_column='kdPoli', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmpoli = models.CharField(db_column='nmPoli', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keluhan = models.CharField(max_length=400, blank=True, null=True)
    kdsadar = models.CharField(db_column='kdSadar', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmsadar = models.CharField(db_column='nmSadar', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sistole = models.CharField(max_length=3, blank=True, null=True)
    diastole = models.CharField(max_length=3, blank=True, null=True)
    beratbadan = models.CharField(db_column='beratBadan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tinggibadan = models.CharField(db_column='tinggiBadan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    resprate = models.CharField(db_column='respRate', max_length=3, blank=True, null=True)  # Field name made lowercase.
    heartrate = models.CharField(db_column='heartRate', max_length=3, blank=True, null=True)  # Field name made lowercase.
    terapi = models.CharField(max_length=400, blank=True, null=True)
    kdstatuspulang = models.CharField(db_column='kdStatusPulang', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmstatuspulang = models.CharField(db_column='nmStatusPulang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tglpulang = models.DateField(db_column='tglPulang', blank=True, null=True)  # Field name made lowercase.
    kddokter = models.CharField(db_column='kdDokter', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nmdokter = models.CharField(db_column='nmDokter', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kddiag1 = models.CharField(db_column='kdDiag1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag1 = models.CharField(db_column='nmDiag1', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kddiag2 = models.CharField(db_column='kdDiag2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag2 = models.CharField(db_column='nmDiag2', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kddiag3 = models.CharField(db_column='kdDiag3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag3 = models.CharField(db_column='nmDiag3', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pcare_kunjungan_umum'


class PcareObatDiberikan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    nokunjungan = models.CharField(db_column='noKunjungan', max_length=40)  # Field name made lowercase.
    kdobatsk = models.CharField(db_column='kdObatSK', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tgl_perawatan = models.DateField()
    jam = models.TimeField()
    kode_brng = models.ForeignKey(MapingObatPcare, on_delete = models.CASCADE, db_column='kode_brng')
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'pcare_obat_diberikan'
        unique_together = (('no_rawat', 'nokunjungan', 'tgl_perawatan', 'jam', 'kode_brng', 'no_batch', 'no_faktur'),)


class PcarePendaftaran(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgldaftar = models.DateField(db_column='tglDaftar')  # Field name made lowercase.
    no_rkm_medis = models.CharField(max_length=15)
    nm_pasien = models.CharField(max_length=40)
    kdproviderpeserta = models.CharField(db_column='kdProviderPeserta', max_length=15)  # Field name made lowercase.
    nokartu = models.CharField(db_column='noKartu', max_length=25)  # Field name made lowercase.
    kdpoli = models.CharField(db_column='kdPoli', max_length=5)  # Field name made lowercase.
    nmpoli = models.CharField(db_column='nmPoli', max_length=50)  # Field name made lowercase.
    keluhan = models.CharField(max_length=400)
    kunjsakit = models.CharField(db_column='kunjSakit', max_length=15)  # Field name made lowercase.
    sistole = models.CharField(max_length=3)
    diastole = models.CharField(max_length=3)
    beratbadan = models.CharField(db_column='beratBadan', max_length=5)  # Field name made lowercase.
    tinggibadan = models.CharField(db_column='tinggiBadan', max_length=5)  # Field name made lowercase.
    resprate = models.CharField(db_column='respRate', max_length=3)  # Field name made lowercase.
    heartrate = models.CharField(db_column='heartRate', max_length=3)  # Field name made lowercase.
    rujukbalik = models.CharField(db_column='rujukBalik', max_length=3)  # Field name made lowercase.
    kdtkp = models.CharField(db_column='kdTkp', max_length=21)  # Field name made lowercase.
    nourut = models.CharField(db_column='noUrut', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pcare_pendaftaran'


class PcarePesertaKegiatanKelompok(models.Model):
    eduid = models.OneToOneField(PcareKegiatanKelompok, on_delete = models.CASCADE, db_column='eduId', primary_key=True)  # Field name made lowercase.
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis')

    class Meta:
        managed = True
        db_table = 'pcare_peserta_kegiatan_kelompok'
        unique_together = (('eduid', 'no_rkm_medis'),)


class PcareTindakanRalanDiberikan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    nokunjungan = models.CharField(db_column='noKunjungan', max_length=40)  # Field name made lowercase.
    kdtindakansk = models.CharField(db_column='kdTindakanSK', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tgl_perawatan = models.DateField()
    jam = models.TimeField()
    kd_jenis_prw = models.ForeignKey(MapingTindakanPcare, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField()
    tarif_tindakanpr = models.FloatField()
    kso = models.FloatField()
    menejemen = models.FloatField()
    biaya_rawat = models.FloatField()

    class Meta:
        managed = True
        db_table = 'pcare_tindakan_ralan_diberikan'
        unique_together = (('no_rawat', 'nokunjungan', 'tgl_perawatan', 'jam', 'kd_jenis_prw'),)


class PcareTindakanRanapDiberikan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    nokunjungan = models.CharField(db_column='noKunjungan', max_length=40)  # Field name made lowercase.
    kdtindakansk = models.CharField(db_column='kdTindakanSK', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tgl_perawatan = models.DateField()
    jam = models.TimeField()
    kd_jenis_prw = models.ForeignKey(MapingTindakanRanapPcare, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField()
    tarif_tindakanpr = models.FloatField()
    kso = models.FloatField()
    menejemen = models.FloatField()
    biaya_rawat = models.FloatField()

    class Meta:
        managed = True
        db_table = 'pcare_tindakan_ranap_diberikan'
        unique_together = (('no_rawat', 'nokunjungan', 'tgl_perawatan', 'jam', 'kd_jenis_prw'),)


class Pegawai(models.Model):
    nik = models.CharField(unique=True, max_length=20)
    nama = models.CharField(max_length=50)
    jk = models.CharField(max_length=6)
    jbtn = models.CharField(max_length=25)
    jnj_jabatan = models.ForeignKey(JnjJabatan, on_delete = models.CASCADE, db_column='jnj_jabatan')
    kode_kelompok = models.ForeignKey(KelompokJabatan, on_delete = models.CASCADE, db_column='kode_kelompok')
    kode_resiko = models.ForeignKey('ResikoKerja', on_delete = models.CASCADE, db_column='kode_resiko')
    kode_emergency = models.ForeignKey(EmergencyIndex, on_delete = models.CASCADE, db_column='kode_emergency')
    departemen = models.ForeignKey(Departemen, on_delete = models.CASCADE, db_column='departemen')
    bidang = models.ForeignKey(Bidang, on_delete = models.CASCADE, db_column='bidang')
    stts_wp = models.ForeignKey('SttsWp', on_delete = models.CASCADE, db_column='stts_wp')
    stts_kerja = models.ForeignKey('SttsKerja', on_delete = models.CASCADE, db_column='stts_kerja')
    npwp = models.CharField(max_length=15)
    pendidikan = models.ForeignKey('Pendidikan', on_delete = models.CASCADE, db_column='pendidikan')
    gapok = models.FloatField()
    tmp_lahir = models.CharField(max_length=20)
    tgl_lahir = models.DateField()
    alamat = models.CharField(max_length=60)
    kota = models.CharField(max_length=20)
    mulai_kerja = models.DateField()
    ms_kerja = models.CharField(max_length=4)
    indexins = models.ForeignKey(Departemen, on_delete = models.CASCADE, db_column='indexins')
    bpd = models.ForeignKey(Bank, on_delete = models.CASCADE, db_column='bpd')
    rekening = models.CharField(max_length=25)
    stts_aktif = models.CharField(max_length=11)
    wajibmasuk = models.IntegerField()
    pengurang = models.FloatField()
    indek = models.IntegerField()
    mulai_kontrak = models.DateField(blank=True, null=True)
    cuti_diambil = models.IntegerField()
    dankes = models.FloatField()
    photo = models.CharField(max_length=500, blank=True, null=True)
    no_ktp = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'pegawai'


class PemasukanLain(models.Model):
    no_masuk = models.CharField(primary_key=True, max_length=15)
    tanggal = models.DateTimeField()
    kode_kategori = models.ForeignKey(KategoriPemasukanLain, on_delete = models.CASCADE, db_column='kode_kategori')
    besar = models.FloatField(blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    keterangan = models.CharField(max_length=50, blank=True, null=True)
    keperluan = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pemasukan_lain'


class PembagianAkte(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    persen = models.FloatField()

    class Meta:
        managed = True
        db_table = 'pembagian_akte'


class PembagianResume(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    persen = models.FloatField()

    class Meta:
        managed = True
        db_table = 'pembagian_resume'


class PembagianTuslah(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    persen = models.FloatField()

    class Meta:
        managed = True
        db_table = 'pembagian_tuslah'


class PembagianWarung(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    persen = models.FloatField()

    class Meta:
        managed = True
        db_table = 'pembagian_warung'


class Pembelian(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=20)
    kode_suplier = models.ForeignKey(Datasuplier, on_delete = models.CASCADE, db_column='kode_suplier', blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    tgl_beli = models.DateField(blank=True, null=True)
    total1 = models.FloatField()
    potongan = models.FloatField()
    total2 = models.FloatField()
    ppn = models.FloatField()
    tagihan = models.FloatField()
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')
    kd_rek = models.ForeignKey(AkunBayar, on_delete = models.CASCADE, db_column='kd_rek', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pembelian'


class Pemberihibah(models.Model):
    kode_pemberi = models.CharField(primary_key=True, max_length=5)
    nama_pemberi = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=20, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pemberihibah'


class PemeriksaanGinekologiRalan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    inspeksi = models.CharField(max_length=50, blank=True, null=True)
    inspeksi_vulva = models.CharField(max_length=50, blank=True, null=True)
    inspekulo_gine = models.CharField(max_length=50, blank=True, null=True)
    fluxus_gine = models.CharField(max_length=1, blank=True, null=True)
    fluor_gine = models.CharField(max_length=1, blank=True, null=True)
    vulva_inspekulo = models.CharField(max_length=50)
    portio_inspekulo = models.CharField(max_length=50, blank=True, null=True)
    sondage = models.CharField(max_length=50, blank=True, null=True)
    portio_dalam = models.CharField(max_length=50, blank=True, null=True)
    bentuk = models.CharField(max_length=50, blank=True, null=True)
    cavum_uteri = models.CharField(max_length=50, blank=True, null=True)
    mobilitas = models.CharField(max_length=1, blank=True, null=True)
    ukuran = models.CharField(max_length=50, blank=True, null=True)
    nyeri_tekan = models.CharField(max_length=1, blank=True, null=True)
    adnexa_kanan = models.CharField(max_length=50, blank=True, null=True)
    adnexa_kiri = models.CharField(max_length=50)
    cavum_douglas = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'pemeriksaan_ginekologi_ralan'
        unique_together = (('no_rawat', 'tgl_perawatan', 'jam_rawat'),)


class PemeriksaanGinekologiRanap(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    inspeksi = models.CharField(max_length=50, blank=True, null=True)
    inspeksi_vulva = models.CharField(max_length=50, blank=True, null=True)
    inspekulo_gine = models.CharField(max_length=50, blank=True, null=True)
    fluxus_gine = models.CharField(max_length=1, blank=True, null=True)
    fluor_gine = models.CharField(max_length=1, blank=True, null=True)
    vulva_inspekulo = models.CharField(max_length=50)
    portio_inspekulo = models.CharField(max_length=50, blank=True, null=True)
    sondage = models.CharField(max_length=50, blank=True, null=True)
    portio_dalam = models.CharField(max_length=50, blank=True, null=True)
    bentuk = models.CharField(max_length=50, blank=True, null=True)
    cavum_uteri = models.CharField(max_length=50, blank=True, null=True)
    mobilitas = models.CharField(max_length=1, blank=True, null=True)
    ukuran = models.CharField(max_length=50, blank=True, null=True)
    nyeri_tekan = models.CharField(max_length=1, blank=True, null=True)
    adnexa_kanan = models.CharField(max_length=50, blank=True, null=True)
    adnexa_kiri = models.CharField(max_length=50)
    cavum_douglas = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'pemeriksaan_ginekologi_ranap'
        unique_together = (('no_rawat', 'tgl_perawatan', 'jam_rawat'),)


class PemeriksaanObstetriRalan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    tinggi_uteri = models.CharField(max_length=5, blank=True, null=True)
    janin = models.CharField(max_length=7, blank=True, null=True)
    letak = models.CharField(max_length=50, blank=True, null=True)
    panggul = models.CharField(max_length=3, blank=True, null=True)
    denyut = models.CharField(max_length=5, blank=True, null=True)
    kontraksi = models.CharField(max_length=1, blank=True, null=True)
    kualitas_mnt = models.CharField(max_length=5, blank=True, null=True)
    kualitas_dtk = models.CharField(max_length=5, blank=True, null=True)
    fluksus = models.CharField(max_length=1, blank=True, null=True)
    albus = models.CharField(max_length=1, blank=True, null=True)
    vulva = models.CharField(max_length=50, blank=True, null=True)
    portio = models.CharField(max_length=50, blank=True, null=True)
    dalam = models.CharField(max_length=6, blank=True, null=True)
    tebal = models.CharField(max_length=5, blank=True, null=True)
    arah = models.CharField(max_length=8, blank=True, null=True)
    pembukaan = models.CharField(max_length=50, blank=True, null=True)
    penurunan = models.CharField(max_length=50, blank=True, null=True)
    denominator = models.CharField(max_length=50)
    ketuban = models.CharField(max_length=1, blank=True, null=True)
    feto = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pemeriksaan_obstetri_ralan'
        unique_together = (('no_rawat', 'tgl_perawatan', 'jam_rawat'),)


class PemeriksaanObstetriRanap(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    tinggi_uteri = models.CharField(max_length=5, blank=True, null=True)
    janin = models.CharField(max_length=7, blank=True, null=True)
    letak = models.CharField(max_length=50, blank=True, null=True)
    panggul = models.CharField(max_length=3, blank=True, null=True)
    denyut = models.CharField(max_length=5, blank=True, null=True)
    kontraksi = models.CharField(max_length=1, blank=True, null=True)
    kualitas_mnt = models.CharField(max_length=5, blank=True, null=True)
    kualitas_dtk = models.CharField(max_length=5, blank=True, null=True)
    fluksus = models.CharField(max_length=1, blank=True, null=True)
    albus = models.CharField(max_length=1, blank=True, null=True)
    vulva = models.CharField(max_length=50, blank=True, null=True)
    portio = models.CharField(max_length=50, blank=True, null=True)
    dalam = models.CharField(max_length=6, blank=True, null=True)
    tebal = models.CharField(max_length=5, blank=True, null=True)
    arah = models.CharField(max_length=8, blank=True, null=True)
    pembukaan = models.CharField(max_length=50, blank=True, null=True)
    penurunan = models.CharField(max_length=50, blank=True, null=True)
    denominator = models.CharField(max_length=50)
    ketuban = models.CharField(max_length=1, blank=True, null=True)
    feto = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pemeriksaan_obstetri_ranap'
        unique_together = (('no_rawat', 'tgl_perawatan', 'jam_rawat'),)


class PemeriksaanRalan(models.Model):
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    tgl_perawatan = models.DateField(blank=True, null=True)
    jam_rawat = models.TimeField(blank=True, null=True)
    suhu_tubuh = models.CharField(max_length=5, blank=True, null=True)
    tensi = models.CharField(max_length=7)
    nadi = models.CharField(max_length=3, blank=True, null=True)
    respirasi = models.CharField(max_length=3, blank=True, null=True)
    tinggi = models.CharField(max_length=5, blank=True, null=True)
    berat = models.CharField(max_length=5, blank=True, null=True)
    gcs = models.CharField(max_length=10, blank=True, null=True)
    keluhan = models.CharField(max_length=400, blank=True, null=True)
    pemeriksaan = models.CharField(max_length=400, blank=True, null=True)
    alergi = models.CharField(max_length=50, blank=True, null=True)
    imun_ke = models.CharField(max_length=2, blank=True, null=True)
    rtl = models.CharField(max_length=400)
    penilaian = models.CharField(max_length=400)

    class Meta:
        managed = True
        db_table = 'pemeriksaan_ralan'


class PemeriksaanRanap(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    suhu_tubuh = models.CharField(max_length=5, blank=True, null=True)
    tensi = models.CharField(max_length=7)
    nadi = models.CharField(max_length=3, blank=True, null=True)
    respirasi = models.CharField(max_length=3, blank=True, null=True)
    tinggi = models.CharField(max_length=5, blank=True, null=True)
    berat = models.CharField(max_length=5, blank=True, null=True)
    gcs = models.CharField(max_length=10, blank=True, null=True)
    keluhan = models.CharField(max_length=400, blank=True, null=True)
    pemeriksaan = models.CharField(max_length=400, blank=True, null=True)
    alergi = models.CharField(max_length=50, blank=True, null=True)
    penilaian = models.CharField(max_length=400)
    rtl = models.CharField(max_length=400)

    class Meta:
        managed = True
        db_table = 'pemeriksaan_ranap'
        unique_together = (('no_rawat', 'tgl_perawatan', 'jam_rawat'),)


class Pemesanan(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=20)
    no_order = models.CharField(max_length=20)
    kode_suplier = models.ForeignKey(Datasuplier, on_delete = models.CASCADE, db_column='kode_suplier', blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    tgl_pesan = models.DateField(blank=True, null=True)
    tgl_faktur = models.DateField(blank=True, null=True)
    tgl_tempo = models.DateField(blank=True, null=True)
    total1 = models.FloatField()
    potongan = models.FloatField()
    total2 = models.FloatField()
    ppn = models.FloatField()
    meterai = models.FloatField(blank=True, null=True)
    tagihan = models.FloatField()
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')
    status = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pemesanan'


class PeminjamanBerkas(models.Model):
    peminjam = models.CharField(primary_key=True, max_length=60)
    id_ruang = models.ForeignKey(InventarisRuang, on_delete = models.CASCADE, db_column='id_ruang')
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis')
    tgl_pinjam = models.DateField()
    tgl_kembali = models.DateField()
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')
    status_pinjam = models.CharField(max_length=14)

    class Meta:
        managed = True
        db_table = 'peminjaman_berkas'
        unique_together = (('peminjam', 'id_ruang', 'no_rkm_medis', 'tgl_pinjam', 'nip'),)


class PeminjamanKoperasi(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    tanggal = models.DateField()
    pinjaman = models.FloatField()
    banyak_angsur = models.IntegerField()
    pokok = models.FloatField()
    jasa = models.FloatField()
    status = models.CharField(max_length=11)

    class Meta:
        managed = True
        db_table = 'peminjaman_koperasi'
        unique_together = (('id', 'tanggal'),)


class PencapaianKinerja(models.Model):
    kode_pencapaian = models.CharField(primary_key=True, max_length=3)
    nama_pencapaian = models.CharField(max_length=200, blank=True, null=True)
    indek = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pencapaian_kinerja'


class PencapaianKinerjaPegawai(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    kode_pencapaian = models.ForeignKey(PencapaianKinerja, on_delete = models.CASCADE, db_column='kode_pencapaian')
    tahun = models.TextField()  # This field type is a guess.
    bulan = models.IntegerField()
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pencapaian_kinerja_pegawai'
        unique_together = (('id', 'kode_pencapaian', 'tahun', 'bulan'),)


class Pendidikan(models.Model):
    tingkat = models.CharField(primary_key=True, max_length=80)
    indek = models.IntegerField()
    gapok1 = models.FloatField()
    kenaikan = models.FloatField()
    maksimal = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'pendidikan'


class Pengaduan(models.Model):
    date_time = models.DateTimeField()
    username = models.CharField(max_length=20)
    message = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'pengaduan'


class PengajuanBarangMedis(models.Model):
    no_pengajuan = models.CharField(primary_key=True, max_length=20)
    nip = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pengajuan_barang_medis'


class PengajuanBarangNonmedis(models.Model):
    no_pengajuan = models.CharField(primary_key=True, max_length=20)
    nip = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pengajuan_barang_nonmedis'


class PengajuanInventaris(models.Model):
    no_pengajuan = models.CharField(primary_key=True, max_length=20)
    tanggal = models.DateField()
    nik = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='nik')
    urgensi = models.CharField(max_length=9)
    latar_belakang = models.CharField(max_length=200)
    nama_barang = models.CharField(max_length=70)
    spesifikasi = models.CharField(max_length=200)
    jumlah = models.FloatField()
    harga = models.FloatField()
    total = models.FloatField()
    keterangan = models.CharField(max_length=70)
    nik_pj = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='nik_pj')
    status = models.CharField(max_length=16)

    class Meta:
        managed = True
        db_table = 'pengajuan_inventaris'


class PengeluaranHarian(models.Model):
    tanggal = models.DateTimeField(primary_key=True)
    kode_kategori = models.ForeignKey(KategoriPengeluaranHarian, on_delete = models.CASCADE, db_column='kode_kategori', blank=True, null=True)
    biaya = models.FloatField()
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    keterangan = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'pengeluaran_harian'
        unique_together = (('tanggal', 'keterangan'),)


class PengeluaranObatBhp(models.Model):
    no_keluar = models.CharField(primary_key=True, max_length=15)
    tanggal = models.DateField()
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')
    keterangan = models.CharField(max_length=200)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pengeluaran_obat_bhp'


class PenguranganBiaya(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    nama_pengurangan = models.CharField(max_length=60)
    besar_pengurangan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pengurangan_biaya'
        unique_together = (('no_rawat', 'nama_pengurangan'),)


class PeniliaianAwalKeperawatanRalan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    informasi = models.CharField(max_length=13)
    td = models.CharField(max_length=5)
    nadi = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    bb = models.CharField(max_length=5)
    tb = models.CharField(max_length=5)
    bmi = models.CharField(max_length=5)
    keluhan_utama = models.CharField(max_length=150)
    rpd = models.CharField(max_length=100)
    rpk = models.CharField(max_length=100)
    rpo = models.CharField(max_length=100)
    alergi = models.CharField(max_length=25)
    alat_bantu = models.CharField(max_length=5)
    ket_bantu = models.CharField(max_length=70)
    prothesa = models.CharField(max_length=5)
    ket_pro = models.CharField(max_length=100)
    adl = models.CharField(max_length=7)
    status_psiko = models.CharField(max_length=9)
    ket_psiko = models.CharField(max_length=70)
    hub_keluarga = models.CharField(max_length=10)
    tinggal_dengan = models.CharField(max_length=13)
    ket_tinggal = models.CharField(max_length=70)
    ekonomi = models.CharField(max_length=6)
    edukasi = models.CharField(max_length=8)
    ket_edukasi = models.CharField(max_length=70)
    berjalan_a = models.CharField(max_length=5)
    berjalan_b = models.CharField(max_length=5)
    berjalan_c = models.CharField(max_length=5)
    hasil = models.CharField(max_length=40)
    lapor = models.CharField(max_length=5)
    ket_lapor = models.CharField(max_length=70)
    sg1 = models.CharField(max_length=11)
    nilai1 = models.CharField(max_length=1)
    sg2 = models.CharField(max_length=5)
    nilai2 = models.CharField(max_length=1)
    total_hasil = models.CharField(max_length=5)
    nyeri = models.CharField(max_length=15)
    provokes = models.CharField(max_length=15)
    ket_provokes = models.CharField(max_length=100)
    quality = models.CharField(max_length=16)
    ket_quality = models.CharField(max_length=70)
    lokasi = models.CharField(max_length=70)
    menyebar = models.CharField(max_length=5)
    skala_nyeri = models.CharField(max_length=2)
    durasi = models.CharField(max_length=5)
    nyeri_hilang = models.CharField(max_length=14)
    ket_nyeri = models.CharField(max_length=70)
    pada_dokter = models.CharField(max_length=5)
    ket_dokter = models.CharField(max_length=70)
    masalah_keperawatan = models.CharField(max_length=34)
    rencana = models.CharField(max_length=150)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')

    class Meta:
        managed = True
        db_table = 'peniliaian_awal_keperawatan_ralan'


class Penjab(models.Model):
    kd_pj = models.CharField(primary_key=True, max_length=3)
    png_jawab = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'penjab'


class Penjualan(models.Model):
    nota_jual = models.CharField(primary_key=True, max_length=20)
    tgl_jual = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis', blank=True, null=True)
    nm_pasien = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.CharField(max_length=40, blank=True, null=True)
    jns_jual = models.CharField(max_length=11, blank=True, null=True)
    ongkir = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=13, blank=True, null=True)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')
    kd_rek = models.ForeignKey(AkunBayar, on_delete = models.CASCADE, db_column='kd_rek', blank=True, null=True)
    nama_bayar = models.ForeignKey(AkunBayar, on_delete = models.CASCADE, db_column='nama_bayar', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'penjualan'


class Penyakit(models.Model):
    kd_penyakit = models.CharField(primary_key=True, max_length=10)
    nm_penyakit = models.CharField(max_length=100, blank=True, null=True)
    ciri_ciri = models.TextField(blank=True, null=True)
    keterangan = models.CharField(max_length=60, blank=True, null=True)
    kd_ktg = models.ForeignKey(KategoriPenyakit, on_delete = models.CASCADE, db_column='kd_ktg', blank=True, null=True)
    status = models.CharField(max_length=13)

    class Meta:
        managed = True
        db_table = 'penyakit'


class PenyakitPd3I(models.Model):
    kd_penyakit = models.OneToOneField(Penyakit, on_delete = models.CASCADE, db_column='kd_penyakit', primary_key=True)

    class Meta:
        managed = True
        db_table = 'penyakit_pd3i'


class PeriksaLab(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')
    kd_jenis_prw = models.ForeignKey(JnsPerawatanLab, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    dokter_perujuk = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='dokter_perujuk')
    bagian_rs = models.FloatField()
    bhp = models.FloatField()
    tarif_perujuk = models.FloatField()
    tarif_tindakan_dokter = models.FloatField()
    tarif_tindakan_petugas = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya = models.FloatField()
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')
    status = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'periksa_lab'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'tgl_periksa', 'jam'),)


class PeriksaRadiologi(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip')
    kd_jenis_prw = models.ForeignKey(JnsPerawatanRadiologi, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    dokter_perujuk = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='dokter_perujuk')
    bagian_rs = models.FloatField()
    bhp = models.FloatField()
    tarif_perujuk = models.FloatField()
    tarif_tindakan_dokter = models.FloatField()
    tarif_tindakan_petugas = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya = models.FloatField()
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')
    status = models.CharField(max_length=5, blank=True, null=True)
    proyeksi = models.CharField(max_length=50)
    kv = models.CharField(db_column='kV', max_length=10)  # Field name made lowercase.
    mas = models.CharField(db_column='mAS', max_length=10)  # Field name made lowercase.
    ffd = models.CharField(db_column='FFD', max_length=10)  # Field name made lowercase.
    bsf = models.CharField(db_column='BSF', max_length=10)  # Field name made lowercase.
    inak = models.CharField(max_length=10)
    jml_penyinaran = models.CharField(max_length=10)
    dosis = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'periksa_radiologi'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'tgl_periksa', 'jam'),)


class PermintaanDetailPermintaanLab(models.Model):
    noorder = models.OneToOneField('PermintaanLab', on_delete = models.CASCADE, db_column='noorder', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanLab, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    id_template = models.ForeignKey('TemplateLaboratorium', on_delete = models.CASCADE, db_column='id_template')
    stts_bayar = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'permintaan_detail_permintaan_lab'
        unique_together = (('noorder', 'kd_jenis_prw', 'id_template'),)


class PermintaanLab(models.Model):
    noorder = models.CharField(primary_key=True, max_length=15)
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    tgl_permintaan = models.DateField()
    jam_permintaan = models.TimeField()
    tgl_sampel = models.DateField()
    jam_sampel = models.TimeField()
    tgl_hasil = models.DateField()
    jam_hasil = models.TimeField()
    dokter_perujuk = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='dokter_perujuk')
    status = models.CharField(max_length=5)

    class Meta:
        managed = True
        db_table = 'permintaan_lab'


class PermintaanMedis(models.Model):
    no_permintaan = models.CharField(primary_key=True, max_length=20)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal', blank=True, null=True)
    nip = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    kd_bangsaltujuan = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsaltujuan')

    class Meta:
        managed = True
        db_table = 'permintaan_medis'


class PermintaanNonMedis(models.Model):
    no_permintaan = models.CharField(primary_key=True, max_length=20)
    ruang = models.CharField(max_length=50, blank=True, null=True)
    nip = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'permintaan_non_medis'


class PermintaanObat(models.Model):
    tanggal = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')

    class Meta:
        managed = True
        db_table = 'permintaan_obat'
        unique_together = (('tanggal', 'jam', 'no_rawat', 'kode_brng'),)


class PermintaanPemeriksaanLab(models.Model):
    noorder = models.OneToOneField(PermintaanLab, on_delete = models.CASCADE, db_column='noorder', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanLab, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    stts_bayar = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'permintaan_pemeriksaan_lab'
        unique_together = (('noorder', 'kd_jenis_prw'),)


class PermintaanPemeriksaanRadiologi(models.Model):
    noorder = models.OneToOneField('PermintaanRadiologi', on_delete = models.CASCADE, db_column='noorder', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanRadiologi, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    stts_bayar = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'permintaan_pemeriksaan_radiologi'
        unique_together = (('noorder', 'kd_jenis_prw'),)


class PermintaanPerbaikanInventaris(models.Model):
    no_permintaan = models.CharField(primary_key=True, max_length=15)
    no_inventaris = models.ForeignKey(Inventaris, on_delete = models.CASCADE, db_column='no_inventaris', blank=True, null=True)
    nik = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='nik', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    deskripsi_kerusakan = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'permintaan_perbaikan_inventaris'


class PermintaanRadiologi(models.Model):
    noorder = models.CharField(primary_key=True, max_length=15)
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    tgl_permintaan = models.DateField()
    jam_permintaan = models.TimeField()
    tgl_sampel = models.DateField()
    jam_sampel = models.TimeField()
    tgl_hasil = models.DateField()
    jam_hasil = models.TimeField()
    dokter_perujuk = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='dokter_perujuk')
    status = models.CharField(max_length=5)
    informasi_tambahan = models.CharField(max_length=100)
    diagnosa_klinis = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'permintaan_radiologi'


class PermintaanRegistrasi(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    biaya = models.FloatField()

    class Meta:
        managed = True
        db_table = 'permintaan_registrasi'


class PerpustakaanAnggota(models.Model):
    no_anggota = models.CharField(primary_key=True, max_length=10)
    nama_anggota = models.CharField(max_length=40, blank=True, null=True)
    tmp_lahir = models.CharField(max_length=20, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    j_kel = models.CharField(max_length=1, blank=True, null=True)
    alamat = models.CharField(max_length=70, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    tgl_gabung = models.DateField(blank=True, null=True)
    masa_berlaku = models.DateField(blank=True, null=True)
    jenis_anggota = models.CharField(max_length=7)
    nomer_id = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'perpustakaan_anggota'


class PerpustakaanBayarDenda(models.Model):
    tgl_denda = models.DateField(primary_key=True)
    no_anggota = models.ForeignKey(PerpustakaanAnggota, on_delete = models.CASCADE, db_column='no_anggota')
    no_inventaris = models.ForeignKey('PerpustakaanInventaris', on_delete = models.CASCADE, db_column='no_inventaris')
    kode_denda = models.ForeignKey('PerpustakaanDenda', on_delete = models.CASCADE, db_column='kode_denda')
    besar_denda = models.FloatField(blank=True, null=True)
    keterangan_denda = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_bayar_denda'
        unique_together = (('tgl_denda', 'no_anggota', 'no_inventaris', 'kode_denda'),)


class PerpustakaanBayarDendaHarian(models.Model):
    tgl_denda = models.DateField(primary_key=True)
    no_anggota = models.ForeignKey(PerpustakaanAnggota, on_delete = models.CASCADE, db_column='no_anggota')
    no_inventaris = models.ForeignKey('PerpustakaanInventaris', on_delete = models.CASCADE, db_column='no_inventaris')
    keterlambatan = models.IntegerField(blank=True, null=True)
    besar_denda = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_bayar_denda_harian'
        unique_together = (('tgl_denda', 'no_anggota', 'no_inventaris'),)


class PerpustakaanBuku(models.Model):
    kode_buku = models.CharField(primary_key=True, max_length=10)
    judul_buku = models.CharField(max_length=200, blank=True, null=True)
    jml_halaman = models.CharField(max_length=5, blank=True, null=True)
    kode_penerbit = models.ForeignKey('PerpustakaanPenerbit', on_delete = models.CASCADE, db_column='kode_penerbit', blank=True, null=True)
    kode_pengarang = models.ForeignKey('PerpustakaanPengarang', on_delete = models.CASCADE, db_column='kode_pengarang', blank=True, null=True)
    thn_terbit = models.TextField(blank=True, null=True)  # This field type is a guess.
    isbn = models.CharField(max_length=20, blank=True, null=True)
    id_kategori = models.ForeignKey('PerpustakaanKategori', on_delete = models.CASCADE, db_column='id_kategori', blank=True, null=True)
    id_jenis = models.ForeignKey('PerpustakaanJenisBuku', on_delete = models.CASCADE, db_column='id_jenis', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_buku'


class PerpustakaanDenda(models.Model):
    kode_denda = models.CharField(primary_key=True, max_length=5)
    jenis_denda = models.CharField(max_length=40, blank=True, null=True)
    besar_denda = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_denda'


class PerpustakaanEbook(models.Model):
    kode_ebook = models.CharField(primary_key=True, max_length=10)
    judul_ebook = models.CharField(max_length=200, blank=True, null=True)
    jml_halaman = models.CharField(max_length=5, blank=True, null=True)
    kode_penerbit = models.ForeignKey('PerpustakaanPenerbit', on_delete = models.CASCADE, db_column='kode_penerbit', blank=True, null=True)
    kode_pengarang = models.ForeignKey('PerpustakaanPengarang', on_delete = models.CASCADE, db_column='kode_pengarang', blank=True, null=True)
    thn_terbit = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_kategori = models.ForeignKey('PerpustakaanKategori', on_delete = models.CASCADE, db_column='id_kategori', blank=True, null=True)
    id_jenis = models.ForeignKey('PerpustakaanJenisBuku', on_delete = models.CASCADE, db_column='id_jenis', blank=True, null=True)
    berkas = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'perpustakaan_ebook'


class PerpustakaanInventaris(models.Model):
    no_inventaris = models.CharField(primary_key=True, max_length=20)
    kode_buku = models.ForeignKey(PerpustakaanBuku, on_delete = models.CASCADE, db_column='kode_buku', blank=True, null=True)
    asal_buku = models.CharField(max_length=7, blank=True, null=True)
    tgl_pengadaan = models.DateField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    status_buku = models.CharField(max_length=8, blank=True, null=True)
    kd_ruang = models.ForeignKey('PerpustakaanRuang', on_delete = models.CASCADE, db_column='kd_ruang', blank=True, null=True)
    no_rak = models.CharField(max_length=3, blank=True, null=True)
    no_box = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_inventaris'


class PerpustakaanJenisBuku(models.Model):
    id_jenis = models.CharField(primary_key=True, max_length=5)
    nama_jenis = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_jenis_buku'


class PerpustakaanKategori(models.Model):
    id_kategori = models.CharField(primary_key=True, max_length=5)
    nama_kategori = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_kategori'


class PerpustakaanPeminjaman(models.Model):
    no_anggota = models.ForeignKey(PerpustakaanAnggota, on_delete = models.CASCADE, db_column='no_anggota', blank=True, null=True)
    no_inventaris = models.ForeignKey(PerpustakaanInventaris, on_delete = models.CASCADE, db_column='no_inventaris', blank=True, null=True)
    tgl_pinjam = models.DateField(blank=True, null=True)
    tgl_kembali = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('Petugas', on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    status_pinjam = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_peminjaman'


class PerpustakaanPenerbit(models.Model):
    kode_penerbit = models.CharField(primary_key=True, max_length=10)
    nama_penerbit = models.CharField(max_length=40, blank=True, null=True)
    alamat_penerbit = models.CharField(max_length=70, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    website_penerbit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_penerbit'


class PerpustakaanPengarang(models.Model):
    kode_pengarang = models.CharField(primary_key=True, max_length=7)
    nama_pengarang = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_pengarang'


class PerpustakaanRuang(models.Model):
    kd_ruang = models.CharField(primary_key=True, max_length=5)
    nm_ruang = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_ruang'


class PerpustakaanSetPeminjaman(models.Model):
    max_pinjam = models.IntegerField(blank=True, null=True)
    lama_pinjam = models.IntegerField(blank=True, null=True)
    denda_perhari = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perpustakaan_set_peminjaman'


class PerusahaanPasien(models.Model):
    kode_perusahaan = models.CharField(primary_key=True, max_length=8)
    nama_perusahaan = models.CharField(max_length=70, blank=True, null=True)
    alamat = models.CharField(max_length=100, blank=True, null=True)
    kota = models.CharField(max_length=40, blank=True, null=True)
    no_telp = models.CharField(max_length=27, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perusahaan_pasien'


class Petugas(models.Model):
    nip = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='nip', primary_key=True)
    nama = models.CharField(max_length=50, blank=True, null=True)
    jk = models.CharField(max_length=1, blank=True, null=True)
    tmp_lahir = models.CharField(max_length=20, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    gol_darah = models.CharField(max_length=2, blank=True, null=True)
    agama = models.CharField(max_length=12, blank=True, null=True)
    stts_nikah = models.CharField(max_length=7, blank=True, null=True)
    alamat = models.CharField(max_length=60, blank=True, null=True)
    kd_jbtn = models.ForeignKey(Jabatan, on_delete = models.CASCADE, db_column='kd_jbtn', blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'petugas'


class Piutang(models.Model):
    nota_piutang = models.CharField(primary_key=True, max_length=20)
    tgl_piutang = models.DateField(blank=True, null=True)
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis', blank=True, null=True)
    nm_pasien = models.CharField(max_length=50, blank=True, null=True)
    catatan = models.CharField(max_length=40, blank=True, null=True)
    jns_jual = models.CharField(max_length=11, blank=True, null=True)
    ongkir = models.FloatField(blank=True, null=True)
    uangmuka = models.FloatField(blank=True, null=True)
    sisapiutang = models.FloatField()
    status = models.CharField(max_length=5, blank=True, null=True)
    tgltempo = models.DateField()
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')

    class Meta:
        managed = True
        db_table = 'piutang'


class PiutangPasien(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgl_piutang = models.DateField(blank=True, null=True)
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis', blank=True, null=True)
    status = models.CharField(max_length=11)
    totalpiutang = models.FloatField(blank=True, null=True)
    uangmuka = models.FloatField(blank=True, null=True)
    sisapiutang = models.FloatField()
    tgltempo = models.DateField()

    class Meta:
        managed = True
        db_table = 'piutang_pasien'


class PnmTnjBulanan(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    id_tnj = models.ForeignKey(MasterTunjanganBulanan, on_delete = models.CASCADE, db_column='id_tnj')

    class Meta:
        managed = True
        db_table = 'pnm_tnj_bulanan'
        unique_together = (('id', 'id_tnj'),)


class PnmTnjHarian(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    id_tnj = models.ForeignKey(MasterTunjanganHarian, on_delete = models.CASCADE, db_column='id_tnj')

    class Meta:
        managed = True
        db_table = 'pnm_tnj_harian'
        unique_together = (('id', 'id_tnj'),)


class Poliklinik(models.Model):
    kd_poli = models.CharField(primary_key=True, max_length=5)
    nm_poli = models.CharField(max_length=50, blank=True, null=True)
    registrasi = models.FloatField()
    registrasilama = models.FloatField()
    status = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'poliklinik'


class Potongan(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    id = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='id')
    bpjs = models.FloatField()
    jamsostek = models.FloatField()
    dansos = models.FloatField()
    simwajib = models.FloatField()
    angkop = models.FloatField()
    angla = models.FloatField()
    telpri = models.FloatField()
    pajak = models.FloatField()
    pribadi = models.FloatField()
    lain = models.FloatField()
    ktg = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'potongan'
        unique_together = (('tahun', 'bulan', 'id'),)


class Presensi(models.Model):
    tgl = models.DateField(primary_key=True)
    id = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='id')
    jns = models.CharField(max_length=2)
    lembur = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'presensi'
        unique_together = (('tgl', 'id'),)


class Propinsi(models.Model):
    kd_prop = models.AutoField(primary_key=True)
    nm_prop = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = True
        db_table = 'propinsi'


class ProsedurPasien(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kode = models.ForeignKey(Icd9, on_delete = models.CASCADE, db_column='kode')
    status = models.CharField(max_length=5)
    prioritas = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'prosedur_pasien'
        unique_together = (('no_rawat', 'kode', 'status'),)


class RanapGabung(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    no_rawat2 = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat2')

    class Meta:
        managed = True
        db_table = 'ranap_gabung'
        unique_together = (('no_rawat', 'no_rawat2'),)


class RawatInapDr(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanInap, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawat_inap_dr'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'kd_dokter', 'tgl_perawatan', 'jam_rawat'),)


class RawatInapDrpr(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanInap, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip')
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField(blank=True, null=True)
    tarif_tindakanpr = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawat_inap_drpr'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'kd_dokter', 'nip', 'tgl_perawatan', 'jam_rawat'),)


class RawatInapPr(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanInap, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip')
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakanpr = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawat_inap_pr'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'nip', 'tgl_perawatan', 'jam_rawat'),)


class RawatJlDr(models.Model):
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    kd_jenis_prw = models.ForeignKey(JnsPerawatan, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')
    tgl_perawatan = models.DateField(blank=True, null=True)
    jam_rawat = models.TimeField(blank=True, null=True)
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)
    stts_bayar = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawat_jl_dr'


class RawatJlDrpr(models.Model):
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    kd_jenis_prw = models.ForeignKey(JnsPerawatan, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip')
    tgl_perawatan = models.DateField(blank=True, null=True)
    jam_rawat = models.TimeField(blank=True, null=True)
    material = models.FloatField(blank=True, null=True)
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField(blank=True, null=True)
    tarif_tindakanpr = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)
    stts_bayar = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawat_jl_drpr'


class RawatJlPr(models.Model):
    no_rawat = models.ForeignKey('RegPeriksa', on_delete = models.CASCADE, db_column='no_rawat')
    kd_jenis_prw = models.ForeignKey(JnsPerawatan, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip')
    tgl_perawatan = models.DateField(blank=True, null=True)
    jam_rawat = models.TimeField(blank=True, null=True)
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakanpr = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)
    stts_bayar = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rawat_jl_pr'


class Rawatjalan(models.Model):
    tgl = models.DateTimeField(primary_key=True)
    id = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='id')
    tnd = models.IntegerField()
    jm = models.FloatField()
    nm_pasien = models.CharField(max_length=30)
    kamar = models.CharField(max_length=20)
    diagnosa = models.CharField(max_length=50)
    jmlh = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'rawatjalan'
        unique_together = (('tgl', 'id', 'tnd'),)


class RegPeriksa(models.Model):
    no_reg = models.CharField(max_length=8, blank=True, null=True)
    no_rawat = models.CharField(primary_key=True, max_length=17)
    tgl_registrasi = models.DateField(blank=True, null=True)
    jam_reg = models.TimeField(blank=True, null=True)
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter', blank=True, null=True)
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis', blank=True, null=True)
    kd_poli = models.ForeignKey(Poliklinik, on_delete = models.CASCADE, db_column='kd_poli', blank=True, null=True)
    p_jawab = models.CharField(max_length=100, blank=True, null=True)
    almt_pj = models.CharField(max_length=200, blank=True, null=True)
    hubunganpj = models.CharField(max_length=20, blank=True, null=True)
    biaya_reg = models.FloatField(blank=True, null=True)
    stts = models.CharField(max_length=15, blank=True, null=True)
    stts_daftar = models.CharField(max_length=4)
    status_lanjut = models.CharField(max_length=5)
    kd_pj = models.ForeignKey(Penjab, on_delete = models.CASCADE, db_column='kd_pj')
    umurdaftar = models.IntegerField(blank=True, null=True)
    sttsumur = models.CharField(max_length=2, blank=True, null=True)
    status_bayar = models.CharField(max_length=11)
    status_poli = models.CharField(max_length=4)

    class Meta:
        managed = True
        db_table = 'reg_periksa'


class RekapPresensi(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    shift = models.CharField(max_length=13)
    jam_datang = models.DateTimeField()
    jam_pulang = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=25)
    keterlambatan = models.CharField(max_length=20)
    durasi = models.CharField(max_length=20, blank=True, null=True)
    keterangan = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'rekap_presensi'
        unique_together = (('id', 'jam_datang'),)


class Rekening(models.Model):
    kd_rek = models.CharField(primary_key=True, max_length=15)
    nm_rek = models.CharField(max_length=100, blank=True, null=True)
    tipe = models.CharField(max_length=1, blank=True, null=True)
    balance = models.CharField(max_length=1, blank=True, null=True)
    level = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rekening'


class Rekeningtahun(models.Model):
    thn = models.TextField(primary_key=True)  # This field type is a guess.
    kd_rek = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='kd_rek')
    saldo_awal = models.FloatField()

    class Meta:
        managed = True
        db_table = 'rekeningtahun'
        unique_together = (('thn', 'kd_rek'),)


class ResepDokter(models.Model):
    no_resep = models.ForeignKey('ResepObat', on_delete = models.CASCADE, db_column='no_resep', blank=True, null=True)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng', blank=True, null=True)
    jml = models.FloatField(blank=True, null=True)
    aturan_pakai = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resep_dokter'


class ResepDokterRacikan(models.Model):
    no_resep = models.OneToOneField('ResepObat', on_delete = models.CASCADE, db_column='no_resep', primary_key=True)
    no_racik = models.CharField(max_length=2)
    nama_racik = models.CharField(max_length=100)
    kd_racik = models.ForeignKey(MetodeRacik, on_delete = models.CASCADE, db_column='kd_racik')
    jml_dr = models.IntegerField()
    aturan_pakai = models.CharField(max_length=150)
    keterangan = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'resep_dokter_racikan'
        unique_together = (('no_resep', 'no_racik'),)


class ResepDokterRacikanDetail(models.Model):
    no_resep = models.OneToOneField('ResepObat', on_delete = models.CASCADE, db_column='no_resep', primary_key=True)
    no_racik = models.CharField(max_length=2)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    p1 = models.FloatField(blank=True, null=True)
    p2 = models.FloatField(blank=True, null=True)
    kandungan = models.CharField(max_length=10, blank=True, null=True)
    jml = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resep_dokter_racikan_detail'
        unique_together = (('no_resep', 'no_racik', 'kode_brng'),)


class ResepObat(models.Model):
    no_resep = models.CharField(primary_key=True, max_length=14)
    tgl_perawatan = models.DateField(blank=True, null=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat')
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')
    tgl_peresepan = models.DateField(blank=True, null=True)
    jam_peresepan = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resep_obat'
        unique_together = (('tgl_perawatan', 'jam', 'no_rawat'),)


class ResepPulang(models.Model):
    no_rawat = models.OneToOneField(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    jml_barang = models.FloatField()
    harga = models.FloatField()
    total = models.FloatField()
    dosis = models.CharField(max_length=20)
    tanggal = models.DateField()
    jam = models.TimeField()
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'resep_pulang'
        unique_together = (('no_rawat', 'kode_brng', 'tanggal', 'jam', 'no_batch', 'no_faktur'),)


class ResikoKerja(models.Model):
    kode_resiko = models.CharField(primary_key=True, max_length=3)
    nama_resiko = models.CharField(max_length=200, blank=True, null=True)
    indek = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resiko_kerja'


class ResumePasien(models.Model):
    no_rawat = models.OneToOneField(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')
    keluhan_utama = models.TextField()
    jalannya_penyakit = models.TextField()
    pemeriksaan_penunjang = models.TextField()
    hasil_laborat = models.TextField()
    diagnosa_utama = models.CharField(max_length=80)
    kd_diagnosa_utama = models.CharField(max_length=10)
    diagnosa_sekunder = models.CharField(max_length=80)
    kd_diagnosa_sekunder = models.CharField(max_length=10)
    diagnosa_sekunder2 = models.CharField(max_length=80)
    kd_diagnosa_sekunder2 = models.CharField(max_length=10)
    diagnosa_sekunder3 = models.CharField(max_length=80)
    kd_diagnosa_sekunder3 = models.CharField(max_length=10)
    diagnosa_sekunder4 = models.CharField(max_length=80)
    kd_diagnosa_sekunder4 = models.CharField(max_length=10)
    prosedur_utama = models.CharField(max_length=80)
    kd_prosedur_utama = models.CharField(max_length=8)
    prosedur_sekunder = models.CharField(max_length=80)
    kd_prosedur_sekunder = models.CharField(max_length=8)
    prosedur_sekunder2 = models.CharField(max_length=80)
    kd_prosedur_sekunder2 = models.CharField(max_length=8)
    prosedur_sekunder3 = models.CharField(max_length=80)
    kd_prosedur_sekunder3 = models.CharField(max_length=8)
    kondisi_pulang = models.CharField(max_length=9)
    obat_pulang = models.TextField()

    class Meta:
        managed = True
        db_table = 'resume_pasien'


class RetensiPasien(models.Model):
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis', blank=True, null=True)
    terakhir_daftar = models.DateField(blank=True, null=True)
    tgl_retensi = models.DateField(blank=True, null=True)
    lokasi_pdf = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'retensi_pasien'


class Returbeli(models.Model):
    no_retur_beli = models.CharField(primary_key=True, max_length=20)
    tgl_retur = models.DateField(blank=True, null=True)
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    kode_suplier = models.ForeignKey(Datasuplier, on_delete = models.CASCADE, db_column='kode_suplier')
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')

    class Meta:
        managed = True
        db_table = 'returbeli'


class Returjual(models.Model):
    no_retur_jual = models.CharField(primary_key=True, max_length=20)
    tgl_retur = models.DateField(blank=True, null=True)
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis')
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')

    class Meta:
        managed = True
        db_table = 'returjual'


class Returpasien(models.Model):
    tanggal = models.DateField(primary_key=True)
    no_rawat = models.ForeignKey(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    jml = models.FloatField()
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'returpasien'
        unique_together = (('tanggal', 'no_rawat', 'kode_brng', 'no_batch', 'no_faktur'),)


class Returpiutang(models.Model):
    no_retur_piutang = models.CharField(primary_key=True, max_length=20)
    tgl_retur = models.DateField(blank=True, null=True)
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis')
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')

    class Meta:
        managed = True
        db_table = 'returpiutang'


class RiwayatBarangMedis(models.Model):
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng', blank=True, null=True)
    stok_awal = models.FloatField(blank=True, null=True)
    masuk = models.FloatField(blank=True, null=True)
    keluar = models.FloatField(blank=True, null=True)
    stok_akhir = models.FloatField()
    posisi = models.CharField(max_length=17, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)
    petugas = models.CharField(max_length=20, blank=True, null=True)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal', blank=True, null=True)
    status = models.CharField(max_length=6, blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'riwayat_barang_medis'


class RiwayatJabatan(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    jabatan = models.CharField(max_length=50)
    tmt_pangkat = models.DateField()
    tmt_pangkat_yad = models.DateField()
    pejabat_penetap = models.CharField(max_length=50)
    nomor_sk = models.CharField(max_length=25)
    tgl_sk = models.DateField()
    dasar_peraturan = models.CharField(max_length=50)
    masa_kerja = models.IntegerField()
    bln_kerja = models.IntegerField()
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'riwayat_jabatan'
        unique_together = (('id', 'jabatan'),)


class RiwayatNaikGaji(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    pangkatjabatan = models.CharField(max_length=50)
    gapok = models.FloatField()
    tmt_berkala = models.DateField()
    tmt_berkala_yad = models.DateField()
    no_sk = models.CharField(max_length=25)
    tgl_sk = models.DateField()
    masa_kerja = models.IntegerField()
    bulan_kerja = models.IntegerField()
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'riwayat_naik_gaji'
        unique_together = (('id', 'pangkatjabatan', 'gapok'),)


class RiwayatPendidikan(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    pendidikan = models.CharField(max_length=11)
    sekolah = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=40)
    thn_lulus = models.TextField()  # This field type is a guess.
    kepala = models.CharField(max_length=50)
    pendanaan = models.CharField(max_length=28)
    keterangan = models.CharField(max_length=50)
    status = models.CharField(max_length=40)
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'riwayat_pendidikan'
        unique_together = (('id', 'pendidikan', 'sekolah'),)


class RiwayatPenelitian(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    jenis_penelitian = models.CharField(max_length=30)
    peranan = models.CharField(max_length=30)
    judul_penelitian = models.CharField(max_length=60)
    judul_jurnal = models.CharField(max_length=60)
    tahun = models.TextField()  # This field type is a guess.
    biaya_penelitian = models.FloatField(blank=True, null=True)
    asal_dana = models.CharField(max_length=30)
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'riwayat_penelitian'
        unique_together = (('id', 'judul_penelitian', 'tahun'),)


class RiwayatPenghargaan(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    jenis = models.CharField(max_length=30)
    nama_penghargaan = models.CharField(max_length=60)
    tanggal = models.DateField()
    instansi = models.CharField(max_length=40)
    pejabat_pemberi = models.CharField(max_length=40)
    berkas = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'riwayat_penghargaan'
        unique_together = (('id', 'nama_penghargaan', 'tanggal'),)


class RiwayatSeminar(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    tingkat = models.CharField(max_length=13)
    jenis = models.CharField(max_length=9)
    nama_seminar = models.CharField(max_length=50)
    peranan = models.CharField(max_length=40)
    mulai = models.DateField()
    selesai = models.DateField()
    penyelengara = models.CharField(max_length=50)
    tempat = models.CharField(max_length=50)
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'riwayat_seminar'
        unique_together = (('id', 'nama_seminar', 'mulai'),)


class Rujuk(models.Model):
    no_rujuk = models.CharField(max_length=40)
    no_rawat = models.ForeignKey(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat', blank=True, null=True)
    rujuk_ke = models.CharField(max_length=150, blank=True, null=True)
    tgl_rujuk = models.DateField(blank=True, null=True)
    keterangan_diagnosa = models.TextField(blank=True, null=True)
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter', blank=True, null=True)
    kat_rujuk = models.CharField(max_length=9, blank=True, null=True)
    ambulance = models.CharField(max_length=7, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rujuk'


class RujukMasuk(models.Model):
    no_rawat = models.OneToOneField(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    perujuk = models.CharField(max_length=60, blank=True, null=True)
    alamat = models.CharField(max_length=70)
    no_rujuk = models.CharField(max_length=40)
    jm_perujuk = models.FloatField()
    dokter_perujuk = models.CharField(max_length=50, blank=True, null=True)
    kd_penyakit = models.ForeignKey(Penyakit, on_delete = models.CASCADE, db_column='kd_penyakit', blank=True, null=True)
    kategori_rujuk = models.CharField(max_length=9, blank=True, null=True)
    keterangan = models.CharField(max_length=200, blank=True, null=True)
    no_balasan = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rujuk_masuk'


class RujukanInternalPoli(models.Model):
    no_rawat = models.OneToOneField(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')
    kd_poli = models.ForeignKey(Poliklinik, on_delete = models.CASCADE, db_column='kd_poli', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rujukan_internal_poli'
        unique_together = (('no_rawat', 'kd_dokter'),)


class RujukanranapDokterRs(models.Model):
    tanggal = models.DateField(primary_key=True)
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter')
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis')
    kd_kamar = models.ForeignKey(Kamar, on_delete = models.CASCADE, db_column='kd_kamar')
    jasarujuk = models.FloatField()

    class Meta:
        managed = True
        db_table = 'rujukanranap_dokter_rs'
        unique_together = (('tanggal', 'kd_dokter', 'no_rkm_medis', 'kd_kamar'),)


class Runtext(models.Model):
    teks = models.TextField()
    aktifkan = models.CharField(max_length=3)
    gambar = models.TextField()

    class Meta:
        managed = True
        db_table = 'runtext'


class Runtextapotek(models.Model):
    teks = models.TextField()
    aktifkan = models.CharField(max_length=3)
    gambar = models.TextField()

    class Meta:
        managed = True
        db_table = 'runtextapotek'


class SaranKesanLab(models.Model):
    no_rawat = models.OneToOneField(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    saran = models.CharField(max_length=700, blank=True, null=True)
    kesan = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'saran_kesan_lab'
        unique_together = (('no_rawat', 'tgl_periksa', 'jam'),)


class SatuanPolri(models.Model):
    nama_satuan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'satuan_polri'


class SatuanTni(models.Model):
    nama_satuan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'satuan_tni'


class SetAkte(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    pendapatan_akte = models.FloatField()
    persen_rs = models.FloatField()
    bagian_rs = models.FloatField()
    persen_kry = models.FloatField()
    bagian_kry = models.FloatField()

    class Meta:
        managed = True
        db_table = 'set_akte'
        unique_together = (('tahun', 'bulan'),)


class SetAkun(models.Model):
    pengadaan_obat = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Pengadaan_Obat', blank=True, null=True)  # Field name made lowercase.
    pemesanan_obat = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Pemesanan_Obat', blank=True, null=True)  # Field name made lowercase.
    kontra_pemesanan_obat = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kontra_Pemesanan_Obat', blank=True, null=True)  # Field name made lowercase.
    bayar_pemesanan_obat = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Bayar_Pemesanan_Obat', blank=True, null=True)  # Field name made lowercase.
    penjualan_obat = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Penjualan_Obat', blank=True, null=True)  # Field name made lowercase.
    piutang_obat = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Piutang_Obat', blank=True, null=True)  # Field name made lowercase.
    kontra_piutang_obat = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kontra_Piutang_Obat', blank=True, null=True)  # Field name made lowercase.
    retur_ke_suplayer = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Retur_Ke_Suplayer', blank=True, null=True)  # Field name made lowercase.
    kontra_retur_ke_suplayer = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kontra_Retur_Ke_Suplayer', blank=True, null=True)  # Field name made lowercase.
    retur_dari_pembeli = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Retur_Dari_pembeli', blank=True, null=True)  # Field name made lowercase.
    kontra_retur_dari_pembeli = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kontra_Retur_Dari_Pembeli', blank=True, null=True)  # Field name made lowercase.
    retur_piutang_obat = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Retur_Piutang_Obat', blank=True, null=True)  # Field name made lowercase.
    kontra_retur_piutang_obat = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kontra_Retur_Piutang_Obat', blank=True, null=True)  # Field name made lowercase.
    pengadaan_ipsrs = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Pengadaan_Ipsrs', blank=True, null=True)  # Field name made lowercase.
    stok_keluar_ipsrs = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Stok_Keluar_Ipsrs', blank=True, null=True)  # Field name made lowercase.
    kontra_stok_keluar_ipsrs = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kontra_Stok_Keluar_Ipsrs', blank=True, null=True)  # Field name made lowercase.
    bayar_piutang_pasien = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Bayar_Piutang_Pasien', blank=True, null=True)  # Field name made lowercase.
    pengambilan_utd = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Pengambilan_Utd', blank=True, null=True)  # Field name made lowercase.
    kontra_pengambilan_utd = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kontra_Pengambilan_Utd', blank=True, null=True)  # Field name made lowercase.
    pengambilan_penunjang_utd = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Pengambilan_Penunjang_Utd', blank=True, null=True)  # Field name made lowercase.
    kontra_pengambilan_penunjang_utd = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kontra_Pengambilan_Penunjang_Utd', blank=True, null=True)  # Field name made lowercase.
    penyerahan_darah = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Penyerahan_Darah', blank=True, null=True)  # Field name made lowercase.
    stok_keluar_medis = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Stok_Keluar_Medis')  # Field name made lowercase.
    kontra_stok_keluar_medis = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kontra_Stok_Keluar_Medis')  # Field name made lowercase.
    hpp_obat_jual_bebas = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='HPP_Obat_Jual_Bebas', blank=True, null=True)  # Field name made lowercase.
    persediaan_obat_jual_bebas = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Persediaan_Obat_Jual_Bebas', blank=True, null=True)  # Field name made lowercase.
    penerimaan_nonmedis = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Penerimaan_NonMedis')  # Field name made lowercase.
    kontra_penerimaan_nonmedis = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kontra_Penerimaan_NonMedis')  # Field name made lowercase.
    bayar_pemesanan_non_medis = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Bayar_Pemesanan_Non_Medis')  # Field name made lowercase.
    hibah_obat = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Hibah_Obat')  # Field name made lowercase.
    kontra_hibah_obat = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kontra_Hibah_Obat')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'set_akun'


class SetAkunRalan(models.Model):
    tindakan_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_tindakan_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Dokter_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_jasa_medik_dokter_tindakan_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Dokter_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_paramedis_tindakan_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Paramedis_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_jasa_medik_paramedis_tindakan_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Paramedis_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_kso_tindakan_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_KSO_Tindakan_Ralan')  # Field name made lowercase.
    utang_kso_tindakan_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_KSO_Tindakan_Ralan')  # Field name made lowercase.
    laborat_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_laborat_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Dokter_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_jasa_medik_dokter_laborat_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Dokter_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_petugas_laborat_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Petugas_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_jasa_medik_petugas_laborat_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Petugas_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_kso_laborat_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Kso_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_kso_laborat_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Kso_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    hpp_persediaan_laborat_rawat_jalan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='HPP_Persediaan_Laborat_Rawat_Jalan', blank=True, null=True)  # Field name made lowercase.
    persediaan_bhp_laborat_rawat_jalan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Persediaan_BHP_Laborat_Rawat_Jalan', blank=True, null=True)  # Field name made lowercase.
    radiologi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Radiologi_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_radiologi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Dokter_Radiologi_Ralan')  # Field name made lowercase.
    utang_jasa_medik_dokter_radiologi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Dokter_Radiologi_Ralan')  # Field name made lowercase.
    beban_jasa_medik_petugas_radiologi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Petugas_Radiologi_Ralan')  # Field name made lowercase.
    utang_jasa_medik_petugas_radiologi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Petugas_Radiologi_Ralan')  # Field name made lowercase.
    beban_kso_radiologi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Kso_Radiologi_Ralan')  # Field name made lowercase.
    utang_kso_radiologi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Kso_Radiologi_Ralan')  # Field name made lowercase.
    hpp_persediaan_radiologi_rawat_jalan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='HPP_Persediaan_Radiologi_Rawat_Jalan')  # Field name made lowercase.
    persediaan_bhp_radiologi_rawat_jalan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Persediaan_BHP_Radiologi_Rawat_Jalan')  # Field name made lowercase.
    obat_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Obat_Ralan', blank=True, null=True)  # Field name made lowercase.
    hpp_obat_rawat_jalan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='HPP_Obat_Rawat_Jalan')  # Field name made lowercase.
    persediaan_obat_rawat_jalan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Persediaan_Obat_Rawat_Jalan')  # Field name made lowercase.
    registrasi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Registrasi_Ralan', blank=True, null=True)  # Field name made lowercase.
    operasi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Operasi_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_operasi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Dokter_Operasi_Ralan')  # Field name made lowercase.
    utang_jasa_medik_dokter_operasi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Dokter_Operasi_Ralan')  # Field name made lowercase.
    beban_jasa_medik_paramedis_operasi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Paramedis_Operasi_Ralan')  # Field name made lowercase.
    utang_jasa_medik_paramedis_operasi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Paramedis_Operasi_Ralan')  # Field name made lowercase.
    hpp_obat_operasi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='HPP_Obat_Operasi_Ralan')  # Field name made lowercase.
    persediaan_obat_kamar_operasi_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Persediaan_Obat_Kamar_Operasi_Ralan')  # Field name made lowercase.
    tambahan_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Tambahan_Ralan', blank=True, null=True)  # Field name made lowercase.
    potongan_ralan = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Potongan_Ralan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'set_akun_ralan'


class SetAkunRanap(models.Model):
    suspen_piutang_tindakan_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Suspen_Piutang_Tindakan_Ranap')  # Field name made lowercase.
    tindakan_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Tindakan_Ranap', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_tindakan_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Dokter_Tindakan_Ranap')  # Field name made lowercase.
    utang_jasa_medik_dokter_tindakan_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Dokter_Tindakan_Ranap')  # Field name made lowercase.
    beban_jasa_medik_paramedis_tindakan_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Paramedis_Tindakan_Ranap')  # Field name made lowercase.
    utang_jasa_medik_paramedis_tindakan_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Paramedis_Tindakan_Ranap')  # Field name made lowercase.
    beban_kso_tindakan_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_KSO_Tindakan_Ranap')  # Field name made lowercase.
    utang_kso_tindakan_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_KSO_Tindakan_Ranap')  # Field name made lowercase.
    suspen_piutang_laborat_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Suspen_Piutang_Laborat_Ranap')  # Field name made lowercase.
    laborat_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Laborat_Ranap', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_laborat_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Dokter_Laborat_Ranap')  # Field name made lowercase.
    utang_jasa_medik_dokter_laborat_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Dokter_Laborat_Ranap')  # Field name made lowercase.
    beban_jasa_medik_petugas_laborat_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Petugas_Laborat_Ranap')  # Field name made lowercase.
    utang_jasa_medik_petugas_laborat_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Petugas_Laborat_Ranap')  # Field name made lowercase.
    beban_kso_laborat_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Kso_Laborat_Ranap')  # Field name made lowercase.
    utang_kso_laborat_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Kso_Laborat_Ranap')  # Field name made lowercase.
    hpp_persediaan_laborat_rawat_inap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='HPP_Persediaan_Laborat_Rawat_inap')  # Field name made lowercase.
    persediaan_bhp_laborat_rawat_inap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Persediaan_BHP_Laborat_Rawat_Inap')  # Field name made lowercase.
    suspen_piutang_radiologi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Suspen_Piutang_Radiologi_Ranap')  # Field name made lowercase.
    radiologi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Radiologi_Ranap', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_radiologi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Dokter_Radiologi_Ranap')  # Field name made lowercase.
    utang_jasa_medik_dokter_radiologi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Dokter_Radiologi_Ranap')  # Field name made lowercase.
    beban_jasa_medik_petugas_radiologi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Petugas_Radiologi_Ranap')  # Field name made lowercase.
    utang_jasa_medik_petugas_radiologi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Petugas_Radiologi_Ranap')  # Field name made lowercase.
    beban_kso_radiologi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Kso_Radiologi_Ranap')  # Field name made lowercase.
    utang_kso_radiologi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Kso_Radiologi_Ranap')  # Field name made lowercase.
    hpp_persediaan_radiologi_rawat_inap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='HPP_Persediaan_Radiologi_Rawat_Inap')  # Field name made lowercase.
    persediaan_bhp_radiologi_rawat_inap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Persediaan_BHP_Radiologi_Rawat_Inap')  # Field name made lowercase.
    suspen_piutang_obat_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Suspen_Piutang_Obat_Ranap')  # Field name made lowercase.
    obat_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Obat_Ranap', blank=True, null=True)  # Field name made lowercase.
    hpp_obat_rawat_inap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='HPP_Obat_Rawat_Inap')  # Field name made lowercase.
    persediaan_obat_rawat_inap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Persediaan_Obat_Rawat_Inap')  # Field name made lowercase.
    registrasi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Registrasi_Ranap', blank=True, null=True)  # Field name made lowercase.
    service_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Service_Ranap', blank=True, null=True)  # Field name made lowercase.
    tambahan_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Tambahan_Ranap', blank=True, null=True)  # Field name made lowercase.
    potongan_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Potongan_Ranap', blank=True, null=True)  # Field name made lowercase.
    retur_obat_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Retur_Obat_Ranap', blank=True, null=True)  # Field name made lowercase.
    resep_pulang_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Resep_Pulang_Ranap', blank=True, null=True)  # Field name made lowercase.
    kamar_inap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Kamar_Inap', blank=True, null=True)  # Field name made lowercase.
    suspen_piutang_operasi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Suspen_Piutang_Operasi_Ranap')  # Field name made lowercase.
    operasi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Operasi_Ranap', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_operasi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Dokter_Operasi_Ranap')  # Field name made lowercase.
    utang_jasa_medik_dokter_operasi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Dokter_Operasi_Ranap')  # Field name made lowercase.
    beban_jasa_medik_paramedis_operasi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Beban_Jasa_Medik_Paramedis_Operasi_Ranap')  # Field name made lowercase.
    utang_jasa_medik_paramedis_operasi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Utang_Jasa_Medik_Paramedis_Operasi_Ranap')  # Field name made lowercase.
    hpp_obat_operasi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='HPP_Obat_Operasi_Ranap')  # Field name made lowercase.
    persediaan_obat_kamar_operasi_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Persediaan_Obat_Kamar_Operasi_Ranap')  # Field name made lowercase.
    harian_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Harian_Ranap', blank=True, null=True)  # Field name made lowercase.
    uang_muka_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Uang_Muka_Ranap', blank=True, null=True)  # Field name made lowercase.
    piutang_pasien_ranap = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='Piutang_Pasien_Ranap', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'set_akun_ranap'


class SetAlamatPasien(models.Model):
    kelurahan = models.CharField(max_length=5, blank=True, null=True)
    kecamatan = models.CharField(max_length=5, blank=True, null=True)
    kabupaten = models.CharField(max_length=5, blank=True, null=True)
    propinsi = models.CharField(max_length=5)

    class Meta:
        managed = True
        db_table = 'set_alamat_pasien'


class SetDepoRalan(models.Model):
    kd_poli = models.OneToOneField(Poliklinik, on_delete = models.CASCADE, db_column='kd_poli', primary_key=True)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')

    class Meta:
        managed = True
        db_table = 'set_depo_ralan'
        unique_together = (('kd_poli', 'kd_bangsal'),)


class SetDepoRanap(models.Model):
    kd_bangsal = models.OneToOneField(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal', primary_key=True)
    kd_depo = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_depo')

    class Meta:
        managed = True
        db_table = 'set_depo_ranap'
        unique_together = (('kd_bangsal', 'kd_depo'),)


class SetEmbalase(models.Model):
    embalase_per_obat = models.FloatField()
    tuslah_per_obat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'set_embalase'


class SetHadir(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'set_hadir'


class SetHargaKamar(models.Model):
    kd_kamar = models.OneToOneField(Kamar, on_delete = models.CASCADE, db_column='kd_kamar', primary_key=True)
    kd_pj = models.ForeignKey(Penjab, on_delete = models.CASCADE, db_column='kd_pj')
    tarif = models.FloatField()

    class Meta:
        managed = True
        db_table = 'set_harga_kamar'
        unique_together = (('kd_kamar', 'kd_pj'),)


class SetHargaObat(models.Model):
    setharga = models.CharField(max_length=10)
    hargadasar = models.CharField(max_length=12)

    class Meta:
        managed = True
        db_table = 'set_harga_obat'


class SetHargaObatRalan(models.Model):
    kd_pj = models.OneToOneField(Penjab, on_delete = models.CASCADE, db_column='kd_pj', primary_key=True)
    hargajual = models.FloatField()

    class Meta:
        managed = True
        db_table = 'set_harga_obat_ralan'


class SetHargaObatRanap(models.Model):
    kd_pj = models.OneToOneField(Penjab, on_delete = models.CASCADE, db_column='kd_pj', primary_key=True)
    kelas = models.CharField(max_length=11)
    hargajual = models.FloatField()

    class Meta:
        managed = True
        db_table = 'set_harga_obat_ranap'
        unique_together = (('kd_pj', 'kelas'),)


class SetHariLibur(models.Model):
    tanggal = models.DateField(primary_key=True)
    ktg = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'set_hari_libur'


class SetInputParsial(models.Model):
    kd_pj = models.OneToOneField(Penjab, on_delete = models.CASCADE, db_column='kd_pj', primary_key=True)

    class Meta:
        managed = True
        db_table = 'set_input_parsial'


class SetInsentif(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    pendapatan = models.FloatField()
    persen = models.FloatField()
    total_insentif = models.FloatField()

    class Meta:
        managed = True
        db_table = 'set_insentif'
        unique_together = (('tahun', 'bulan'),)


class SetJamMinimal(models.Model):
    lamajam = models.IntegerField()
    hariawal = models.CharField(max_length=3)
    feeperujuk = models.FloatField()
    diagnosaakhir = models.CharField(max_length=3, blank=True, null=True)
    bayi = models.IntegerField(blank=True, null=True)
    aktifkan_hapus_data_salah = models.CharField(max_length=3, blank=True, null=True)
    kamar_inap_kasir_ralan = models.CharField(max_length=3, blank=True, null=True)
    ubah_status_kamar = models.CharField(max_length=3)

    class Meta:
        managed = True
        db_table = 'set_jam_minimal'


class SetJgmlm(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'set_jgmlm'


class SetJgtambah(models.Model):
    tnj = models.FloatField()
    pendidikan = models.OneToOneField(Pendidikan, on_delete = models.CASCADE, db_column='pendidikan', primary_key=True)

    class Meta:
        managed = True
        db_table = 'set_jgtambah'


class SetKelengkapanDataPasien(models.Model):
    no_ktp = models.CharField(max_length=3, blank=True, null=True)
    p_no_ktp = models.IntegerField(blank=True, null=True)
    tmp_lahir = models.CharField(max_length=3, blank=True, null=True)
    p_tmp_lahir = models.IntegerField(blank=True, null=True)
    nm_ibu = models.CharField(max_length=3, blank=True, null=True)
    p_nm_ibu = models.IntegerField(blank=True, null=True)
    alamat = models.CharField(max_length=3, blank=True, null=True)
    p_alamat = models.IntegerField(blank=True, null=True)
    pekerjaan = models.CharField(max_length=3, blank=True, null=True)
    p_pekerjaan = models.IntegerField(blank=True, null=True)
    no_tlp = models.CharField(max_length=3, blank=True, null=True)
    p_no_tlp = models.IntegerField(blank=True, null=True)
    umur = models.CharField(max_length=3, blank=True, null=True)
    p_umur = models.IntegerField(blank=True, null=True)
    namakeluarga = models.CharField(max_length=3, blank=True, null=True)
    p_namakeluarga = models.IntegerField(blank=True, null=True)
    no_peserta = models.CharField(max_length=3, blank=True, null=True)
    p_no_peserta = models.IntegerField(blank=True, null=True)
    kelurahan = models.CharField(max_length=3, blank=True, null=True)
    p_kelurahan = models.IntegerField(blank=True, null=True)
    kecamatan = models.CharField(max_length=3, blank=True, null=True)
    p_kecamatan = models.IntegerField(blank=True, null=True)
    kabupaten = models.CharField(max_length=3, blank=True, null=True)
    p_kabupaten = models.IntegerField(blank=True, null=True)
    pekerjaanpj = models.CharField(max_length=3, blank=True, null=True)
    p_pekerjaanpj = models.IntegerField(blank=True, null=True)
    alamatpj = models.CharField(max_length=3, blank=True, null=True)
    p_alamatpj = models.IntegerField(blank=True, null=True)
    kelurahanpj = models.CharField(max_length=3, blank=True, null=True)
    p_kelurahanpj = models.IntegerField(blank=True, null=True)
    kecamatanpj = models.CharField(max_length=3, blank=True, null=True)
    p_kecamatanpj = models.IntegerField(blank=True, null=True)
    kabupatenpj = models.CharField(max_length=3, blank=True, null=True)
    p_kabupatenpj = models.IntegerField(blank=True, null=True)
    propinsi = models.CharField(max_length=3)
    p_propinsi = models.IntegerField()
    propinsipj = models.CharField(max_length=3)
    p_propinsipj = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'set_kelengkapan_data_pasien'


class SetKeterlambatan(models.Model):
    toleransi = models.IntegerField(blank=True, null=True)
    terlambat1 = models.IntegerField(blank=True, null=True)
    terlambat2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'set_keterlambatan'


class SetLemburhb(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'set_lemburhb'


class SetLemburhr(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'set_lemburhr'


class SetLokasi(models.Model):
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')
    asal_stok = models.CharField(max_length=23)

    class Meta:
        managed = True
        db_table = 'set_lokasi'


class SetModalPayment(models.Model):
    modal_awal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'set_modal_payment'


class SetNoRkmMedis(models.Model):
    no_rkm_medis = models.CharField(max_length=15)

    class Meta:
        managed = True
        db_table = 'set_no_rkm_medis'


class SetNota(models.Model):
    notaralan = models.CharField(max_length=11)
    kwitansiralan = models.CharField(max_length=11)
    nota1ranap = models.CharField(max_length=11)
    nota2ranap = models.CharField(max_length=11)
    kwitansiranap = models.CharField(max_length=11)
    notaapotek = models.CharField(max_length=11)
    notalabrad = models.CharField(max_length=11)
    cetaknotasimpanralan = models.CharField(max_length=3)
    cetaknotasimpanranap = models.CharField(max_length=3)
    rinciandokterralan = models.CharField(max_length=3)
    rinciandokterranap = models.CharField(max_length=3)
    centangdokterralan = models.CharField(max_length=3)
    centangdokterranap = models.CharField(max_length=3)
    tampilkan_administrasi_di_billingranap = models.CharField(max_length=3)
    rincianoperasi = models.CharField(max_length=3, blank=True, null=True)
    tampilkan_ppnobat_ralan = models.CharField(max_length=3, blank=True, null=True)
    tampilkan_ppnobat_ranap = models.CharField(max_length=3, blank=True, null=True)
    tampilkan_tombol_nota_ralan = models.CharField(max_length=3, blank=True, null=True)
    tampilkan_tombol_nota_ranap = models.CharField(max_length=3, blank=True, null=True)
    verifikasi_penjualan_di_kasir = models.CharField(max_length=3, blank=True, null=True)
    verifikasi_penyerahan_darah_di_kasir = models.CharField(max_length=3, blank=True, null=True)
    cetaknotasimpanpenjualan = models.CharField(max_length=3, blank=True, null=True)
    tampilkan_tombol_nota_penjualan = models.CharField(max_length=3, blank=True, null=True)
    centangobatralan = models.CharField(max_length=3, blank=True, null=True)
    centangobatranap = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'set_nota'


class SetOtomatisTindakanRalan(models.Model):
    kd_dokter = models.OneToOneField(Dokter, on_delete = models.CASCADE, db_column='kd_dokter', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatan, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    kd_pj = models.ForeignKey(Penjab, on_delete = models.CASCADE, db_column='kd_pj')

    class Meta:
        managed = True
        db_table = 'set_otomatis_tindakan_ralan'
        unique_together = (('kd_dokter', 'kd_jenis_prw', 'kd_pj'),)


class SetOtomatisTindakanRalanDokterpetugas(models.Model):
    kd_dokter = models.OneToOneField(Dokter, on_delete = models.CASCADE, db_column='kd_dokter', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatan, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    kd_pj = models.ForeignKey(Penjab, on_delete = models.CASCADE, db_column='kd_pj')

    class Meta:
        managed = True
        db_table = 'set_otomatis_tindakan_ralan_dokterpetugas'
        unique_together = (('kd_dokter', 'kd_jenis_prw', 'kd_pj'),)


class SetOtomatisTindakanRalanPetugas(models.Model):
    kd_jenis_prw = models.OneToOneField(JnsPerawatan, on_delete = models.CASCADE, db_column='kd_jenis_prw', primary_key=True)
    kd_pj = models.ForeignKey(Penjab, on_delete = models.CASCADE, db_column='kd_pj')

    class Meta:
        managed = True
        db_table = 'set_otomatis_tindakan_ralan_petugas'
        unique_together = (('kd_jenis_prw', 'kd_pj'),)


class SetPjlab(models.Model):
    kd_dokterlab = models.OneToOneField(Dokter, on_delete = models.CASCADE, db_column='kd_dokterlab', primary_key=True)
    kd_dokterrad = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokterrad')
    kd_dokterhemodialisa = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokterhemodialisa')
    kd_dokterutd = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokterutd', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'set_pjlab'
        unique_together = (('kd_dokterlab', 'kd_dokterrad', 'kd_dokterhemodialisa'),)


class SetResume(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    pendapatan_resume = models.FloatField()
    persen_rs = models.FloatField()
    bagian_rs = models.FloatField()
    persen_kry = models.FloatField()
    bagian_kry = models.FloatField()

    class Meta:
        managed = True
        db_table = 'set_resume'
        unique_together = (('tahun', 'bulan'),)


class SetServiceRanap(models.Model):
    nama_service = models.CharField(primary_key=True, max_length=100)
    besar = models.FloatField(blank=True, null=True)
    laborat = models.CharField(max_length=3, blank=True, null=True)
    radiologi = models.CharField(max_length=3, blank=True, null=True)
    operasi = models.CharField(max_length=3, blank=True, null=True)
    obat = models.CharField(max_length=3, blank=True, null=True)
    ranap_dokter = models.CharField(max_length=3, blank=True, null=True)
    ranap_paramedis = models.CharField(max_length=3, blank=True, null=True)
    ralan_dokter = models.CharField(max_length=3, blank=True, null=True)
    ralan_paramedis = models.CharField(max_length=3, blank=True, null=True)
    tambahan = models.CharField(max_length=3, blank=True, null=True)
    potongan = models.CharField(max_length=3, blank=True, null=True)
    kamar = models.CharField(max_length=3, blank=True, null=True)
    registrasi = models.CharField(max_length=3, blank=True, null=True)
    harian = models.CharField(max_length=3, blank=True, null=True)
    retur_obat = models.CharField(db_column='retur_Obat', max_length=3, blank=True, null=True)  # Field name made lowercase.
    resep_pulang = models.CharField(db_column='resep_Pulang', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'set_service_ranap'


class SetServiceRanapPiutang(models.Model):
    nama_service = models.CharField(primary_key=True, max_length=100)
    besar = models.FloatField(blank=True, null=True)
    laborat = models.CharField(max_length=3, blank=True, null=True)
    radiologi = models.CharField(max_length=3, blank=True, null=True)
    operasi = models.CharField(max_length=3, blank=True, null=True)
    obat = models.CharField(max_length=3, blank=True, null=True)
    ranap_dokter = models.CharField(max_length=3, blank=True, null=True)
    ranap_paramedis = models.CharField(max_length=3, blank=True, null=True)
    ralan_dokter = models.CharField(max_length=3, blank=True, null=True)
    ralan_paramedis = models.CharField(max_length=3, blank=True, null=True)
    tambahan = models.CharField(max_length=3, blank=True, null=True)
    potongan = models.CharField(max_length=3, blank=True, null=True)
    kamar = models.CharField(max_length=3, blank=True, null=True)
    registrasi = models.CharField(max_length=3, blank=True, null=True)
    harian = models.CharField(max_length=3, blank=True, null=True)
    retur_obat = models.CharField(db_column='retur_Obat', max_length=3, blank=True, null=True)  # Field name made lowercase.
    resep_pulang = models.CharField(db_column='resep_Pulang', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'set_service_ranap_piutang'


class SetTahun(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    jmlhr = models.IntegerField()
    jmllbr = models.IntegerField()
    normal = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'set_tahun'
        unique_together = (('tahun', 'bulan'),)


class SetTarif(models.Model):
    poli_ralan = models.CharField(max_length=3)
    cara_bayar_ralan = models.CharField(max_length=3)
    ruang_ranap = models.CharField(max_length=3)
    cara_bayar_ranap = models.CharField(max_length=3)
    cara_bayar_lab = models.CharField(max_length=3)
    cara_bayar_radiologi = models.CharField(max_length=3)
    cara_bayar_operasi = models.CharField(max_length=3, blank=True, null=True)
    kelas_ranap = models.CharField(max_length=3)
    kelas_lab = models.CharField(max_length=3)
    kelas_radiologi = models.CharField(max_length=3)
    kelas_operasi = models.CharField(max_length=3)

    class Meta:
        managed = True
        db_table = 'set_tarif'


class SetTniPolri(models.Model):
    tampilkan_tni_polri = models.CharField(max_length=3)

    class Meta:
        managed = True
        db_table = 'set_tni_polri'


class SetTnjanak(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'set_tnjanak'


class SetTnjnikah(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'set_tnjnikah'


class SetTuslah(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    pendapatan_tuslah = models.FloatField()
    persen_rs = models.FloatField()
    bagian_rs = models.FloatField()
    persen_kry = models.FloatField()
    bagian_kry = models.FloatField()

    class Meta:
        managed = True
        db_table = 'set_tuslah'
        unique_together = (('tahun', 'bulan'),)


class SetUrutNoRkmMedis(models.Model):
    urutan = models.CharField(max_length=8)
    tahun = models.CharField(max_length=3)
    bulan = models.CharField(max_length=3)
    posisi_tahun_bulan = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'set_urut_no_rkm_medis'


class SetValidasiCatatan(models.Model):
    tampilkan_catatan = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'set_validasi_catatan'


class SetValidasiRegistrasi(models.Model):
    wajib_closing_kasir = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'set_validasi_registrasi'


class SetWarung(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    pendapatan_warung = models.FloatField()
    persen_rs = models.FloatField()
    bagian_rs = models.FloatField()
    persen_kry = models.FloatField()
    bagian_kry = models.FloatField()

    class Meta:
        managed = True
        db_table = 'set_warung'
        unique_together = (('tahun', 'bulan'),)


class Setpenjualan(models.Model):
    ralan = models.FloatField(blank=True, null=True)
    kelas1 = models.FloatField(blank=True, null=True)
    kelas2 = models.FloatField(blank=True, null=True)
    kelas3 = models.FloatField(blank=True, null=True)
    utama = models.FloatField(blank=True, null=True)
    vip = models.FloatField(blank=True, null=True)
    vvip = models.FloatField(blank=True, null=True)
    beliluar = models.FloatField(blank=True, null=True)
    jualbebas = models.FloatField(blank=True, null=True)
    karyawan = models.FloatField(blank=True, null=True)
    kdjns = models.OneToOneField(Jenis, on_delete = models.CASCADE, db_column='kdjns', primary_key=True)

    class Meta:
        managed = True
        db_table = 'setpenjualan'


class Setpenjualanperbarang(models.Model):
    ralan = models.FloatField(blank=True, null=True)
    kelas1 = models.FloatField(blank=True, null=True)
    kelas2 = models.FloatField(blank=True, null=True)
    kelas3 = models.FloatField(blank=True, null=True)
    utama = models.FloatField(blank=True, null=True)
    vip = models.FloatField(blank=True, null=True)
    vvip = models.FloatField(blank=True, null=True)
    beliluar = models.FloatField(blank=True, null=True)
    jualbebas = models.FloatField(blank=True, null=True)
    karyawan = models.FloatField(blank=True, null=True)
    kode_brng = models.OneToOneField(Databarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)

    class Meta:
        managed = True
        db_table = 'setpenjualanperbarang'


class Setpenjualanumum(models.Model):
    ralan = models.FloatField(blank=True, null=True)
    kelas1 = models.FloatField(blank=True, null=True)
    kelas2 = models.FloatField(blank=True, null=True)
    kelas3 = models.FloatField(blank=True, null=True)
    utama = models.FloatField(blank=True, null=True)
    vip = models.FloatField(blank=True, null=True)
    vvip = models.FloatField(blank=True, null=True)
    beliluar = models.FloatField(blank=True, null=True)
    jualbebas = models.FloatField(blank=True, null=True)
    karyawan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'setpenjualanumum'


class Setsms(models.Model):
    kode_sms = models.CharField(primary_key=True, max_length=200)
    sintax_balasan = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'setsms'


class Setting(models.Model):
    nama_instansi = models.CharField(primary_key=True, max_length=60)
    alamat_instansi = models.CharField(max_length=150, blank=True, null=True)
    kabupaten = models.CharField(max_length=30, blank=True, null=True)
    propinsi = models.CharField(max_length=30, blank=True, null=True)
    kontak = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    aktifkan = models.CharField(max_length=3)
    kode_ppk = models.CharField(max_length=15, blank=True, null=True)
    kode_ppkinhealth = models.CharField(max_length=15, blank=True, null=True)
    kode_ppkkemenkes = models.CharField(max_length=15, blank=True, null=True)
    wallpaper = models.TextField(blank=True, null=True)
    logo = models.TextField()

    class Meta:
        managed = True
        db_table = 'setting'


class Sidikjari(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    sidikjari = models.TextField()

    class Meta:
        managed = True
        db_table = 'sidikjari'


class Sidikjaripasien(models.Model):
    no_rkm_medis = models.OneToOneField(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis', primary_key=True)
    sidikjari = models.TextField()

    class Meta:
        managed = True
        db_table = 'sidikjaripasien'


class SiranapKetersediaanKamar(models.Model):
    kode_ruang_siranap = models.CharField(primary_key=True, max_length=29)
    kelas_ruang_siranap = models.CharField(max_length=21)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')
    kelas = models.CharField(max_length=11)
    kapasitas = models.IntegerField(blank=True, null=True)
    tersedia = models.IntegerField(blank=True, null=True)
    tersediapria = models.IntegerField(blank=True, null=True)
    tersediawanita = models.IntegerField(blank=True, null=True)
    menunggu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'siranap_ketersediaan_kamar'
        unique_together = (('kode_ruang_siranap', 'kelas_ruang_siranap', 'kd_bangsal', 'kelas'),)


class SisruteRujukanKeluar(models.Model):
    no_rawat = models.OneToOneField(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    no_rujuk = models.CharField(max_length=40)
    no_rkm_medis = models.CharField(max_length=15)
    nm_pasien = models.CharField(max_length=40)
    no_ktp = models.CharField(max_length=20)
    no_peserta = models.CharField(max_length=25)
    jk = models.CharField(max_length=1)
    tgl_lahir = models.DateField()
    tmp_lahir = models.CharField(max_length=15)
    alamat = models.CharField(max_length=200)
    no_tlp = models.CharField(max_length=40)
    jns_rujukan = models.CharField(max_length=21)
    tgl_rujuk = models.DateTimeField()
    kd_faskes_tujuan = models.CharField(max_length=12)
    nm_faskes_tujuan = models.CharField(max_length=200)
    kd_alasan = models.CharField(max_length=5)
    alasan_rujuk = models.CharField(max_length=150)
    alasan_lainnya = models.CharField(max_length=50)
    kd_diagnosa = models.CharField(max_length=10)
    diagnosa_rujuk = models.TextField()
    nik_dokter = models.CharField(max_length=20)
    dokter_perujuk = models.CharField(max_length=50)
    nik_petugas = models.CharField(max_length=20)
    petugas_entry = models.CharField(max_length=50)
    anamnesis_pemeriksaan = models.TextField()
    kesadaran = models.CharField(max_length=14)
    tekanan_darah = models.CharField(max_length=7)
    nadi = models.CharField(max_length=3)
    suhu = models.CharField(max_length=5)
    respirasi = models.CharField(max_length=3)
    keadaan_umum = models.TextField()
    tingkat_nyeri = models.CharField(max_length=14)
    alergi = models.CharField(max_length=50)
    laboratorium = models.TextField()
    radiologi = models.TextField()
    terapitindakan = models.TextField()

    class Meta:
        managed = True
        db_table = 'sisrute_rujukan_keluar'


class SkdpBpjs(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis', blank=True, null=True)
    diagnosa = models.CharField(max_length=50)
    terapi = models.CharField(max_length=50)
    alasan1 = models.CharField(max_length=50, blank=True, null=True)
    alasan2 = models.CharField(max_length=50, blank=True, null=True)
    rtl1 = models.CharField(max_length=50, blank=True, null=True)
    rtl2 = models.CharField(max_length=50, blank=True, null=True)
    tanggal_datang = models.DateField(blank=True, null=True)
    tanggal_rujukan = models.DateField()
    no_antrian = models.CharField(max_length=6)
    kd_dokter = models.ForeignKey(Dokter, on_delete = models.CASCADE, db_column='kd_dokter', blank=True, null=True)
    status = models.CharField(max_length=13)

    class Meta:
        managed = True
        db_table = 'skdp_bpjs'
        unique_together = (('tahun', 'no_antrian'),)


class SkriningRawatJalan(models.Model):
    tanggal = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rkm_medis = models.ForeignKey(Pasien, on_delete = models.CASCADE, db_column='no_rkm_medis')
    geriatri = models.CharField(max_length=5, blank=True, null=True)
    kesadaran = models.CharField(max_length=43, blank=True, null=True)
    pernapasan = models.CharField(max_length=14, blank=True, null=True)
    nyeri_dada = models.CharField(max_length=31, blank=True, null=True)
    skala_nyeri = models.CharField(max_length=20, blank=True, null=True)
    keputusan = models.CharField(max_length=14, blank=True, null=True)
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'skrining_rawat_jalan'
        unique_together = (('tanggal', 'jam', 'no_rkm_medis'),)


class Sms(models.Model):
    id_pesan = models.AutoField(primary_key=True)
    sms_masuk = models.CharField(max_length=255, blank=True, null=True)
    no_hp = models.CharField(max_length=15, blank=True, null=True)
    pdu_pesan = models.CharField(max_length=255, blank=True, null=True)
    encoding = models.CharField(max_length=20, blank=True, null=True)
    id_gateway = models.CharField(max_length=20, blank=True, null=True)
    tgl_sms = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sms'


class Spesialis(models.Model):
    kd_sps = models.CharField(primary_key=True, max_length=5)
    nm_sps = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'spesialis'


class StokObatPasien(models.Model):
    tanggal = models.DateField(primary_key=True)
    no_rawat = models.ForeignKey(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat')
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    jumlah = models.FloatField()
    kd_bangsal = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal')
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'stok_obat_pasien'
        unique_together = (('tanggal', 'no_rawat', 'kode_brng', 'no_batch', 'no_faktur'),)


class SttsKerja(models.Model):
    stts = models.CharField(primary_key=True, max_length=3)
    ktg = models.CharField(max_length=20)
    indek = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'stts_kerja'


class SttsWp(models.Model):
    stts = models.CharField(primary_key=True, max_length=5)
    ktg = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'stts_wp'


class Subrekening(models.Model):
    kd_rek = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='kd_rek')
    kd_rek2 = models.OneToOneField(Rekening, on_delete = models.CASCADE, db_column='kd_rek2', primary_key=True)

    class Meta:
        managed = True
        db_table = 'subrekening'


class SukuBangsa(models.Model):
    nama_suku_bangsa = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'suku_bangsa'


class SuratBalas(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    balas = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'surat_balas'


class SuratIndeks(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    indeks = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'surat_indeks'


class SuratKeluar(models.Model):
    no_urut = models.CharField(primary_key=True, max_length=15)
    no_surat = models.CharField(max_length=50)
    tujuan = models.CharField(max_length=300)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=300)
    tgl_kirim = models.DateField()
    kd_lemari = models.ForeignKey('SuratLemari', on_delete = models.CASCADE, db_column='kd_lemari')
    kd_rak = models.ForeignKey('SuratRak', on_delete = models.CASCADE, db_column='kd_rak')
    kd_map = models.ForeignKey('SuratMap', on_delete = models.CASCADE, db_column='kd_map')
    kd_ruang = models.ForeignKey('SuratRuang', on_delete = models.CASCADE, db_column='kd_ruang')
    kd_sifat = models.ForeignKey('SuratSifat', on_delete = models.CASCADE, db_column='kd_sifat')
    lampiran = models.CharField(max_length=300)
    tembusan = models.CharField(max_length=300)
    tgl_deadline_balas = models.DateField()
    kd_balas = models.ForeignKey(SuratBalas, on_delete = models.CASCADE, db_column='kd_balas')
    keterangan = models.CharField(max_length=300)
    kd_status = models.ForeignKey('SuratStatus', on_delete = models.CASCADE, db_column='kd_status')
    kd_klasifikasi = models.ForeignKey('SuratKlasifikasi', on_delete = models.CASCADE, db_column='kd_klasifikasi')
    file_url = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'surat_keluar'


class SuratKeluarDisposisi(models.Model):
    no_disposisi = models.CharField(primary_key=True, max_length=15)
    kd_indeks = models.ForeignKey(SuratIndeks, on_delete = models.CASCADE, db_column='kd_indeks')
    no_urut = models.ForeignKey(SuratKeluar, on_delete = models.CASCADE, db_column='no_urut')
    tgl_selesai = models.DateField()
    isi = models.CharField(max_length=300)
    diteruskan = models.CharField(max_length=300)
    tgl_kembali = models.DateField()
    kepada = models.CharField(max_length=100)
    pengesahan = models.CharField(max_length=5)
    harap = models.CharField(max_length=300)
    catatan = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = 'surat_keluar_disposisi'


class SuratKeluarKendali(models.Model):
    no_kendali = models.CharField(primary_key=True, max_length=15)
    kd_indeks = models.ForeignKey(SuratIndeks, on_delete = models.CASCADE, db_column='kd_indeks')
    no_urut = models.ForeignKey(SuratKeluar, on_delete = models.CASCADE, db_column='no_urut')
    tgl_selesai = models.DateField()
    tgl_kembali = models.DateField()
    kepada = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'surat_keluar_kendali'


class SuratKeluarSetNomor(models.Model):
    id_no_surat = models.AutoField(primary_key=True)
    jenis_surat = models.CharField(max_length=100)
    digit_1 = models.CharField(max_length=26, blank=True, null=True)
    digit_2 = models.CharField(max_length=26, blank=True, null=True)
    digit_3 = models.CharField(max_length=26, blank=True, null=True)
    digit_4 = models.CharField(max_length=26, blank=True, null=True)
    digit_5 = models.CharField(max_length=26, blank=True, null=True)
    digit_6 = models.CharField(max_length=26, blank=True, null=True)
    digit_7 = models.CharField(max_length=26, blank=True, null=True)
    digit_8 = models.CharField(max_length=26, blank=True, null=True)
    digit_9 = models.CharField(max_length=26, blank=True, null=True)
    digit_10 = models.CharField(max_length=26, blank=True, null=True)
    digit_11 = models.CharField(max_length=26, blank=True, null=True)
    digit_12 = models.CharField(max_length=26, blank=True, null=True)
    digit_13 = models.CharField(max_length=26, blank=True, null=True)
    digit_14 = models.CharField(max_length=26, blank=True, null=True)
    digit_15 = models.CharField(max_length=26, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'surat_keluar_set_nomor'


class SuratKlasifikasi(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    klasifikasi = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'surat_klasifikasi'


class SuratLemari(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    lemari = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'surat_lemari'


class SuratMap(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    map = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'surat_map'


class SuratMasuk(models.Model):
    no_urut = models.CharField(primary_key=True, max_length=15)
    no_surat = models.CharField(max_length=50)
    asal = models.CharField(max_length=300)
    tujuan = models.CharField(max_length=300)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=300)
    tgl_terima = models.DateField()
    kd_lemari = models.ForeignKey(SuratLemari, on_delete = models.CASCADE, db_column='kd_lemari')
    kd_rak = models.ForeignKey('SuratRak', on_delete = models.CASCADE, db_column='kd_rak')
    kd_map = models.ForeignKey(SuratMap, on_delete = models.CASCADE, db_column='kd_map')
    kd_ruang = models.ForeignKey('SuratRuang', on_delete = models.CASCADE, db_column='kd_ruang')
    kd_sifat = models.ForeignKey('SuratSifat', on_delete = models.CASCADE, db_column='kd_sifat')
    lampiran = models.CharField(max_length=300)
    tembusan = models.CharField(max_length=300)
    tgl_deadline_balas = models.DateField()
    kd_balas = models.ForeignKey(SuratBalas, on_delete = models.CASCADE, db_column='kd_balas')
    keterangan = models.CharField(max_length=300)
    kd_status = models.ForeignKey('SuratStatus', on_delete = models.CASCADE, db_column='kd_status')
    kd_klasifikasi = models.ForeignKey(SuratKlasifikasi, on_delete = models.CASCADE, db_column='kd_klasifikasi')
    file_url = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'surat_masuk'


class SuratMasukDisposisi(models.Model):
    no_disposisi = models.CharField(primary_key=True, max_length=15)
    kd_indeks = models.ForeignKey(SuratIndeks, on_delete = models.CASCADE, db_column='kd_indeks')
    no_urut = models.ForeignKey(SuratMasuk, on_delete = models.CASCADE, db_column='no_urut')
    tgl_selesai = models.DateField()
    isi = models.CharField(max_length=300)
    diteruskan = models.CharField(max_length=300)
    tgl_kembali = models.DateField()
    kepada = models.CharField(max_length=100)
    pengesahan = models.CharField(max_length=5)
    harap = models.CharField(max_length=300)
    catatan = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = 'surat_masuk_disposisi'


class SuratMasukKendali(models.Model):
    no_kendali = models.CharField(primary_key=True, max_length=15)
    kd_indeks = models.ForeignKey(SuratIndeks, on_delete = models.CASCADE, db_column='kd_indeks')
    no_urut = models.ForeignKey(SuratMasuk, on_delete = models.CASCADE, db_column='no_urut')
    tgl_selesai = models.DateField()
    tgl_kembali = models.DateField()
    kepada = models.CharField(max_length=100)
    pengesahan = models.CharField(max_length=5)

    class Meta:
        managed = True
        db_table = 'surat_masuk_kendali'


class SuratPemesananMedis(models.Model):
    no_pemesanan = models.CharField(primary_key=True, max_length=20)
    kode_suplier = models.ForeignKey(Datasuplier, on_delete = models.CASCADE, db_column='kode_suplier', blank=True, null=True)
    nip = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    total1 = models.FloatField()
    potongan = models.FloatField()
    total2 = models.FloatField()
    ppn = models.FloatField(blank=True, null=True)
    meterai = models.FloatField(blank=True, null=True)
    tagihan = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'surat_pemesanan_medis'


class SuratPemesananNonMedis(models.Model):
    no_pemesanan = models.CharField(primary_key=True, max_length=20)
    kode_suplier = models.ForeignKey(Ipsrssuplier, on_delete = models.CASCADE, db_column='kode_suplier', blank=True, null=True)
    nip = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    subtotal = models.FloatField()
    potongan = models.FloatField()
    total = models.FloatField()
    ppn = models.FloatField(blank=True, null=True)
    meterai = models.FloatField(blank=True, null=True)
    tagihan = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'surat_pemesanan_non_medis'


class SuratRak(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    rak = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'surat_rak'


class SuratRuang(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    ruang = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'surat_ruang'


class SuratSifat(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    sifat = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'surat_sifat'


class SuratStatus(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    status = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'surat_status'


class SuratSubKlasifikasi(models.Model):
    kd = models.CharField(primary_key=True, max_length=10)
    kd_klasifikasi = models.ForeignKey(SuratKlasifikasi, on_delete = models.CASCADE, db_column='kd_klasifikasi')
    sub_klasifikasi = models.CharField(max_length=50)
    no_bulanan = models.IntegerField(blank=True, null=True)
    no_tahunan = models.IntegerField(blank=True, null=True)
    bulan = models.IntegerField()
    tahun = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'surat_sub_klasifikasi'


class Suratsakit(models.Model):
    no_surat = models.CharField(max_length=17)
    no_rawat = models.ForeignKey(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat', blank=True, null=True)
    tanggalawal = models.DateField(blank=True, null=True)
    tanggalakhir = models.DateField(blank=True, null=True)
    lamasakit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'suratsakit'


class TagihanObatLangsung(models.Model):
    no_rawat = models.ForeignKey(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat')
    besar_tagihan = models.FloatField()

    class Meta:
        managed = True
        db_table = 'tagihan_obat_langsung'


class TagihanSadewa(models.Model):
    no_nota = models.CharField(primary_key=True, max_length=17)
    no_rkm_medis = models.CharField(max_length=15)
    nama_pasien = models.CharField(max_length=60)
    alamat = models.CharField(max_length=200)
    tgl_bayar = models.DateTimeField()
    jenis_bayar = models.CharField(max_length=9)
    jumlah_tagihan = models.FloatField()
    jumlah_bayar = models.FloatField()
    status = models.CharField(max_length=5)
    petugas = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tagihan_sadewa'


class TambahanBiaya(models.Model):
    no_rawat = models.OneToOneField(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat', primary_key=True)
    nama_biaya = models.CharField(max_length=60)
    besar_biaya = models.FloatField()

    class Meta:
        managed = True
        db_table = 'tambahan_biaya'
        unique_together = (('no_rawat', 'nama_biaya'),)


class Tambahanpotongan(models.Model):
    indexins = models.CharField(max_length=4)
    potongan = models.FloatField()

    class Meta:
        managed = True
        db_table = 'tambahanpotongan'


class Tambahjaga(models.Model):
    tgl = models.DateField(primary_key=True)
    id = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='id')
    jml = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tambahjaga'
        unique_together = (('tgl', 'id'),)


class Tampbeli1(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    nama_brng = models.CharField(max_length=100, blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    satuan_stok = models.CharField(max_length=10, blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    jumlah_stok = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tampbeli1'


class Tampjual1(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    nama_brng = models.CharField(max_length=100, blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField()
    jumlah = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField(blank=True, null=True)
    bsr_dis = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tampjual1'


class Tampjurnal(models.Model):
    kd_rek = models.CharField(primary_key=True, max_length=15)
    nm_rek = models.CharField(max_length=100, blank=True, null=True)
    debet = models.FloatField(blank=True, null=True)
    kredit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tampjurnal'


class Tamppiutang(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    nama_brng = models.CharField(max_length=50, blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField(blank=True, null=True)
    bsr_dis = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    petugas = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)
    aturan_pakai = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'tamppiutang'
        unique_together = (('kode_brng', 'no_batch', 'no_faktur'),)


class Tampreturbeli(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=20)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    nama_brng = models.CharField(max_length=100, blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jml_beli = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    jml_retur2 = models.FloatField(blank=True, null=True)
    kadaluarsa = models.CharField(max_length=14)
    petugas = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'tampreturbeli'
        unique_together = (('no_faktur', 'kode_brng'),)


class Tampreturjual(models.Model):
    nota_jual = models.CharField(primary_key=True, max_length=20)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    nama_brng = models.CharField(max_length=100, blank=True, null=True)
    jml_jual = models.FloatField(blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    petugas = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'tampreturjual'
        unique_together = (('nota_jual', 'kode_brng', 'no_batch', 'no_faktur'),)


class Tampreturpiutang(models.Model):
    nota_piutang = models.CharField(primary_key=True, max_length=20)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    nama_brng = models.CharField(max_length=100, blank=True, null=True)
    jml_piutang = models.FloatField(blank=True, null=True)
    h_piutang = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    petugas = models.CharField(max_length=20, blank=True, null=True)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'tampreturpiutang'
        unique_together = (('nota_piutang', 'kode_brng', 'no_batch'),)


class TemplateLaboratorium(models.Model):
    kd_jenis_prw = models.ForeignKey(JnsPerawatanLab, on_delete = models.CASCADE, db_column='kd_jenis_prw')
    id_template = models.AutoField(primary_key=True)
    pemeriksaan = models.CharField(db_column='Pemeriksaan', max_length=200)  # Field name made lowercase.
    satuan = models.CharField(max_length=20)
    nilai_rujukan_ld = models.CharField(max_length=30)
    nilai_rujukan_la = models.CharField(max_length=30)
    nilai_rujukan_pd = models.CharField(max_length=30)
    nilai_rujukan_pa = models.CharField(max_length=30)
    bagian_rs = models.FloatField()
    bhp = models.FloatField()
    bagian_perujuk = models.FloatField()
    bagian_dokter = models.FloatField()
    bagian_laborat = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_item = models.FloatField()
    urut = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'template_laboratorium'


class TemplateUtd(models.Model):
    kd_jenis_prw = models.ForeignKey(JnsPerawatanUtd, on_delete = models.CASCADE, db_column='kd_jenis_prw', blank=True, null=True)
    id_template = models.AutoField(primary_key=True)
    pemeriksaan = models.CharField(max_length=200, blank=True, null=True)
    nilai_rujukan = models.CharField(max_length=30)
    bagian_rs = models.FloatField(blank=True, null=True)
    bhp = models.FloatField(blank=True, null=True)
    bagian_perujuk = models.FloatField(blank=True, null=True)
    bagian_dokter = models.FloatField(blank=True, null=True)
    petugas_utd = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_item = models.FloatField(blank=True, null=True)
    urut = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'template_utd'


class Temporary(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary'


class Temporary2(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=100)
    temp2 = models.CharField(max_length=100)
    temp3 = models.CharField(max_length=100)
    temp4 = models.CharField(max_length=100)
    temp5 = models.CharField(max_length=100)
    temp6 = models.CharField(max_length=100)
    temp7 = models.CharField(max_length=100)
    temp8 = models.CharField(max_length=100)
    temp9 = models.CharField(max_length=100)
    temp10 = models.CharField(max_length=100)
    temp11 = models.CharField(max_length=100)
    temp12 = models.CharField(max_length=100)
    temp13 = models.CharField(max_length=100)
    temp14 = models.CharField(max_length=100)
    temp15 = models.CharField(max_length=100)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)
    temp38 = models.CharField(max_length=100)
    temp39 = models.CharField(max_length=100)
    temp40 = models.CharField(max_length=100)
    temp41 = models.CharField(max_length=100)
    temp42 = models.CharField(max_length=100)
    temp43 = models.CharField(max_length=100)
    temp44 = models.CharField(max_length=100)
    temp45 = models.CharField(max_length=100)
    temp46 = models.CharField(max_length=100)
    temp47 = models.CharField(max_length=100)
    temp48 = models.CharField(max_length=100)
    temp49 = models.CharField(max_length=100)
    temp50 = models.CharField(max_length=100)
    temp51 = models.CharField(max_length=100)
    temp52 = models.CharField(max_length=100)
    temp53 = models.CharField(max_length=100)
    temp54 = models.CharField(max_length=100)
    temp55 = models.CharField(max_length=100)
    temp56 = models.CharField(max_length=100)
    temp57 = models.CharField(max_length=100)
    temp58 = models.CharField(max_length=100)
    temp59 = models.CharField(max_length=100)
    temp60 = models.CharField(max_length=100)
    temp61 = models.CharField(max_length=100)
    temp62 = models.CharField(max_length=100)
    temp63 = models.CharField(max_length=100)
    temp64 = models.CharField(max_length=100)
    temp65 = models.CharField(max_length=100)
    temp66 = models.CharField(max_length=100)
    temp67 = models.CharField(max_length=100)
    temp68 = models.CharField(max_length=100)
    temp69 = models.CharField(max_length=100)
    temp70 = models.CharField(max_length=100)
    temp71 = models.CharField(max_length=100)
    temp72 = models.CharField(max_length=100)
    temp73 = models.CharField(max_length=100)
    temp74 = models.CharField(max_length=100)
    temp75 = models.CharField(max_length=100)
    temp76 = models.CharField(max_length=100)
    temp77 = models.CharField(max_length=100)
    temp78 = models.CharField(max_length=100)
    temp79 = models.CharField(max_length=100)
    temp80 = models.CharField(max_length=100)
    temp81 = models.CharField(max_length=100)
    temp82 = models.CharField(max_length=100)
    temp83 = models.CharField(max_length=100)
    temp84 = models.CharField(max_length=100)
    temp85 = models.CharField(max_length=100)
    temp86 = models.CharField(max_length=100)
    temp87 = models.CharField(max_length=100)
    temp88 = models.CharField(max_length=100)
    temp89 = models.CharField(max_length=100)
    temp90 = models.CharField(max_length=100)
    temp91 = models.CharField(max_length=100)
    temp92 = models.CharField(max_length=100)
    temp93 = models.CharField(max_length=100)
    temp94 = models.CharField(max_length=100)
    temp95 = models.CharField(max_length=100)
    temp96 = models.CharField(max_length=100)
    temp97 = models.CharField(max_length=100)
    temp98 = models.CharField(max_length=100)
    temp99 = models.CharField(max_length=100)
    temp100 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary2'


class TemporaryBayarRalan(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=100)
    temp2 = models.CharField(max_length=200)
    temp3 = models.CharField(max_length=100)
    temp4 = models.CharField(max_length=100)
    temp5 = models.CharField(max_length=100)
    temp6 = models.CharField(max_length=100)
    temp7 = models.CharField(max_length=100)
    temp8 = models.CharField(max_length=100)
    temp9 = models.CharField(max_length=100)
    temp10 = models.CharField(max_length=100)
    temp11 = models.CharField(max_length=100)
    temp12 = models.CharField(max_length=100)
    temp13 = models.CharField(max_length=100)
    temp14 = models.CharField(max_length=100)
    temp15 = models.CharField(max_length=100)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_bayar_ralan'


class TemporaryBayarRanap(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=100)
    temp2 = models.CharField(max_length=200)
    temp3 = models.CharField(max_length=100)
    temp4 = models.CharField(max_length=100)
    temp5 = models.CharField(max_length=100)
    temp6 = models.CharField(max_length=100)
    temp7 = models.CharField(max_length=100)
    temp8 = models.CharField(max_length=100)
    temp9 = models.CharField(max_length=100)
    temp10 = models.CharField(max_length=100)
    temp11 = models.CharField(max_length=100)
    temp12 = models.CharField(max_length=100)
    temp13 = models.CharField(max_length=100)
    temp14 = models.CharField(max_length=100)
    temp15 = models.CharField(max_length=100)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_bayar_ranap'


class TemporaryBookingRegistrasi(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_booking_registrasi'


class TemporaryGizi(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_gizi'


class TemporaryGrafik(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_grafik'


class TemporaryLab(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_lab'


class TemporaryLamaPelayananRadiologi(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_lama_pelayanan_radiologi'


class TemporaryPayment(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_payment'


class TemporaryPermintaanLab(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_permintaan_lab'


class TemporaryPermintaanRadiologi(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_permintaan_radiologi'


class TemporaryPresensi(models.Model):
    id = models.OneToOneField(Pegawai, on_delete = models.CASCADE, db_column='id', primary_key=True)
    shift = models.CharField(max_length=13)
    jam_datang = models.DateTimeField(blank=True, null=True)
    jam_pulang = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=25)
    keterlambatan = models.CharField(max_length=20)
    durasi = models.CharField(max_length=20, blank=True, null=True)
    photo = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'temporary_presensi'


class TemporaryRadiologi(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_radiologi'


class TemporaryResep(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_resep'


class TemporaryResume(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_resume'


class TemporarySensusHarian(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'temporary_sensus_harian'


class TemporarySurveilensPenyakit(models.Model):
    kd_penyakit = models.ForeignKey(Penyakit, on_delete = models.CASCADE, db_column='kd_penyakit')
    kd_penyakit2 = models.ForeignKey(Penyakit, on_delete = models.CASCADE, db_column='kd_penyakit2')

    class Meta:
        managed = True
        db_table = 'temporary_surveilens_penyakit'


class TemporaryTambahanPotongan(models.Model):
    no_rawat = models.CharField(primary_key=True, max_length=17)
    nama_tambahan = models.CharField(max_length=100)
    biaya = models.FloatField()
    status = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'temporary_tambahan_potongan'
        unique_together = (('no_rawat', 'nama_tambahan', 'status'),)


class Temppanggilnorawat(models.Model):
    no_rawat = models.CharField(max_length=17)

    class Meta:
        managed = True
        db_table = 'temppanggilnorawat'


class Temppanggilrm(models.Model):
    no_rkm_medis = models.CharField(primary_key=True, max_length=15)

    class Meta:
        managed = True
        db_table = 'temppanggilrm'


class Tindakan(models.Model):
    tgl = models.DateTimeField(primary_key=True)
    id = models.ForeignKey(Pegawai, on_delete = models.CASCADE, db_column='id')
    tnd = models.IntegerField()
    jm = models.FloatField()
    nm_pasien = models.CharField(max_length=30)
    kamar = models.CharField(max_length=20)
    diagnosa = models.CharField(max_length=50)
    jmlh = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tindakan'
        unique_together = (('tgl', 'id', 'tnd', 'nm_pasien'),)


class Tracker(models.Model):
    nip = models.CharField(primary_key=True, max_length=20)
    tgl_login = models.DateField()
    jam_login = models.TimeField()

    class Meta:
        managed = True
        db_table = 'tracker'
        unique_together = (('nip', 'tgl_login', 'jam_login'),)


class Trackersql(models.Model):
    tanggal = models.DateTimeField()
    sqle = models.TextField()
    usere = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'trackersql'


class UbahPenjab(models.Model):
    no_rawat = models.ForeignKey(RegPeriksa, on_delete = models.CASCADE, db_column='no_rawat')
    tgl_ubah = models.DateTimeField()
    kd_pj1 = models.ForeignKey(Penjab, on_delete = models.CASCADE, db_column='kd_pj1')
    kd_pj2 = models.ForeignKey(Penjab, on_delete = models.CASCADE, db_column='kd_pj2')

    class Meta:
        managed = True
        db_table = 'ubah_penjab'


class User(models.Model):
    id_user = models.CharField(primary_key=True, max_length=700)
    password = models.TextField()
    penyakit = models.CharField(max_length=5)
    obat_penyakit = models.CharField(max_length=5)
    dokter = models.CharField(max_length=5)
    jadwal_praktek = models.CharField(max_length=5)
    petugas = models.CharField(max_length=5)
    pasien = models.CharField(max_length=5)
    registrasi = models.CharField(max_length=5)
    tindakan_ralan = models.CharField(max_length=5)
    kamar_inap = models.CharField(max_length=5)
    tindakan_ranap = models.CharField(max_length=5)
    operasi = models.CharField(max_length=5)
    rujukan_keluar = models.CharField(max_length=5)
    rujukan_masuk = models.CharField(max_length=5)
    beri_obat = models.CharField(max_length=5)
    resep_pulang = models.CharField(max_length=5)
    pasien_meninggal = models.CharField(max_length=5)
    diet_pasien = models.CharField(max_length=5)
    kelahiran_bayi = models.CharField(max_length=5)
    periksa_lab = models.CharField(max_length=5)
    periksa_radiologi = models.CharField(max_length=5)
    kasir_ralan = models.CharField(max_length=5)
    deposit_pasien = models.CharField(max_length=5)
    piutang_pasien = models.CharField(max_length=5)
    peminjaman_berkas = models.CharField(max_length=5)
    barcode = models.CharField(max_length=5)
    presensi_harian = models.CharField(max_length=5)
    presensi_bulanan = models.CharField(max_length=5)
    pegawai_admin = models.CharField(max_length=5)
    pegawai_user = models.CharField(max_length=5)
    suplier = models.CharField(max_length=5)
    satuan_barang = models.CharField(max_length=5)
    konversi_satuan = models.CharField(max_length=5)
    jenis_barang = models.CharField(max_length=5)
    obat = models.CharField(max_length=5)
    stok_opname_obat = models.CharField(max_length=5)
    stok_obat_pasien = models.CharField(max_length=5)
    pengadaan_obat = models.CharField(max_length=5)
    pemesanan_obat = models.CharField(max_length=5)
    penjualan_obat = models.CharField(max_length=5)
    piutang_obat = models.CharField(max_length=5)
    retur_ke_suplier = models.CharField(max_length=5)
    retur_dari_pembeli = models.CharField(max_length=5)
    retur_obat_ranap = models.CharField(max_length=5)
    retur_piutang_pasien = models.CharField(max_length=5)
    keuntungan_penjualan = models.CharField(max_length=5)
    keuntungan_beri_obat = models.CharField(max_length=5)
    sirkulasi_obat = models.CharField(max_length=5)
    ipsrs_barang = models.CharField(max_length=5)
    ipsrs_pengadaan_barang = models.CharField(max_length=5)
    ipsrs_stok_keluar = models.CharField(max_length=5)
    ipsrs_rekap_pengadaan = models.CharField(max_length=5)
    ipsrs_rekap_stok_keluar = models.CharField(max_length=5)
    ipsrs_pengeluaran_harian = models.CharField(max_length=5)
    inventaris_jenis = models.CharField(max_length=5)
    inventaris_kategori = models.CharField(max_length=5)
    inventaris_merk = models.CharField(max_length=5)
    inventaris_ruang = models.CharField(max_length=5)
    inventaris_produsen = models.CharField(max_length=5)
    inventaris_koleksi = models.CharField(max_length=5)
    inventaris_inventaris = models.CharField(max_length=5)
    inventaris_sirkulasi = models.CharField(max_length=5)
    parkir_jenis = models.CharField(max_length=5)
    parkir_in = models.CharField(max_length=5)
    parkir_out = models.CharField(max_length=5)
    parkir_rekap_harian = models.CharField(max_length=5)
    parkir_rekap_bulanan = models.CharField(max_length=5)
    informasi_kamar = models.CharField(max_length=5)
    harian_tindakan_poli = models.CharField(max_length=5)
    obat_per_poli = models.CharField(max_length=5)
    obat_per_kamar = models.CharField(max_length=5)
    obat_per_dokter_ralan = models.CharField(max_length=5)
    obat_per_dokter_ranap = models.CharField(max_length=5)
    harian_dokter = models.CharField(max_length=5)
    bulanan_dokter = models.CharField(max_length=5)
    harian_paramedis = models.CharField(max_length=5)
    bulanan_paramedis = models.CharField(max_length=5)
    pembayaran_ralan = models.CharField(max_length=5)
    pembayaran_ranap = models.CharField(max_length=5)
    rekap_pembayaran_ralan = models.CharField(max_length=5)
    rekap_pembayaran_ranap = models.CharField(max_length=5)
    tagihan_masuk = models.CharField(max_length=5)
    tambahan_biaya = models.CharField(max_length=5)
    potongan_biaya = models.CharField(max_length=5)
    resep_obat = models.CharField(max_length=5)
    resume_pasien = models.CharField(max_length=5)
    penyakit_ralan = models.CharField(max_length=5)
    penyakit_ranap = models.CharField(max_length=5)
    kamar = models.CharField(max_length=5)
    tarif_ralan = models.CharField(max_length=5)
    tarif_ranap = models.CharField(max_length=5)
    tarif_lab = models.CharField(max_length=5)
    tarif_radiologi = models.CharField(max_length=5)
    tarif_operasi = models.CharField(max_length=5)
    akun_rekening = models.CharField(max_length=5)
    rekening_tahun = models.CharField(max_length=5)
    posting_jurnal = models.CharField(max_length=5)
    buku_besar = models.CharField(max_length=5)
    cashflow = models.CharField(max_length=5)
    keuangan = models.CharField(max_length=5)
    pengeluaran = models.CharField(max_length=5)
    setup_pjlab = models.CharField(max_length=5)
    setup_otolokasi = models.CharField(max_length=5)
    setup_jam_kamin = models.CharField(max_length=5)
    setup_embalase = models.CharField(max_length=5)
    tracer_login = models.CharField(max_length=5)
    display = models.CharField(max_length=5)
    set_harga_obat = models.CharField(max_length=5)
    set_penggunaan_tarif = models.CharField(max_length=5)
    set_oto_ralan = models.CharField(max_length=5)
    biaya_harian = models.CharField(max_length=5)
    biaya_masuk_sekali = models.CharField(max_length=5)
    set_no_rm = models.CharField(max_length=5)
    billing_ralan = models.CharField(max_length=5)
    billing_ranap = models.CharField(max_length=5)
    jm_ranap_dokter = models.CharField(max_length=5)
    igd = models.CharField(max_length=5)
    barcoderalan = models.CharField(max_length=5)
    barcoderanap = models.CharField(max_length=5)
    set_harga_obat_ralan = models.CharField(max_length=5)
    set_harga_obat_ranap = models.CharField(max_length=5)
    penyakit_pd3i = models.CharField(max_length=5)
    surveilans_pd3i = models.CharField(max_length=5)
    surveilans_ralan = models.CharField(max_length=5)
    diagnosa_pasien = models.CharField(max_length=5)
    surveilans_ranap = models.CharField(max_length=5)
    pny_takmenular_ranap = models.CharField(max_length=5)
    pny_takmenular_ralan = models.CharField(max_length=5)
    kunjungan_ralan = models.CharField(max_length=5)
    rl32 = models.CharField(max_length=5)
    rl33 = models.CharField(max_length=5)
    rl37 = models.CharField(max_length=5)
    rl38 = models.CharField(max_length=5)
    harian_tindakan_dokter = models.CharField(max_length=5)
    sms = models.CharField(max_length=5)
    sidikjari = models.CharField(max_length=5)
    jam_masuk = models.CharField(max_length=5)
    jadwal_pegawai = models.CharField(max_length=5)
    parkir_barcode = models.CharField(max_length=5)
    set_nota = models.CharField(max_length=5)
    dpjp_ranap = models.CharField(max_length=5)
    mutasi_barang = models.CharField(max_length=5)
    rl34 = models.CharField(max_length=5, blank=True, null=True)
    rl36 = models.CharField(max_length=5)
    fee_visit_dokter = models.CharField(max_length=5, blank=True, null=True)
    fee_bacaan_ekg = models.CharField(max_length=5, blank=True, null=True)
    fee_rujukan_rontgen = models.CharField(max_length=5, blank=True, null=True)
    fee_rujukan_ranap = models.CharField(max_length=5, blank=True, null=True)
    fee_ralan = models.CharField(max_length=5, blank=True, null=True)
    akun_bayar = models.CharField(max_length=5, blank=True, null=True)
    bayar_pemesanan_obat = models.CharField(max_length=5, blank=True, null=True)
    obat_per_dokter_peresep = models.CharField(max_length=5, blank=True, null=True)
    ipsrs_jenis_barang = models.CharField(max_length=5, blank=True, null=True)
    pemasukan_lain = models.CharField(max_length=5, blank=True, null=True)
    pengaturan_rekening = models.CharField(max_length=5, blank=True, null=True)
    closing_kasir = models.CharField(max_length=5, blank=True, null=True)
    keterlambatan_presensi = models.CharField(max_length=5, blank=True, null=True)
    set_harga_kamar = models.CharField(max_length=5, blank=True, null=True)
    rekap_per_shift = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_nik = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_kartu = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_riwayat = models.CharField(max_length=5, blank=True, null=True)
    obat_per_cara_bayar = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_ranap = models.CharField(max_length=5, blank=True, null=True)
    bayar_piutang = models.CharField(max_length=5, blank=True, null=True)
    payment_point = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_nomor_rujukan = models.CharField(max_length=5, blank=True, null=True)
    icd9 = models.CharField(max_length=5, blank=True, null=True)
    darurat_stok = models.CharField(max_length=5, blank=True, null=True)
    retensi_rm = models.CharField(max_length=5, blank=True, null=True)
    temporary_presensi = models.CharField(max_length=5, blank=True, null=True)
    jurnal_harian = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_obat2 = models.CharField(max_length=5, blank=True, null=True)
    edit_registrasi = models.CharField(max_length=5, blank=True, null=True)
    bpjs_referensi_diagnosa = models.CharField(max_length=5, blank=True, null=True)
    bpjs_referensi_poli = models.CharField(max_length=5, blank=True, null=True)
    industrifarmasi = models.CharField(max_length=5, blank=True, null=True)
    harian_js = models.CharField(max_length=5, blank=True, null=True)
    bulanan_js = models.CharField(max_length=5, blank=True, null=True)
    harian_paket_bhp = models.CharField(max_length=5, blank=True, null=True)
    bulanan_paket_bhp = models.CharField(max_length=5, blank=True, null=True)
    piutang_pasien2 = models.CharField(max_length=5, blank=True, null=True)
    bpjs_referensi_faskes = models.CharField(max_length=5, blank=True, null=True)
    bpjs_sep = models.CharField(max_length=5, blank=True, null=True)
    pengambilan_utd = models.CharField(max_length=5, blank=True, null=True)
    tarif_utd = models.CharField(max_length=5, blank=True, null=True)
    pengambilan_utd2 = models.CharField(max_length=5, blank=True, null=True)
    utd_medis_rusak = models.CharField(max_length=5, blank=True, null=True)
    pengambilan_penunjang_utd = models.CharField(max_length=5, blank=True, null=True)
    pengambilan_penunjang_utd2 = models.CharField(max_length=5, blank=True, null=True)
    utd_penunjang_rusak = models.CharField(max_length=5, blank=True, null=True)
    suplier_penunjang = models.CharField(max_length=5, blank=True, null=True)
    utd_donor = models.CharField(max_length=5, blank=True, null=True)
    bpjs_monitoring_klaim = models.CharField(max_length=5, blank=True, null=True)
    utd_cekal_darah = models.CharField(max_length=5, blank=True, null=True)
    utd_komponen_darah = models.CharField(max_length=5, blank=True, null=True)
    utd_stok_darah = models.CharField(max_length=5, blank=True, null=True)
    utd_pemisahan_darah = models.CharField(max_length=5, blank=True, null=True)
    harian_kamar = models.CharField(max_length=5, blank=True, null=True)
    rincian_piutang_pasien = models.CharField(max_length=5, blank=True, null=True)
    keuntungan_beri_obat_nonpiutang = models.CharField(max_length=5, blank=True, null=True)
    reklasifikasi_ralan = models.CharField(max_length=5, blank=True, null=True)
    reklasifikasi_ranap = models.CharField(max_length=5, blank=True, null=True)
    utd_penyerahan_darah = models.CharField(max_length=5, blank=True, null=True)
    hutang_obat = models.CharField(max_length=5, blank=True, null=True)
    riwayat_obat_alkes_bhp = models.CharField(max_length=5, blank=True, null=True)
    sensus_harian_poli = models.CharField(max_length=5, blank=True, null=True)
    rl4a = models.CharField(max_length=5, blank=True, null=True)
    aplicare_referensi_kamar = models.CharField(max_length=5, blank=True, null=True)
    aplicare_ketersediaan_kamar = models.CharField(max_length=5, blank=True, null=True)
    inacbg_klaim_baru_otomatis = models.CharField(max_length=5, blank=True, null=True)
    inacbg_klaim_baru_manual = models.CharField(max_length=5, blank=True, null=True)
    inacbg_coder_nik = models.CharField(max_length=5, blank=True, null=True)
    mutasi_berkas = models.CharField(max_length=5, blank=True, null=True)
    akun_piutang = models.CharField(max_length=5, blank=True, null=True)
    harian_kso = models.CharField(max_length=5, blank=True, null=True)
    bulanan_kso = models.CharField(max_length=5, blank=True, null=True)
    harian_menejemen = models.CharField(max_length=5, blank=True, null=True)
    bulanan_menejemen = models.CharField(max_length=5, blank=True, null=True)
    inhealth_cek_eligibilitas = models.CharField(max_length=5, blank=True, null=True)
    inhealth_referensi_jenpel_ruang_rawat = models.CharField(max_length=5, blank=True, null=True)
    inhealth_referensi_poli = models.CharField(max_length=5, blank=True, null=True)
    inhealth_referensi_faskes = models.CharField(max_length=5, blank=True, null=True)
    inhealth_sjp = models.CharField(max_length=5, blank=True, null=True)
    piutang_ralan = models.CharField(max_length=5, blank=True, null=True)
    piutang_ranap = models.CharField(max_length=5, blank=True, null=True)
    detail_piutang_penjab = models.CharField(max_length=5, blank=True, null=True)
    lama_pelayanan_ralan = models.CharField(max_length=5, blank=True, null=True)
    catatan_pasien = models.CharField(max_length=5, blank=True, null=True)
    rl4b = models.CharField(max_length=5, blank=True, null=True)
    rl4asebab = models.CharField(max_length=5, blank=True, null=True)
    rl4bsebab = models.CharField(max_length=5, blank=True, null=True)
    data_hais = models.CharField(db_column='data_HAIs', max_length=5, blank=True, null=True)  # Field name made lowercase.
    harian_hais = models.CharField(db_column='harian_HAIs', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bulanan_hais = models.CharField(db_column='bulanan_HAIs', max_length=5, blank=True, null=True)  # Field name made lowercase.
    hitung_bor = models.CharField(max_length=5, blank=True, null=True)
    perusahaan_pasien = models.CharField(max_length=5, blank=True, null=True)
    resep_dokter = models.CharField(max_length=5, blank=True, null=True)
    lama_pelayanan_apotek = models.CharField(max_length=5, blank=True, null=True)
    hitung_alos = models.CharField(max_length=5, blank=True, null=True)
    detail_tindakan = models.CharField(max_length=5, blank=True, null=True)
    rujukan_poli_internal = models.CharField(max_length=5, blank=True, null=True)
    rekap_poli_anak = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_poli = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_perdokter = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_perpekerjaan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_perpendidikan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_pertahun = models.CharField(max_length=5, blank=True, null=True)
    berkas_digital_perawatan = models.CharField(max_length=5, blank=True, null=True)
    penyakit_menular_ranap = models.CharField(max_length=5, blank=True, null=True)
    penyakit_menular_ralan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_perbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_demografi = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftartahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftartahun2 = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftarbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftarbulan2 = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftartanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftartanggal2 = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusbataltahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusbatalbulan = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_penyakit = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusbataltanggal = models.CharField(max_length=5, blank=True, null=True)
    kategori_barang = models.CharField(max_length=5, blank=True, null=True)
    golongan_barang = models.CharField(max_length=5, blank=True, null=True)
    pemberian_obat_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    penjualan_obat_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_kesadaran = models.CharField(max_length=5, blank=True, null=True)
    pembatalan_periksa_dokter = models.CharField(max_length=5, blank=True, null=True)
    pembayaran_per_unit = models.CharField(max_length=5, blank=True, null=True)
    rekap_pembayaran_per_unit = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_percarabayar = models.CharField(max_length=5, blank=True, null=True)
    ipsrs_pengadaan_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    ipsrs_stokkeluar_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_ranaptahun = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_rujukan = models.CharField(max_length=5, blank=True, null=True)
    grafik_lab_ralantahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_rad_ralantahun = models.CharField(max_length=5, blank=True, null=True)
    cek_entry_ralan = models.CharField(max_length=5, blank=True, null=True)
    inacbg_klaim_baru_manual2 = models.CharField(max_length=5, blank=True, null=True)
    permintaan_medis = models.CharField(max_length=5, blank=True, null=True)
    rekap_permintaan_medis = models.CharField(max_length=5, blank=True, null=True)
    surat_pemesanan_medis = models.CharField(max_length=5, blank=True, null=True)
    permintaan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    rekap_permintaan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    surat_pemesanan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    grafik_per_perujuk = models.CharField(max_length=5)
    bpjs_cek_prosedur = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_kelas_rawat = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_dokter = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_spesialistik = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_ruangrawat = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_carakeluar = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_pasca_pulang = models.CharField(max_length=5, blank=True, null=True)
    detail_tindakan_okvk = models.CharField(max_length=5, blank=True, null=True)
    billing_parsial = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_nomor_rujukan_rs = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_rujukan_kartu_pcare = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_rujukan_kartu_rs = models.CharField(max_length=5, blank=True, null=True)
    akses_depo_obat = models.CharField(max_length=5, blank=True, null=True)
    bpjs_rujukan_keluar = models.CharField(max_length=5, blank=True, null=True)
    grafik_lab_ralanbulan = models.CharField(max_length=5, blank=True, null=True)
    pengeluaran_stok_apotek = models.CharField(max_length=5, blank=True, null=True)
    grafik_rad_ralanbulan = models.CharField(max_length=5, blank=True, null=True)
    detailjmdokter2 = models.CharField(max_length=5, blank=True, null=True)
    pengaduan_pasien = models.CharField(max_length=5, blank=True, null=True)
    grafik_lab_ralanhari = models.CharField(max_length=5, blank=True, null=True)
    grafik_rad_ralanhari = models.CharField(max_length=5, blank=True, null=True)
    sensus_harian_ralan = models.CharField(max_length=5, blank=True, null=True)
    metode_racik = models.CharField(max_length=5, blank=True, null=True)
    pembayaran_akun_bayar = models.CharField(max_length=5, blank=True, null=True)
    pengguna_obat_resep = models.CharField(max_length=5, blank=True, null=True)
    rekap_pemesanan = models.CharField(max_length=5, blank=True, null=True)
    master_berkas_pegawai = models.CharField(max_length=5, blank=True, null=True)
    berkas_kepegawaian = models.CharField(max_length=5, blank=True, null=True)
    riwayat_jabatan = models.CharField(max_length=5, blank=True, null=True)
    riwayat_pendidikan = models.CharField(max_length=5, blank=True, null=True)
    riwayat_naik_gaji = models.CharField(max_length=5, blank=True, null=True)
    kegiatan_ilmiah = models.CharField(max_length=5, blank=True, null=True)
    riwayat_penghargaan = models.CharField(max_length=5, blank=True, null=True)
    riwayat_penelitian = models.CharField(max_length=5, blank=True, null=True)
    penerimaan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    bayar_pesan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    hutang_barang_non_medis = models.CharField(max_length=5, blank=True, null=True)
    rekap_pemesanan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    insiden_keselamatan = models.CharField(max_length=5, blank=True, null=True)
    insiden_keselamatan_pasien = models.CharField(max_length=5, blank=True, null=True)
    grafik_ikp_pertahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_ikp_perbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_ikp_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    riwayat_data_batch = models.CharField(max_length=5, blank=True, null=True)
    grafik_ikp_jenis = models.CharField(max_length=5, blank=True, null=True)
    grafik_ikp_dampak = models.CharField(max_length=5, blank=True, null=True)
    piutang_akun_piutang = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_per_agama = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_per_umur = models.CharField(max_length=5, blank=True, null=True)
    suku_bangsa = models.CharField(max_length=5, blank=True, null=True)
    bahasa_pasien = models.CharField(max_length=5, blank=True, null=True)
    golongan_tni = models.CharField(max_length=5, blank=True, null=True)
    satuan_tni = models.CharField(max_length=5, blank=True, null=True)
    jabatan_tni = models.CharField(max_length=5, blank=True, null=True)
    pangkat_tni = models.CharField(max_length=5, blank=True, null=True)
    golongan_polri = models.CharField(max_length=5, blank=True, null=True)
    satuan_polri = models.CharField(max_length=5, blank=True, null=True)
    jabatan_polri = models.CharField(max_length=5, blank=True, null=True)
    pangkat_polri = models.CharField(max_length=5, blank=True, null=True)
    cacat_fisik = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_suku = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_bahasa = models.CharField(max_length=5, blank=True, null=True)
    booking_operasi = models.CharField(max_length=5, blank=True, null=True)
    mapping_poli_bpjs = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_per_cacat = models.CharField(max_length=5, blank=True, null=True)
    barang_cssd = models.CharField(max_length=5, blank=True, null=True)
    skdp_bpjs = models.CharField(max_length=5, blank=True, null=True)
    booking_registrasi = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_propinsi = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_kabupaten = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_kecamatan = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_dokterdpjp = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_riwayat_rujukanrs = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_tanggal_rujukan = models.CharField(max_length=5, blank=True, null=True)
    permintaan_lab = models.CharField(max_length=5, blank=True, null=True)
    permintaan_radiologi = models.CharField(max_length=5, blank=True, null=True)
    surat_indeks = models.CharField(max_length=5, blank=True, null=True)
    surat_map = models.CharField(max_length=5, blank=True, null=True)
    surat_almari = models.CharField(max_length=5, blank=True, null=True)
    surat_rak = models.CharField(max_length=5, blank=True, null=True)
    surat_ruang = models.CharField(max_length=5, blank=True, null=True)
    surat_klasifikasi = models.CharField(max_length=5, blank=True, null=True)
    surat_status = models.CharField(max_length=5, blank=True, null=True)
    surat_sifat = models.CharField(max_length=5, blank=True, null=True)
    surat_balas = models.CharField(max_length=5)
    surat_masuk = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_dokter = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_poli = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_provider = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_statuspulang = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_spesialis = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_subspesialis = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_sarana = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_khusus = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_obat = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_tindakan = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_faskessubspesialis = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_faskesalihrawat = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_faskesthalasemia = models.CharField(max_length=5, blank=True, null=True)
    pcare_mapping_obat = models.CharField(max_length=5, blank=True, null=True)
    pcare_mapping_tindakan = models.CharField(max_length=5, blank=True, null=True)
    pcare_club_prolanis = models.CharField(max_length=5, blank=True, null=True)
    pcare_mapping_poli = models.CharField(max_length=5, blank=True, null=True)
    pcare_kegiatan_kelompok = models.CharField(max_length=5, blank=True, null=True)
    pcare_mapping_tindakan_ranap = models.CharField(max_length=5, blank=True, null=True)
    pcare_peserta_kegiatan_kelompok = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_obat3 = models.CharField(max_length=5, blank=True, null=True)
    bridging_pcare_daftar = models.CharField(max_length=5, blank=True, null=True)
    pcare_mapping_dokter = models.CharField(max_length=5, blank=True, null=True)
    ranap_per_ruang = models.CharField(max_length=5, blank=True, null=True)
    penyakit_ranap_cara_bayar = models.CharField(max_length=5, blank=True, null=True)
    anggota_militer_dirawat = models.CharField(max_length=5, blank=True, null=True)
    set_input_parsial = models.CharField(max_length=5, blank=True, null=True)
    lama_pelayanan_radiologi = models.CharField(max_length=5, blank=True, null=True)
    lama_pelayanan_lab = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_sep = models.CharField(max_length=5, blank=True, null=True)
    catatan_perawatan = models.CharField(max_length=5, blank=True, null=True)
    surat_keluar = models.CharField(max_length=5, blank=True, null=True)
    kegiatan_farmasi = models.CharField(max_length=5, blank=True, null=True)
    stok_opname_logistik = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_non_medis = models.CharField(max_length=5, blank=True, null=True)
    rekap_lab_pertahun = models.CharField(max_length=5, blank=True, null=True)
    perujuk_lab_pertahun = models.CharField(max_length=5, blank=True, null=True)
    rekap_radiologi_pertahun = models.CharField(max_length=5, blank=True, null=True)
    perujuk_radiologi_pertahun = models.CharField(max_length=5, blank=True, null=True)
    jumlah_porsi_diet = models.CharField(max_length=5, blank=True, null=True)
    jumlah_macam_diet = models.CharField(max_length=5, blank=True, null=True)
    payment_point2 = models.CharField(max_length=5, blank=True, null=True)
    pembayaran_akun_bayar2 = models.CharField(max_length=5, blank=True, null=True)
    hapus_nota_salah = models.CharField(max_length=5, blank=True, null=True)
    pengkajian_askep = models.CharField(max_length=5, blank=True, null=True)
    hais_perbangsal = models.CharField(max_length=5, blank=True, null=True)
    ppn_obat = models.CharField(max_length=5, blank=True, null=True)
    saldo_akun_perbulan = models.CharField(max_length=5, blank=True, null=True)
    display_apotek = models.CharField(max_length=5, blank=True, null=True)
    sisrute_referensi_faskes = models.CharField(max_length=5, blank=True, null=True)
    sisrute_referensi_alasanrujuk = models.CharField(max_length=5, blank=True, null=True)
    sisrute_referensi_diagnosa = models.CharField(max_length=5, blank=True, null=True)
    sisrute_rujukan_masuk = models.CharField(max_length=5, blank=True, null=True)
    sisrute_rujukan_keluar = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_skdp = models.CharField(max_length=5, blank=True, null=True)
    data_batch = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_permintaan_lab = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_permintaan_lab2 = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_permintaan_radiologi = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_permintaan_radiologi2 = models.CharField(max_length=5, blank=True, null=True)
    pcare_pemberian_obat = models.CharField(max_length=5, blank=True, null=True)
    pcare_pemberian_tindakan = models.CharField(max_length=5)
    pembayaran_akun_bayar3 = models.CharField(max_length=5, blank=True, null=True)
    password_asuransi = models.CharField(max_length=5, blank=True, null=True)
    kemenkes_sitt = models.CharField(max_length=5)
    siranap_ketersediaan_kamar = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_periodelaporan = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_rujukan = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_riwayat = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_tipediagnosis = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_statushiv = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_skoringanak = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_konfirmasiskoring5 = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_konfirmasiskoring6 = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_sumberobat = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_hasilakhirpengobatan = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_hasilteshiv = models.CharField(max_length=5)
    kadaluarsa_batch = models.CharField(max_length=5)
    sisa_stok = models.CharField(max_length=5, blank=True, null=True)
    obat_per_resep = models.CharField(max_length=5, blank=True, null=True)
    pemakaian_air_pdam = models.CharField(max_length=5, blank=True, null=True)
    limbah_b3_medis = models.CharField(max_length=5, blank=True, null=True)
    grafik_air_pdam_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_air_pdam_perbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_limbahb3_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_limbahb3_perbulan = models.CharField(max_length=5, blank=True, null=True)
    limbah_domestik = models.CharField(max_length=5, blank=True, null=True)
    grafik_limbahdomestik_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_limbahdomestik_perbulan = models.CharField(max_length=5, blank=True, null=True)
    mutu_air_limbah = models.CharField(max_length=5, blank=True, null=True)
    pest_control = models.CharField(max_length=5, blank=True, null=True)
    ruang_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    kategori_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    jenis_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    pengarang_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    penerbit_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    koleksi_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    inventaris_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    set_peminjaman_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    denda_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    anggota_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    peminjaman_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    bayar_denda_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    ebook_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    jenis_cidera_k3rs = models.CharField(max_length=5, blank=True, null=True)
    penyebab_k3rs = models.CharField(max_length=5, blank=True, null=True)
    jenis_luka_k3rs = models.CharField(max_length=5, blank=True, null=True)
    lokasi_kejadian_k3rs = models.CharField(max_length=5, blank=True, null=True)
    dampak_cidera_k3rs = models.CharField(max_length=5, blank=True, null=True)
    jenis_pekerjaan_k3rs = models.CharField(max_length=5, blank=True, null=True)
    bagian_tubuh_k3rs = models.CharField(max_length=5, blank=True, null=True)
    peristiwa_k3rs = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_pertahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perjeniscidera = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perpenyebab = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perjenisluka = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_lokasikejadian = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_dampakcidera = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perjenispekerjaan = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perbagiantubuh = models.CharField(max_length=5, blank=True, null=True)
    jenis_cidera_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    penyebab_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    jenis_luka_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    lokasi_kejadian_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    dampak_cidera_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    jenis_pekerjaan_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    bagian_tubuh_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    sekrining_rawat_jalan = models.CharField(max_length=5, blank=True, null=True)
    bpjs_histori_pelayanan = models.CharField(max_length=5, blank=True, null=True)
    rekap_mutasi_berkas = models.CharField(max_length=5, blank=True, null=True)
    skrining_ralan_pernapasan_pertahun = models.CharField(max_length=5, blank=True, null=True)
    pengajuan_barang_medis = models.CharField(max_length=5, blank=True, null=True)
    pengajuan_barang_nonmedis = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_ranapbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_ranaptanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_ranap_peruang = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_bangsal_pertahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_jenjang_jabatanpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_bidangpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_departemenpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_pendidikanpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_sttswppegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_sttskerjapegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_sttspulangranap = models.CharField(max_length=5, blank=True, null=True)
    kip_pasien_ranap = models.CharField(max_length=5, blank=True, null=True)
    kip_pasien_ralan = models.CharField(max_length=5, blank=True, null=True)
    bpjs_mapping_dokterdpjp = models.CharField(max_length=5, blank=True, null=True)
    data_triase_igd = models.CharField(max_length=5, blank=True, null=True)
    master_triase_skala1 = models.CharField(max_length=5, blank=True, null=True)
    master_triase_skala2 = models.CharField(max_length=5, blank=True, null=True)
    master_triase_skala3 = models.CharField(max_length=5, blank=True, null=True)
    master_triase_skala4 = models.CharField(max_length=5, blank=True, null=True)
    master_triase_skala5 = models.CharField(max_length=5, blank=True, null=True)
    master_triase_pemeriksaan = models.CharField(max_length=5, blank=True, null=True)
    master_triase_macamkasus = models.CharField(max_length=5, blank=True, null=True)
    rekap_permintaan_diet = models.CharField(max_length=5, blank=True, null=True)
    daftar_pasien_ranap = models.CharField(max_length=5, blank=True, null=True)
    daftar_pasien_ranaptni = models.CharField(max_length=5, blank=True, null=True)
    pengajuan_asetinventaris = models.CharField(max_length=5, blank=True, null=True)
    item_apotek_jenis = models.CharField(max_length=5, blank=True, null=True)
    item_apotek_kategori = models.CharField(max_length=5, blank=True, null=True)
    item_apotek_golongan = models.CharField(max_length=5, blank=True, null=True)
    item_apotek_industrifarmasi = models.CharField(max_length=5, blank=True, null=True)
    number_10_obat_terbanyak_poli = models.CharField(db_column='10_obat_terbanyak_poli', max_length=5, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    grafik_pengajuan_aset_urgensi = models.CharField(max_length=5, blank=True, null=True)
    grafik_pengajuan_aset_status = models.CharField(max_length=5, blank=True, null=True)
    grafik_pengajuan_aset_departemen = models.CharField(max_length=5, blank=True, null=True)
    rekap_pengajuan_aset_departemen = models.CharField(max_length=5, blank=True, null=True)
    grafik_kelompok_jabatanpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_resiko_kerjapegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_emergency_indexpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_inventaris_ruang = models.CharField(max_length=5, blank=True, null=True)
    harian_hais2 = models.CharField(db_column='harian_HAIs2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_inventaris_jenis = models.CharField(max_length=5, blank=True, null=True)
    data_resume_pasien = models.CharField(max_length=5, blank=True, null=True)
    perkiraan_biaya_ranap = models.CharField(max_length=5, blank=True, null=True)
    rekap_obat_poli = models.CharField(max_length=5, blank=True, null=True)
    rekap_obat_pasien = models.CharField(max_length=5, blank=True, null=True)
    permintaan_perbaikan_inventaris = models.CharField(max_length=5, blank=True, null=True)
    grafik_hais_pasienbangsal = models.CharField(db_column='grafik_HAIs_pasienbangsal', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_pasienbulan = models.CharField(db_column='grafik_HAIs_pasienbulan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_vap = models.CharField(db_column='grafik_HAIs_laju_vap', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_iad = models.CharField(db_column='grafik_HAIs_laju_iad', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_pleb = models.CharField(db_column='grafik_HAIs_laju_pleb', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_isk = models.CharField(db_column='grafik_HAIs_laju_isk', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_ilo = models.CharField(db_column='grafik_HAIs_laju_ilo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_hap = models.CharField(db_column='grafik_HAIs_laju_hap', max_length=5, blank=True, null=True)  # Field name made lowercase.
    inhealth_mapping_poli = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_dokter = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_tindakan_ralan = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_tindakan_ranap = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_tindakan_radiologi = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_tindakan_laborat = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_tindakan_operasi = models.CharField(max_length=5, blank=True, null=True)
    hibah_obat_bhp = models.CharField(max_length=5, blank=True, null=True)
    asal_hibah = models.CharField(max_length=5, blank=True, null=True)
    asuhan_gizi = models.CharField(max_length=5, blank=True, null=True)
    inhealth_kirim_tagihan = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_obat4 = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_obat5 = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_non_medis2 = models.CharField(max_length=5, blank=True, null=True)
    monitoring_asuhan_gizi = models.CharField(max_length=5, blank=True, null=True)
    penerimaan_obat_perbulan = models.CharField(max_length=5, blank=True, null=True)
    rekap_kunjungan = models.CharField(max_length=5, blank=True, null=True)
    surat_sakit = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_keperawatan_ralan = models.CharField(max_length=5, blank=True, null=True)
    permintaan_diet = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'


class UtdCekalDarah(models.Model):
    no_donor = models.OneToOneField('UtdDonor', on_delete = models.CASCADE, db_column='no_donor', primary_key=True)
    tanggal = models.DateField(blank=True, null=True)
    dinas = models.CharField(max_length=5, blank=True, null=True)
    petugas_pemusnahan = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='petugas_pemusnahan', blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_cekal_darah'


class UtdDetailPemisahanKomponen(models.Model):
    no_donor = models.ForeignKey('UtdPemisahanKomponen', on_delete = models.CASCADE, db_column='no_donor', blank=True, null=True)
    no_kantong = models.CharField(primary_key=True, max_length=15)
    kode_komponen = models.CharField(max_length=5, blank=True, null=True)
    tanggal_kadaluarsa = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_detail_pemisahan_komponen'


class UtdDonor(models.Model):
    no_donor = models.CharField(primary_key=True, max_length=15)
    nama = models.CharField(max_length=60, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    dinas = models.CharField(max_length=5, blank=True, null=True)
    jk = models.CharField(max_length=1, blank=True, null=True)
    umur = models.IntegerField(blank=True, null=True)
    alamat = models.CharField(max_length=100, blank=True, null=True)
    golongan_darah = models.CharField(max_length=2, blank=True, null=True)
    resus = models.CharField(max_length=3, blank=True, null=True)
    tensi = models.CharField(max_length=7, blank=True, null=True)
    no_bag = models.IntegerField(blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    jenis_bag = models.CharField(max_length=2, blank=True, null=True)
    jenis_donor = models.CharField(max_length=2, blank=True, null=True)
    tempat_aftap = models.CharField(max_length=12, blank=True, null=True)
    petugas_aftap = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='petugas_aftap', blank=True, null=True)
    hbsag = models.CharField(max_length=7, blank=True, null=True)
    hcv = models.CharField(max_length=7, blank=True, null=True)
    hiv = models.CharField(max_length=7, blank=True, null=True)
    spilis = models.CharField(max_length=7, blank=True, null=True)
    malaria = models.CharField(max_length=7, blank=True, null=True)
    petugas_u_saring = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='petugas_u_saring', blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_donor'


class UtdKomponenDarah(models.Model):
    kode = models.CharField(primary_key=True, max_length=5)
    nama = models.CharField(max_length=70, blank=True, null=True)
    lama = models.SmallIntegerField(blank=True, null=True)
    jasa_sarana = models.FloatField(blank=True, null=True)
    paket_bhp = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    manajemen = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    pembatalan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_komponen_darah'


class UtdMedisRusak(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    jml = models.FloatField(blank=True, null=True)
    hargabeli = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip')
    tanggal = models.DateTimeField()
    keterangan = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_medis_rusak'
        unique_together = (('kode_brng', 'nip', 'tanggal'),)


class UtdPemisahanKomponen(models.Model):
    no_donor = models.OneToOneField(UtdDonor, on_delete = models.CASCADE, db_column='no_donor', primary_key=True)
    tanggal = models.DateField(blank=True, null=True)
    dinas = models.CharField(max_length=5, blank=True, null=True)
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_pemisahan_komponen'


class UtdPengambilanMedis(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    jml = models.FloatField(blank=True, null=True)
    hargabeli = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    kd_bangsal_dr = models.ForeignKey(Bangsal, on_delete = models.CASCADE, db_column='kd_bangsal_dr')
    tanggal = models.DateTimeField()
    keterangan = models.CharField(max_length=60, blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'utd_pengambilan_medis'
        unique_together = (('kode_brng', 'tanggal', 'no_batch', 'no_faktur'),)


class UtdPengambilanPenunjang(models.Model):
    kode_brng = models.OneToOneField(Ipsrsbarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip')
    tanggal = models.DateTimeField()
    keterangan = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_pengambilan_penunjang'
        unique_together = (('kode_brng', 'nip', 'tanggal'),)


class UtdPenggunaanMedisDonor(models.Model):
    no_donor = models.OneToOneField(UtdDonor, on_delete = models.CASCADE, db_column='no_donor', primary_key=True)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_penggunaan_medis_donor'
        unique_together = (('no_donor', 'kode_brng'),)


class UtdPenggunaanMedisPemisahanKomponen(models.Model):
    no_donor = models.OneToOneField(UtdPemisahanKomponen, on_delete = models.CASCADE, db_column='no_donor', primary_key=True)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_penggunaan_medis_pemisahan_komponen'
        unique_together = (('no_donor', 'kode_brng'),)


class UtdPenggunaanMedisPenyerahanDarah(models.Model):
    no_penyerahan = models.OneToOneField('UtdPenyerahanDarah', on_delete = models.CASCADE, db_column='no_penyerahan', primary_key=True)
    kode_brng = models.ForeignKey(Databarang, on_delete = models.CASCADE, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_penggunaan_medis_penyerahan_darah'
        unique_together = (('no_penyerahan', 'kode_brng'),)


class UtdPenggunaanPenunjangDonor(models.Model):
    no_donor = models.OneToOneField(UtdDonor, on_delete = models.CASCADE, db_column='no_donor', primary_key=True)
    kode_brng = models.ForeignKey(Ipsrsbarang, on_delete = models.CASCADE, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_penggunaan_penunjang_donor'
        unique_together = (('no_donor', 'kode_brng'),)


class UtdPenggunaanPenunjangPemisahanKomponen(models.Model):
    no_donor = models.OneToOneField(UtdPemisahanKomponen, on_delete = models.CASCADE, db_column='no_donor', primary_key=True)
    kode_brng = models.ForeignKey(Ipsrsbarang, on_delete = models.CASCADE, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_penggunaan_penunjang_pemisahan_komponen'
        unique_together = (('no_donor', 'kode_brng'),)


class UtdPenggunaanPenunjangPenyerahanDarah(models.Model):
    no_penyerahan = models.OneToOneField('UtdPenyerahanDarah', on_delete = models.CASCADE, db_column='no_penyerahan', primary_key=True)
    kode_brng = models.ForeignKey(Ipsrsbarang, on_delete = models.CASCADE, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_penggunaan_penunjang_penyerahan_darah'
        unique_together = (('no_penyerahan', 'kode_brng'),)


class UtdPenunjangRusak(models.Model):
    kode_brng = models.OneToOneField(Ipsrsbarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    nip = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip')
    tanggal = models.DateTimeField()
    keterangan = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_penunjang_rusak'
        unique_together = (('kode_brng', 'nip', 'tanggal'),)


class UtdPenyerahanDarah(models.Model):
    no_penyerahan = models.CharField(primary_key=True, max_length=17)
    tanggal = models.DateField(blank=True, null=True)
    dinas = models.CharField(max_length=5, blank=True, null=True)
    nip_cross = models.ForeignKey(Petugas, on_delete = models.CASCADE, db_column='nip_cross', blank=True, null=True)
    keterangan = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=13, blank=True, null=True)
    kd_rek = models.ForeignKey(Rekening, on_delete = models.CASCADE, db_column='kd_rek', blank=True, null=True)
    pengambil_darah = models.CharField(max_length=70, blank=True, null=True)
    alamat_pengambil_darah = models.CharField(max_length=120, blank=True, null=True)
    nip_pj = models.CharField(max_length=20, blank=True, null=True)
    besarppn = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_penyerahan_darah'


class UtdPenyerahanDarahDetail(models.Model):
    no_penyerahan = models.OneToOneField(UtdPenyerahanDarah, on_delete = models.CASCADE, db_column='no_penyerahan', primary_key=True)
    no_kantong = models.ForeignKey('UtdStokDarah', on_delete = models.CASCADE, db_column='no_kantong')
    jasa_sarana = models.FloatField(blank=True, null=True)
    paket_bhp = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    manajemen = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_penyerahan_darah_detail'
        unique_together = (('no_penyerahan', 'no_kantong'),)


class UtdStokDarah(models.Model):
    no_kantong = models.CharField(primary_key=True, max_length=20)
    kode_komponen = models.ForeignKey(UtdKomponenDarah, on_delete = models.CASCADE, db_column='kode_komponen', blank=True, null=True)
    golongan_darah = models.CharField(max_length=2, blank=True, null=True)
    resus = models.CharField(max_length=3, blank=True, null=True)
    tanggal_aftap = models.DateField(blank=True, null=True)
    tanggal_kadaluarsa = models.DateField(blank=True, null=True)
    asal_darah = models.CharField(max_length=16, blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_stok_darah'


class UtdStokMedis(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    stok = models.FloatField(blank=True, null=True)
    hargaterakhir = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_stok_medis'


class UtdStokPenunjang(models.Model):
    kode_brng = models.OneToOneField(Ipsrsbarang, on_delete = models.CASCADE, db_column='kode_brng', primary_key=True)
    stok = models.FloatField(blank=True, null=True)
    hargaterakhir = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'utd_stok_penunjang'
