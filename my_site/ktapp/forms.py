from django import forms
from django.contrib.auth.models import User
from ktapp.models import Categoria,Document,Documento


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)


class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model =User
        fields = ['username', 'email', 'password']
