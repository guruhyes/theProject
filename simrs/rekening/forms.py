from django import forms
from rekening import models

class basicForm(forms.ModelForm):
    class Meta:
        model = models.Rekening
        fields=[
            'kd_rek',
            'nm_rek',
            'tipe',
            'balance',
            'level'
        ]
        widgets={
            'kd_rek':forms.TextInput(
                attrs={
                    'class':'easyui-textbox',
                    'name':'kd_rek',
                    'id':'kd_rek',
                }
            ),
            'nm_rek':forms.TextInput(
                attrs={
                    'class':'easyui-textbox',
                    'name':'nm_rek',
                    'id':'nm_rek',
                }
            ),
            'tipe':forms.TextInput(
                attrs={
                    'class':'easyui-combobox',
                    'id':'tipe',
                    'data-options':"data:[{vTipe:'N',tTipe:'N'},{vTipe:'K',tTipe:'K'}],valueField:'vTipe',textField:'tTipe'",
                }
            ),
            'balance':forms.TextInput(
                attrs={
                    'class':'easyui-combobox',
                    'id':'balance',
                    'data-options':"data:[{vBalance:'D',tBalance:'D'},{vBalance:'R',tBalance:'R'}],valueField:'vBalance',textField:'tBalance'",
                }
            ),
            'level':forms.TextInput(
                attrs={
                    'class':'easyui-combobox',
                    'id':'level',
                    'data-options':"data:[{vLevel:'0',tLevel:'0'},{vLevel:'1',tLevel:'1'}],valueField:'vLevel',textField:'tLevel'",
                }
            ),
        }