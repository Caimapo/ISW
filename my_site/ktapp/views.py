# coding=utf-8
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from ktapp.forms import CategoriaForm
from django.http import HttpResponseRedirect
from .models import Categoria, Documento, Document, Clasificar
from django.views.decorators.csrf  import csrf_protect
from urlparse import *
from urllib import *
from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
import os
from .clasificador import *
try:
    import cPickle as pickle
except ImportError:
    import pickle
# Create your views here.
def index(request):
    return render_to_response('index.html')

def UserFormView(request):
    template_name = 'registration_form.html'
    args = {}


    if request.POST:
        form = UserForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # limpiar (normalizar) datos
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user.set_password(password)
            user.save()

            # retorna User Objects si la credencial es correcta
            user = authenticate(email=email, username=username, password=password)

            if user is not None:
                if user.is_active:
                    return HttpResponseRedirect('/')

    else:
        form = UserForm(None)

    args['form'] = form

    return render(request, template_name, args)


def buscar(request):
    Document.objects.all().delete()
    if request.POST:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            data = form.cleaned_data
            largo= len(Clasificar.objects.all())
            Lista_Textos=[]
            Lista_Categorias=[]
            for i in range(0,largo):
                arreglo1= repr(Clasificar.objects.all()[i]).split("----aquisecortaeltexto----")
                Lista_Textos.append(arreglo1[0])
                Lista_Categorias.append(arreglo1[1])
            tc = TextClassifier(texts=Lista_Textos,ids=map(str, range(largo)))
            tc.make_classifier(name="clasificador_categoria",ids=map(str, range(largo)),labels=Lista_Categorias)
            nombre_total= data['nombre'].replace(" ","+")
            soup_busqueda = BeautifulSoup(urlopen(
                "http://www.fisicanet.com.ar/buscador/fis_buscador.php?criterio=" + nombre_total + "&Buscar=Buscar&registros=1000&como=todas"),
                                          'html.parser')

            lista_links = []
            # obtenemos la informacion para obtener los links de las busquedas
            busqueda = soup_busqueda.find_all("div", class_="brBot1")
            for i in busqueda:
                for j in i.find_all('a'):
                    lista_links.append(j['href'])
                    # se agregan en una lista los url de las paginas de la busqueda hecha
            contador = 1
            # for en el que va entrando pagina por pagina extraendo imagenes y texto
            for links in lista_links:
                if contador > 10:
                    break
                # se busca la informacion en relacion a la pagina
                sopa_de_cada_busqueda = BeautifulSoup(urlopen(links), 'html.parser')
                # extraemos el texto sobre la materia
                texto1 = sopa_de_cada_busqueda.find(itemprop="articleBody").get_text()


                imagenes = sopa_de_cada_busqueda.find(itemprop="articleBody").find_all("img")
                urlimagenes = []
                # entra al for para extraer las imaagenes
                for imagen in imagenes:
                    # se crea el link que nos llevara a la imagen en el buscador web
                    link = urljoin(links, imagen['src'])
                    urlimagenes.append(link)
                    if "img/" in link:
                        break
                labels_considerados, puntajes = tc.classify(classifier_name='clasificador_categoria', examples=[texto1])
                categoria_lista=sorted(zip(puntajes[0], labels_considerados), reverse=True)
                agregar = Document(texto=texto1, numero=contador,categoria=categoria_lista[0][1][:-1])
                agregar.save()
                contador = contador + 1
            return HttpResponseRedirect('/resultado')
    else:
        form = CategoriaForm()

    args = {}

    args['form'] = form
    return render(request, 'buscar_articulo.html', args)

def resultado(request):
    all_documentos = Document.objects.all()
    return render(request, 'resultado.html', {'all_documentos': all_documentos})

def clasificador(request):
    if request.GET:
        if 'texto' in request.GET:
            Agregar=Clasificar(texto=request.GET['texto'],categoria=request.GET['gender'])
            Agregar.save()
    return render(request, 'clasificador.html', request.GET)

def homepage(request):
    return render(request, 'homepage.html',None)