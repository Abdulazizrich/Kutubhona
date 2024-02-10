from django import forms
from .models import *

class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields='__all__'

class MuallifForm(forms.Form):
    ism=forms.CharField(label='ism')
    jins = forms.CharField(label="jins")
    tugilgan_sana = forms.DateTimeField(label='tugilgan_sana')
    kitoblar_soni = forms.IntegerField(label='kitoblar_soni')
    tirik = forms.BooleanField(label="tirik")

class KutubhonachiForm(forms.Form):
    ism=forms.CharField(label='ism')
    ish_vaqti = forms.CharField(label='ish_vaqti')

