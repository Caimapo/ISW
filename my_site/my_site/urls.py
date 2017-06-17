"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ktapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login
import os

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login, {'template_name' : 'index.html'}, name='login'),
    url(r'^buscar/$', views.buscar, name='buscar'),
    url(r'^resultado/$', views.resultado, name='resultado'),
    url(r'^registrar/$', views.UserFormView, name='UserFormView'),
    url(r'^clasificador/$', views.clasificador, name='clasificador'),
    url(r'^homepage/$', views.homepage, name='homepage'),

]

urlpatterns += staticfiles_urlpatterns()