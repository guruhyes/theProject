from django import forms
from simrs.models.poliklinik import (
    Bangsal,
    Kamar,
    Poliklinik,
)
class formPoliklinik(forms.ModelForm):
    class Meta:
        model = Poliklinik
        fields = [
            'kd_poli',
            'nm_poli',
            'registrasi',
            'registrasilama',
            'status',
        ]
        widgets={
            'kd_poli':forms.TextInput(
                attrs={
                    'class':'easyui-textbox',
                    'name':'kd_poli',
                    'id':'kd_poli',
                }
            ),
            'nm_poli':forms.TextInput(
                attrs={
                    'class':'easyui-textbox',
                    'name':'nm_poli',
                    'id':'nm_poli',
                }
            ),
            'registrasi':forms.TextInput(
                attrs={
                    'class':'easyui-numberbox',
                    'name':'registrasi',
                    'id':'registrasi',
                }
            ),
            'registrasilama':forms.TextInput(
                attrs={
                    'class':'easyui-numberbox',
                    'name':'registrasilama',
                    'id':'registrasilama',
                }
            ),
            'status':forms.TextInput(
                attrs={
                    'class':'easyui-combobox',
                    'id':'status',
                    'data-options':"data:[{vStatus:'0',tStatus:'0'},{vStatus:'1',tStatus:'1'}],valueField:'vStatus',textField:'tStatus'",
                }
            ),
            
        }

class formBangsal(forms.ModelForm):
    class Meta:
        model = Bangsal
        fields = [
            'kd_bangsal',
            'nm_bangsal',
            'status',
        ]
        widgets = {
            'kd_bangsal':forms.TextInput(
                attrs={
                    'class':'easyui-textbox',
                    'name':'kd_bangsal',
                    'id':'kd_bangsal',
                }
            ),
            'nm_bangsal':forms.TextInput(
                attrs={
                    'class':'easyui-textbox',
                    'name':'nm_bangsal',
                    'id':'nm_bangsal',
                }
            ),
            'status':forms.TextInput(
                attrs={
                    'class':'easyui-combobox',
                    'id':'status',
                    'data-options':"data:[{vStatus:'0',tStatus:'0'},{vStatus:'1',tStatus:'1'}],valueField:'vStatus',textField:'tStatus'",
                }
            ),
        }
class formKamar(forms.ModelForm):
    no_kamar = forms.CharField(max_length=10,widget=forms.TextInput(attrs={
        'class':'easyui-textbox',
        'name':'no_kamar',
        'id':'no_kamar',
        'readonly':'false',
    }))
    class Meta:
        model = Kamar
        fields = [
            'kd_bangsal',
            'kd_kamar',
            'trf_kamar',
            'status',
            'kelas',
            'statusdata',
        ]
        widgets={
            'kd_kamar':forms.TextInput(
                attrs={
                    'class':'easyui-textbox',
                    'name':'kd_kamar',
                    'id':'kd_kamar',
                    'readonly':'true',
                }
            ),
            'kd_bangsal':forms.TextInput(
                attrs={
                    'class':'easyui-combobox',
                    'data-options':"url:'cmBangsal/',valueField:'kd_bangsal',textField:'nm_bangsal'",
                    'style':"width:160px",
                    'id':'kd_bangsal'
                }
            ),
            'trf_kamar':forms.TextInput(
                attrs={
                    'class':'easyui-numberbox',
                    'name':'trf_kamar',
                    'id':'trf_kamar',
                }
            ),
            'status':forms.TextInput(
                attrs={
                    'class':'easyui-combobox',
                    'id':'status',
                    'data-options':"data:[{vStatus:'ISI',tStatus:'ISI'},{vStatus:'KOSONG',tStatus:'KOSONG'},{vStatus:'DIBERSIHKAN',tStatus:'DIBERSIHKAN'},{vStatus:'DIBOOKING',tStatus:'DIBOOKING'}],valueField:'vStatus',textField:'tStatus'",
                }
            ),
            'kelas':forms.TextInput(
                attrs={
                    'class':'easyui-combobox',
                    'id':'kelas',
                    'data-options':"data:[{vKelas:'kelas 1',tKelas:'kelas 1'},{vKelas:'kelas 2',tKelas:'kelas 2'},{vKelas:'kelas 3',tKelas:'kelas 3'},{vKelas:'kelas utama',tKelas:'kelas utama'},{vKelas:'kelas vip',tKelas:'kelas vip'},{vKelas:'kelas vvip',tKelas:'kelas vvip'}],valueField:'vKelas',textField:'tKelas'",
                }
            ),
            'statusdata':forms.TextInput(
                attrs={
                    'class':'easyui-combobox',
                    'id':'statusData',
                    'data-options':"url:'/static/rawJson/status.json',valueField:'vStatus',textField:'tStatus'",
                    'style':"width:160px"
                }
            ),
        }
