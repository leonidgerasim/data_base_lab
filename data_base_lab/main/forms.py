from django import forms
from .models import Main


class MainForm(forms.Form):
    house = forms.CharField(widget=forms.TextInput, required=False)
    corpus = forms.CharField(widget=forms.TextInput, required=False)
    apart = forms.CharField(widget=forms.TextInput, required=False)
    tel = forms.CharField(widget=forms.TextInput, required=False)
    f_name_fk = forms.CharField(widget=forms.TextInput, required=False)
    surname_fk = forms.CharField(widget=forms.TextInput, required=False)
    otch_fk = forms.CharField(widget=forms.TextInput, required=False)
    street_fk = forms.CharField(widget=forms.TextInput, required=False)
