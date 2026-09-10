# Importamos a função index() definida no arquivo views.py
from . import views
from django.urls import path

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET /
    path('', views.index, name='index'),
]
