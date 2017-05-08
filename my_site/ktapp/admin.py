from django.contrib import admin
from .models import Documento, Categoria,Document

# Register your models here.
admin.site.register(Documento)
admin.site.register(Categoria)
admin.site.register(Document)