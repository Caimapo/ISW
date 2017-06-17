from django.contrib import admin
from .models import Documento, Categoria,Document,Clasificar

# Register your models here.
admin.site.register(Documento)
admin.site.register(Categoria)
admin.site.register(Document)
admin.site.register(Clasificar)