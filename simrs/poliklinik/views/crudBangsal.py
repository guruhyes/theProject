from django.shortcuts import render
from poliklinik import forms
from simrs import jsonView
from simrs.models.poliklinik import Bangsal
from django.http import JsonResponse
def index(request):
    context = {
        'formBangsal': forms.formBangsal
    }
    return render(request,'poliklinik/indexBangsal.html',context)
def cmBangsal(request):
    return jsonView.comboJson(request,Bangsal.objects.all(),['kd_bangsal','nm_bangsal'])
def dgBangsal(request):
    sort_by = "bangsal.nm_bangsal"
    query_total = "select count(*) from bangsal"
    query_data = "select * from bangsal"
    kwargs = {
        "kd_bangsal":request.POST.get('cKd_bangsal')
    }
    return jsonView.datagridJson(sort_by,query_total,query_data,Bangsal,request,tgl="",**kwargs)
def hapusBangsal(request):
    try:
        Bangsal.objects.get(kd_bangsal=request.POST['kd_bangsal']).delete()
        return JsonResponse({"success":"berhasil Hapus"})
    except:
        return JsonResponse({"errorMsg":"error Hapus Data"})
def simpanBangsal(request,id=None):
    return jsonView.saveForm(request,Bangsal,'kd_bangsal',id,'formBangsal',forms)