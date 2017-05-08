from django import forms
from ktapp.models import Categoria,Document,Documento


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)


