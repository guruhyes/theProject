from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db import connection
import datetime
from django.db.models import F
from django.db.models import Q
import os,time
import hashlib
import random
import base64
import urllib
import hmac

##### Build in Untuk Jeasy UI Combobox #######
##### Parameter 'ob' => object dari suatu model-> ex: model.objects.all()
##### Parameter 'ar' => List Field yang akan di tambilkan di combobobox
##### sl => setting untuk membuat combobox default value ketika halaman di load -> nilainya 0(off) atau 1(on) Default is 0
##### id => parameter untuk mencari satu atau lebih berdasarkan parameter inputan
##### param=> parameter untuk mencari default combo
##### offtable => digunakan di url template, untuk melakukan query diluar ar parameter
##### absolute => digunakan untuk pencarian absolute match query
def comboJson(request,ob,ar,sl=0,id="",param="",offtable="",abso=""):
    #datacombo = ob
    if(len(ar)<=1):
        #pp=ar[0]+"__startswith"
        pp=ar[0]+"__icontains"
    elif(offtable!="" and param!=""):
        #yy=offtable + "__startswith"
        yy=offtable + "__icontains"
    elif(abso!="" and param!=""):
        kk=ar[1]
        pp=ar[0]
    else:
        #kk=ar[1]+"__startswith" 
        #pp=ar[0]+"__startswith"
        kk=ar[1]+"__icontains"
        pp=ar[0]+"__icontains"
        #like '%'
        
    #print(yy)
    try :
        ob.__name__
        # datacombo = ob.objects.filter(ar[0]__icontains=param)
        if(len(ar)<=1):
            datacombo = ob.objects.filter(**{pp: param})
        elif(offtable!="" and param!=""):
            cuy = ob.objects.filter(Q(**{yy: param}))
            if cuy:
                datacombo = ob.objects.filter(Q(**{yy: param}))
            else:
                datacombo = ob.objects.filter(Q(**{yy: ""})) 

        else:
            datacombo = ob.objects.filter(Q(**{kk:param}) | Q(**{pp:param}))
            
            #datacombo = ob.objects.filter(Q(**{kk:param}))
        #datacombo = ob.objects.all()
    except:
        datacombo = ob
    data=[]
    x=0
    y=0

    for dataCombo in datacombo:
        result={}
        
        
        if id:
            
            if id==dataCombo.id_ruang.strip():
                while x < len(ar):
                    try:
                        result[ar[x]]=getattr(dataCombo,ar[x]).strip()
                    except:
                        result[ar[x]]=getattr(dataCombo,ar[x])
                    if sl==1:
                        if(y==0):
                            result['selected']="true"
                    x +=1
                    y +=1
                x=0
                
                data.append(result)
                
        else:
            while x < len(ar):
                try:
                    result[ar[x]]=getattr(dataCombo,ar[x]).strip()
                except:
                    result[ar[x]]=getattr(dataCombo,ar[x])
                if sl==1:
                    if(y==0):
                        result['selected']="true"
                x +=1
                y +=1
            x=0
            
            data.append(result)
    return JsonResponse(data,safe=False)

##### Build in untuk Jeasyu Ui Datagrid dengan Pagination ######
##### sort_by => digunakan untuk mengurutkan data--> full object ex:klinik.id_klinik,sdm.id_pasien
##### query_total => menghitung jumlah baris dari query --> raw query
##### query_data => list data yang di cari --> raw query
##### model => model atau table yang akan digunakan
##### page and rows default value =>request.POST['page'] dan request.POST['rows']
##### tgl => return value dari fungsi parameterExecption, digunakan untuk parameter tanggal
##### **kwargs menangkap data yang berupa dict => lihat jsonView.paramException()
##### **kwargs bisa langsung di dideklarasikan di view menggunakan request.POST.get()
def datagridJson(sort_by,query_total,query_data,model,request,tgl="",**kwargs):
    #print(kwargs)
    #print(str(tgl))
    try:
        page = request.POST['page']
    except:
        page = 1
    else :
        page
    try :
        rows = request.POST['rows']
    except:
        rows = 10
    else:
        rows
    offse = (int(page) - 1)* int(rows)
    ### QUERY DI BAWAH UNTUK MENCARI TOTAL DATA PASIEN
    #queryTotal = "select count(*) from klinik"
    
    #tele ="order by {} asc OFFSET {} ROWS FETCH NEXT {} ROWS ONLY".format(sort_by,int(offse),int(rows))
    tele ="order by {} asc LIMIT {} OFFSET {}".format(sort_by,int(rows),int(offse))
    s=""
    for key,value in kwargs.items():
        if value==None:
            st = " and {} like '%%'".format(key)
        elif value=='':
            st = " and {} like '%{}%'".format(key,value)
        else:
            st = " and {} like '%%{}%%'".format(key,value)
        s +=st
    if len(kwargs)==0:
        whereParam=""
    else:
        whereParam ="where "+s[5:]
    #print(whereParam)
    #print(s[5:])
    #print(whereParam)
    cursor = connection.cursor()
    qtot = query_total+" "+whereParam+" "+str(tgl)
    #print(qtot)
    cursor.execute(qtot)
    for resultTotal in cursor.fetchone():
        resultTotal

    paramQuery = (int(offse),int(rows))
    query = query_data+" "+str(whereParam)+" "+str(tgl)+" "+tele
    #print(query)
    jsonData = model.objects.raw(query)
    data=[]
    x=1
    #print(jsonData.query)
    for jsondata in jsonData:
        yy = list(jsondata.__dict__.keys())
        #print(len(ll))
        #print(getattr(jsondata,ll[1]))
        result={}
        while x < len(yy):
            result[yy[x]]=getattr(jsondata,yy[x])
            x +=1
        x=1
        data.append(result)
    tt ={}
    total = resultTotal
    tt['total']=total
    tt['rows']=data
    #print(tt)
    return JsonResponse(tt,safe=False)
#### Form save
#### Request from POST
#### id => Jika akan adanya perbuahan data atau update
#### Requirements -> Form dibuat dari Forms Model
#### Model Name => object model name, jika menggunakan Full path Model ex(models.Model) maka perlu di import ulang menjadi nama model ex(klinik)
#### kwKey => key untuk keyword args -> merupakan fields db yang akan digunakan untuk dijadikan parameter pencarian primary key atau field update
#### kwVal => value untuk keyword args -> parameter pencarian 
#### formName => nama Form -> String
#### forms => Forms Object 
#### Param => kwargs yang digunakan untuk override form dari template
"""
example kwargs
    kwargs={'field':'value',dll}
    field -> merupakan field form atau field database yang akan di ovveride
    value -> merupakan nilai atau value baru 

"""
def saveForm(request,modelName,kwKey,kwVal,formName,forms,**param):
    kwargs = {kwKey:kwVal}
    #print(kwargs)
    #dd={'id_agama':'8','agama':'c','ll':'s'}
    result={}
    result.clear()
    keyi=""
    for tt in request.POST:
        
        result[tt]=request.POST[tt] 
        for key,value in param.items():
            keyi=key
            if tt==key:
                if tt==str(keyi):
                    result[tt]=value
            elif request.POST[tt]=="":
                if tt==str(keyi):
                    result[tt]=value
    param.clear()
    #print(result)
    if request.method=='POST':
        if kwVal:
            try:
                cekAgama = get_object_or_404(modelName,**kwargs)
                form = getattr(forms,formName)(result,instance=cekAgama)
                err = []
                tt = form.errors
                #print(form.errors)
                for yy in form.errors.items():
                    for kk in yy:
                        print(kk)
                print(form)
                if form.is_valid():
                    form.save()
                    print(connection.queries[-1])
                    return JsonResponse({'success':'data terupdate'})
                else:
                    return JsonResponse({'errorMsg':kk})
            except cekAgama.DoesNotExist:
                return JsonResponse({'errorMsg':'Tidak Ada Data Ter Update'}) 
        else:
            form = getattr(forms,formName)(result)
            #form = getattr(forms,formName)()
            err = []
            tt = form.errors
            #print(form.errors)
            for yy in form.errors.items():
                for kk in yy:
                    print(kk)
            #### fetch error di bawah {{deprecated}}
            #### ada sebagaian error yang beraada diluar form
                    # for ll in form:
                    #     #print(ll.errors)
                    #     for kk in ll.errors:
                    #         print(kk)
            #### fetch error di atas {{deprecated}}

            #### ada sebagaian error yang beraada diluar form        
            #print(tt)
            #form.agama='test'
            #form.initial["agama"] ="test"
            if form.is_valid():
                #form.save(commit=False)
                #form.fields['agama'] ="test"
                #form.cleaned_data['Email'] = "test"
                #student = form.save(commit=False)
                # commit=False tells Django that "Don't send this to database yet.
                # I have more things I want to do with it."

                form.save()
                #print(connection.queries[-1])
                return JsonResponse({'success':'Simpan Berhasil'})
            else:
                return JsonResponse({'errorMsg':kk},status=500)
##### Digunakan untuk parameter pencarian
##### Untuk ngakali ketika post request gagal, maka value akan diisi dengan default value yang di inginkan
##### request => di ambil dari request data dari form templates
##### kwargs param => mengampil parameter yang di inputkan -> format dictionary
'''
example :
    param=['satu','dua','dll']
    param merupakan list dari variable yang di parsing dari form

'''
#### Fungsi ini hanya digunakan untuk parameter String 
#### param => list parameter yang digunakan untuk pencarian di query
#### param => ['db.field1','db.field2',dll]
#### param => field , variable harus sama
#### param => db. (database reference untuk query, harus diisi)
def paramException(request,*param):
    
    kwargs={}
    kwargs.clear()
    x=0
    for susu in param:
        try:
            dada=susu.split('.')
            #print(susu.split('.'))
            request.POST[dada[1]]
            
            kwargs[susu]=request.POST[dada[1]]
            #print(kwargs)
        except :
            pass
        x+=1
    return kwargs
#### Inquery parameter yang menggunakan tanggal
#### request => Mengambila seluruh data dari post
#### var1 => variable tanggal awal -> String
#### var2 => variable tanggal akhir -> String
#### field => field tanggal dalam database yang akan dicari 
#### field => format list -> ['db.field1','db.field2']

def paramTanggal(request,var1,var2,field):
    tgl1=""
    tgl2=""
    #print(var1)
    #lo = datetime.datetime.strptime("21/12/2008", "%d/%m/%Y").strftime("%Y-%m-%d")
    if request.POST.get(var1) and request.POST.get(var2):
        try:
            request.POST[var1]
            tgl1 = datetime.datetime.strptime(request.POST[var1], "%d/%m/%Y").strftime("%Y-%m-%d 00:00:00")
            
        except :
            pass
        try:
            request.POST[var2]
            tgl2 = datetime.datetime.strptime(request.POST[var2], "%d/%m/%Y").strftime("%Y-%m-%d 23:59:59")
        except:
            pass
        stri = " and {} between '{}' and '{}'".format(field,tgl1,tgl2)
    else:
        stri=""
    return stri
#### konversi short date
def konveriTanggal(tgl1,forma=""):
    paramTanggal=str(tgl1)[0:10]
    if forma=="":
        try:
            tanggal = datetime.datetime.strptime(paramTanggal, "%Y-%m-%d").strftime("%d/%m/%Y")
            return tanggal
        except :
            return None
    elif forma=="yyyy-mm-dd":
        try:
            tanggal = datetime.datetime.strptime(paramTanggal, "%d/%m/%Y").strftime("%Y-%m-%d")
            return tanggal
        except :
            return None
    elif forma=="pot-yyyy-mm-dd":
        try:
            tanggal = datetime.datetime.strptime(paramTanggal, "%Y-%m-%d").strftime("%Y-%m-%d")
            return tanggal
        except :
            return None
#### Konversi Long date
#### input => dd/mm/YYYY hh:mm:ss
#### output => YYYY-mm-dd hh:mm:ss
def konversiLongDate(tgl1):
    os.environ['TZ'] = 'Asia/Jakarta'
    try:

        tt=datetime.datetime.strptime(tgl1, "%d/%m/%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
        yy = datetime.datetime.strptime(tt,"%Y-%m-%d %H:%M:%S")
        tete=datetime.datetime(yy.year,yy.month,yy.day,yy.hour,yy.minute,yy.second)
        return tete
    except:
        return None
def debug(**kwargs):
    print(kwargs)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
##### Parameter 'ob' => object dari suatu model-> ex: model.objects.all()
##### Parameter 'ar' => List Field yang akan di tambilkan di combobobox
##### param=> parameter untuk mencari default combo
##### alias =>kwargs untuk mengubah fields menjadi nama alias

def formLoad(request,ob,ar,param="",offtable="",**alias):
    #datacombo = ob
    if offtable!="":
        pp = offtable+"__icontains"
    else:
        pp=ar[0]+"__icontains"
    if alias=={}:
        try :
            ob.__name__
            datacombo = ob.objects.filter(**{pp: param})
        except:
            datacombo = ob
        x=0
        for dataCombo in datacombo:
            result={}
                
            while x < len(ar):

                result[ar[x]]=getattr(dataCombo,ar[x])
                x +=1
            x=0
        
    else:
        paramAlias={}
        for k,v in alias.items():
            paramAlias[v]=k
        #print(paramAlias)
        try :
            ob.__name__
            
            datacombo = ob.objects.filter(**{pp: param}).extra(select=paramAlias)
            
        except:
            datacombo = ob
            #print(datacombo.query)
        x=0
        
        for dataCombo in datacombo:
            result={}

            #print(alias)
            for l,o in alias.items():
                if(konveriTanggal(getattr(dataCombo,ar[x])))!=None:
                    if(l==ar[x]):
                        result[o]=konveriTanggal(getattr(dataCombo,ar[x]))
                    else:
                        result[ar[x]]=konveriTanggal(getattr(dataCombo,ar[x]))
                else:
                    
                    if(l==ar[x]):
                        result[o]=getattr(dataCombo,ar[x])
                        
                    else:
                        result[ar[x]]=getattr(dataCombo,ar[x])
                x +=1
                    
                
            # x=0
    
    return JsonResponse(result,safe=False)

def tarifPaket():
    pass

def deleteRecord(md,field,val):
    try:
        md.objects.get(field=val).delete()
        return JsonResponse({"success":"hapus berhasil"})
    except:
        return JsonResponse({"errorMsg":"Hapus Gagal"})
def bpjsVclaim():
    seconds = time.time()
    secretkey = '5yQ2C73905'
    dd="28740"
    data="28740"+"&"+str(int(seconds))
    key_bytes= bytes(secretkey , 'latin-1')
    data_bytes = bytes(data ,'latin-1')
    signature = hmac.new(key_bytes, data_bytes, digestmod=hashlib.sha256).digest()
    encodedSignature = base64.encodebytes(signature)
    lele = [dd,str(int(seconds)),encodedSignature.decode().replace('\n','')]
    headers = {
        'X-cons-id': dd,
        'X-timestamp': str(int(seconds)),
        'X-signature': encodedSignature.decode().replace('\n',''),
        }
    return headers
def bpjsVclaimPost():
    seconds = time.time()
    secretkey = '5yQ2C73905'
    dd="28740"
    data="28740"+"&"+str(int(seconds))
    key_bytes= bytes(secretkey , 'latin-1')
    data_bytes = bytes(data ,'latin-1')
    signature = hmac.new(key_bytes, data_bytes, digestmod=hashlib.sha256).digest()
    encodedSignature = base64.encodebytes(signature)
    lele = [dd,str(int(seconds)),encodedSignature.decode().replace('\n','')]
    headers = {
        'X-cons-id': dd,
        'X-timestamp': str(int(seconds)),
        'X-signature': encodedSignature.decode().replace('\n',''),
        'Content-Type':'Application/x-www-form-urlencoded',
        }
    return headers
def settingModul():
    data={
        'koders':'0150R010'
    }
    return data
def baseUrlVclaim():
    url = "https://dvlp.bpjs-kesehatan.go.id/vclaim-rest"
    return url


    