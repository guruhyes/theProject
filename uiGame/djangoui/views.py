from django.shortcuts import render
from django.http import HttpResponse
import subprocess
# Create your views here.
def index(request):
    #return HttpResponse('test')
    return render(request,'base/desktop.html')
def uiGame(request):
    return render(request,'uiGame/ui.html')
def uiController(request):
    return render(request,'uiGame/uiController.html')
def uiBat(request):
    return render(request,'uiGame/uiBat.html')
def directCall(request):
    subprocess.call([r'C:\\Users\\bw\\Desktop\\sample.bat'])
def createFile(request):
    f = open(r'C:\\Users\\bw\\Desktop\\sample1.bat', "a")
    f.write("START /WAIT notepad \necho 'Hello World'")
    f.close()