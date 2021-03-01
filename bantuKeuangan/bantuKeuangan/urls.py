"""bantuKeuangan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from . import views_gaji

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('gaji',views_gaji.index,name="gaji"),
    path('generateExcel/<str:form>',views_gaji.generateExcel,name="generateExcel"),
    path('doc/',views.doc,name='doc'),
    path('doc_test/',views.doc_test,name="doc_test"),
    path('exportExcel/',views.exportExcel,name="exportExcel"),
    path('exportWord/',views.exportWord,name="exportWord"),
    path('print/',views.print,name="weasyPrint"),
    path('replaceWord/',views.replaceWord,name="replaceWord"),
]
