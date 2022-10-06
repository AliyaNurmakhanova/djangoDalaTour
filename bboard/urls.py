from django.urls import path, re_path
from bboard import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('bao/', views.bao, name='bao'),
    path('charyn/', views.charyn, name='charyn'),
    path('kolsay/', views.kolsay, name='kolsay'),
    path('chymbulak/', views.chymbulak, name='chymbulak'),
    path('borovoe/', views.borovoe, name='borovoe'),
    path('altay/', views.altay, name='altay'),
]