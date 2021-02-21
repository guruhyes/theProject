from django.urls import path
from .views import (
    crudPoliklinik,
    crudBangsal,
    crudKamar,
)
urlpatterns = [
    path('',crudPoliklinik.index,name="poliklinik"),
    path('bangsal',crudBangsal.index,name="bangsal"),
    path('bedTerakhir/',crudKamar.bedTerakhir,name="bedTerakhir"),
    path('bedTerakhir/<str:lbed>',crudKamar.bedTerakhir,name="bedTerakhir"),
    path('cmBangsal/',crudBangsal.cmBangsal,name="cmBangsal"),
    path('dgBangsal/',crudBangsal.dgBangsal,name="dgBangsal"),
    path('dgKamar/',crudKamar.dgKamar,name="dgKamar"),
    path('dgPoliklinik/',crudPoliklinik.dgPoliklinik,name="dgPoliklinik"),
    path('deleteBangsal',crudBangsal.hapusBangsal,name="hapusBangsal"),
    path('deletePoliklinik',crudPoliklinik.deletePolilinik,name="deletePoliklinik"),
    path('deleteKamar',crudKamar.hapusKamar,name="deleteKamar"),
    path('kamar',crudKamar.index,name="kamar"),
    path('simpanBangsal/',crudBangsal.simpanBangsal,name="simpanBangsal"),
    path('simpanBangsal/<str:id>',crudBangsal.simpanBangsal,name="simpanBangsal"),
    path('simpanKamar/',crudKamar.simpanKamar,name="simpanKamar"),
    path('simpanKamar/<str:id>',crudKamar.simpanKamar,name="simpanKamar"),
    path('simpanPoliklinik/',crudPoliklinik.simpanPoliklinik,name="simpanPoliklinik"),
    path('simpanPoliklinik/<str:id>',crudPoliklinik.simpanPoliklinik,name="simpanPoliklinik"),
]
