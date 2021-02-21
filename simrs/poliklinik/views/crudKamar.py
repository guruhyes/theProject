from django.shortcuts import render
from simrs import jsonView
from simrs.models.poliklinik import Kamar
from poliklinik import forms
from django.http import JsonResponse,HttpResponse

def index(request):
    context={
        "formKamar":forms.formKamar
    }
    return render(request,'poliklinik/indexKamar.html',context)
def bedTerakhir(request,lbed):
    qu = "SELECT kd_kamar,max(cast(SUBSTRING_INDEX(kd_kamar,' ',-1) as unsigned)) as total from kamar where kd_bangsal='{}'".format(lbed)

    bed = Kamar.objects.raw(qu)
    for i in bed:
        return HttpResponse(i.total,content_type="text/plain")
def cekNomorKamar(kd_kamar):
    try:
        cek = Kamar.objects.get(kd_kamar=kd_kamar)
        return False
    except Kamar.DoesNotExist:
        return True
    
def dgKamar(request):
    sort_by = "bangsal.nm_bangsal"
    query_total = "select count(*) from kamar inner join bangsal on kamar.kd_bangsal=bangsal.kd_bangsal"
    query_data = """
    select kamar.kd_bangsal,kamar.kelas,kamar.statusdata,kamar.kd_kamar,bangsal.nm_bangsal,kamar.status,kamar.trf_kamar
    from kamar
    inner join bangsal on kamar.kd_bangsal=bangsal.kd_bangsal
    """
    kwargs={
        "nm_bangsal":request.POST.get('cNm_bangsal')
    }
    return jsonView.datagridJson(sort_by,query_total,query_data,Kamar,request,tgl="",**kwargs)

def hapusKamar(request):

    try:
        Kamar.objects.get(kd_kamar=request.POST['kd_kamar']).delete()
        return JsonResponse({"success":"hapus berhasil"})
    except:
        return JsonResponse({"errorMsg":"Hapus Gagal"})
def simpanKamar(request,id=None):
    kd_bangsal = request.POST['kd_bangsal']
    no_kamar = int(request.POST['no_kamar'])
    if id==None:
        while True:
            cek = kd_bangsal +"."+ str(no_kamar)
            if(cekNomorKamar(cek)==False):
                no_kamar += 1
            else:
                break
    kd_kamar = kd_bangsal +"."+ str(no_kamar)
    param={
        "kd_kamar":kd_kamar
    }
    return jsonView.saveForm(request,Kamar,'kd_kamar',id,'formKamar',forms,**param)