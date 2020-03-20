from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EncryptForm, DecryptForm
from .vigenere import encrypting, decrypting

class EncryptView(TemplateView):
    def get(self, request):
        text = EncryptForm()
        return render(request, self.template_name, {'text' : text})

    def post(self, request):
        text = EncryptForm(request.POST)
        if text.is_valid():
            encrypt = text.cleaned_data['Encrypt']
            key = text.cleaned_data['Key']
            encrypted = encrypting(encrypt, key)
        return render(request, self.template_name, {'text' : text, 'encrypt' : encrypted})

class DecryptView(TemplateView):
    def get(self, request):
        text = DecryptForm()
        return render(request, self.template_name, {'text' : text})

    def post(self, request):
        text = DecryptForm(request.POST)
        if text.is_valid():
            decrypt = text.cleaned_data['Decrypt']
            key = text.cleaned_data['Key']
            decrypted = decrypting(decrypt, key)
        return render(request, self.template_name, {'text' : text, 'decrypt' : decrypted})
