from django import forms

class EncryptForm(forms.Form):
    Encrypt = forms.CharField()
    Key = forms.CharField()

class DecryptForm(forms.Form):
    Decrypt = forms.CharField()
    Key = forms.CharField()
