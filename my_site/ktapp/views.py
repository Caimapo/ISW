from django.shortcuts import render, render_to_response, get_object_or_404
from ktapp.forms import CategoriaForm
from django.http import HttpResponseRedirect
from .models import Categoria, Documento, Document
from django.views.decorators.csrf  import csrf_protect
from urllib.request import *
from urllib.parse import *
from bs4 import BeautifulSoup
import os
# Create your views here.
def index(request):
    return render_to_response('index.html')

def buscar(request):
    Document.objects.all().delete()
    if request.POST:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            print(data['nombre'])

            soup_busqueda = BeautifulSoup(urlopen(
                "http://www.fisicanet.com.ar/buscador/fis_buscador.php?criterio=" + data['nombre'] + "&Buscar=Buscar&registros=1000&como=todas"),
                                          'html.parser')

            lista_links = []
            # obtenemos la informacion para obtener los links de las busquedas
            busqueda = soup_busqueda.find_all("div", class_="brBot1")
            for i in busqueda:
                for j in i.find_all('a'):
                    lista_links.append(j['href'])
                    # se agregan en una lista los url de las paginas de la busqueda hecha
            contador = 1
            print("Entro al archivo  " + str(contador))
            # for en el que va entrando pagina por pagina extrañendo imagenes y texto
            for links in lista_links:
                if contador > 10:
                    break
                # se busca la informacion en relacion a la pagina
                sopa_de_cada_busqueda = BeautifulSoup(urlopen(links), 'html.parser')
                # extraemos el texto sobre la materia
                texto1 = sopa_de_cada_busqueda.find(itemprop="articleBody").get_text()

                contador= contador+1
                print(contador)
                imagenes = sopa_de_cada_busqueda.find(itemprop="articleBody").find_all("img")
                urlimagenes = []
                print("lego a imagen for  " + str(contador))
                # entra al for para extraer las imaagenes
                for imagen in imagenes:
                    # se crea el link que nos llevara a la imagen en el buscador web
                    link = urljoin(links, imagen['src'])
                    urlimagenes.append(link)
                    if "img/" in link:
                        break
                agregar = Document(texto=texto1, numero=contador)
                agregar.save()
            return HttpResponseRedirect('/resultado')
    else:
        form = CategoriaForm()

    args = {}

    args['form'] = form
    return render(request, 'buscar_articulo.html', args)

def resultado(request):
    all_documentos = Document.objects.all()
    return render(request, 'resultado.html', {'all_documentos': all_documentos})