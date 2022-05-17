from django.urls import path
from django.contrib import admin  
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('contactocl/', views.contactocl, name='contactocl'),
    path('contactomod/<correo_electronico>', views.contactomod, name='contactomod'),
    path('estadistica/', views.estadistica, name='estadistica'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('clientes/', views.clientes, name='clientes'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('registroprov/', views.registroprov, name='registroprov'),
    path('registroprod/', views.registroprod, name='registroprod'),
    path('listadoprod/', views.listadoprod, name='listadoprod'),
    path('catalogoprod/', views.catalogoprod, name='catalogoprod'),
    path('register_user/',views.register_user, name='register_user'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),

]