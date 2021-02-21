from django.shortcuts import render
from rekening.models import Rekening
from . import forms
from simrs import jsonView
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.
def index(request):
    context={
        'basicForm':forms.basicForm
    }
    return render(request,'rekening/indexRekening.html',context)

def deleteRekening(request):
    try:
        Rekening.objects.get(kd_rek=request.POST['id']).delete()
        return JsonResponse({'success':'delete berhasil'})
    except:
        return JsonResponse({'errorMsg':'error'})
    #print(request.POST['id'])
def dgRekening(request):
    sort_by = "rekening.nm_rek"
    query_total = "select count(*) from rekening"
    query_data = """
    select rekening.kd_rek,rekening.nm_rek,rekening.tipe,rekening.balance,rekening.level from rekening
    """
    kwargs={
        'kd_rek':request.POST.get('cKd_rek')
    }
    return jsonView.datagridJson(sort_by,query_total,query_data,Rekening,request,tgl="",**kwargs)
    # print(jsonView.paramException(request,['kunjungan.id_kunjungan']))

def simpan(request,id=None):
    #print(request.POST)
    return jsonView.saveForm(request,Rekening,'kd_rek',id,'basicForm',forms)
