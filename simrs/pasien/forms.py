from django import forms
from simrs.models.pasien import Penjab

class formPenjab(forms.ModelForm):
    class Meta:
        model = Penjab
        fields =[
            'kd_pj',
            'png_jawab'
        ]
        widgets = {
            'kd_pj':forms.TextInput(
                attrs={
                    'class':'easyui-textbox',
                    'name':'kd_pj',
                    'id':'kd_pj',
                }
            ),
            'png_jawab':forms.TextInput(
                attrs={
                    'class':'easyui-textbox',
                    'name':'png_jawab',
                    'id':'png_jawab',
                }
            ),
        }