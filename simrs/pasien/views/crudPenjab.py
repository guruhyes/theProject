from django.shortcuts import render
from simrs import jsonView
from django.http import JsonResponse
from simrs.models.pasien import Penjab
from pasien import forms
# Create your views here.
def index(request):
    context={
        "formPenjab":forms.formPenjab
    }
    return render(request,'pasien/indexPasien.html',context)
def deletePenjab(request):
    return jsonView.deleteRecord(Penjab,'kd_pj',request.POST['kd_pj'])
def dgPenjab(request):
    sort_by = "penjab.kd_pj"
    query_total = "select count(*) from penjab"
    query_data = "select * from penjab"
    kwargs={
        "png_jawab":request.POST.get['cPng_jawab']
    }
    return jsonView.datagridJson(sort_by,query_total,query_data,Penjab,request,tgl="",**kwargs)
def simpanPenjab(request,id=None):

    return jsonView.saveForm(request,Penjab,"kd_pj",id,'formPenjab',forms)
