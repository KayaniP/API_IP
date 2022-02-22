from django.urls import path
from .views import index, retorna_resultado

urlpatterns = [
    path('', index, name = 'index'),
    path('historico/', retorna_resultado, name = 'retorna_resultado'),
]