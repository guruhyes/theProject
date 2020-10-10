from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse('test')
    return render(request,'base/desktop.html')
def uiGame(request):
    return render(request,'uiGame/ui.html')
def uiController(request):
    return render(request,'uiGame/uiController.html')