from django.shortcuts import render
from poliklinik import forms
from poliklinik.forms import formPoliklinik
from simrs import jsonView
from simrs.models.poliklinik import Poliklinik
from django.http import JsonResponse

def index(request):
    context={
        'formPoliklinik':formPoliklinik,
    }
    return render(request,'poliklinik/indexPoliklinik.html',context)

def dgPoliklinik(request):
    sort_by = "poliklinik.nm_poli"
    query_total = "select count(*) from poliklinik"
    query_data = "select * from poliklinik"
    kwargs={
        "kd_poli":request.POST.get('cKd_poli')
    }
    return jsonView.datagridJson(sort_by,query_total,query_data,Poliklinik,request,tgl="",**kwargs)

def simpanPoliklinik(request,id=None):
    return jsonView.saveForm(request,Poliklinik,'kd_poli',id,'formPoliklinik',forms)

def deletePolilinik(request):
    try:
        Poliklinik.objects.get(kd_poli=request.POST['kd_poli']).delete()
        return JsonResponse({"success":"Hapus Berhasil"})
    except:
        return JsonResponse({"errorMsg":"Hapus Gagal"})
    