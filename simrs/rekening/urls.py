from django.urls import path
from . import views
from .ff import views_d
urlpatterns = [
    path('',views.index,name="indexRekening"),
    path('deleteRekening/',views.deleteRekening,name="deleteRekening"),
    path('dgRekening/',views.dgRekening,name="dgRekening"),
    path('simpanRekening/',views.simpan,name="simpanRekening"),
    path('simpanRekening/<str:id>',views.simpan,name="simpanRekening"),
    path('ff/',views_d.index),
]

