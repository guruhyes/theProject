from django.urls import path
from .views import crudPenjab

urlpatterns = [
    path('penjab/',crudPenjab.index,name="indexPenjab"),
    path('deletePenjab/',crudPenjab.deletePenjab,name="deletePenjab"),
    path('dgPenjab/',crudPenjab.dgPenjab,name="dgPenjab"),
    path('simpanPenjab/',crudPenjab.simpanPenjab,name="simpanPenjab"),
    path('simpanPenjab/<str:id>',crudPenjab.simpanPenjab,name="simpanPenjab"),
]
