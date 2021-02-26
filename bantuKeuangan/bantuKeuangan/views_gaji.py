from django.shortcuts import render

def index(request):
    context={
        'judul':'Gaji'
    }
    return render(request,'gaji.html',context)