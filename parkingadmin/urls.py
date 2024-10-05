from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"), 
    path('sobre_nosotros', views.sobreNosotros, name="sobre_nosotros"),
    path('lectura_placa_vehiculo/', views.lectura_placa_vehiculo, name="lectura_placa_vehiculo"),
    path('ingreso_vehiculo/', views.ingreso_vehiculo, name="ingreso_vehiculo"),
    path('egreso_vehiculo/', views.egreso_vehiculo, name="egreso_vehiculo"),
]

#Vehiculos:
""" path('crear_vehiculo/', views.crear_vehiculo , name="crear_vehiculo"),
    path('eliminar_vehiculo/', views.eliminar_vehiculo , name="eliminar_vehiculo"),
    path('modificar_vehiculo/', views.modificar_vehiculo , name="modificar_vehiculo"),
    #Carnets:
    path('crear_carnet/', views.crear_carnet , name="crear_carnet"),
    path('eliminar_carnet/', views.recargar_carnet , name="recargar_carnet"),
    path('modificar_carnet/', views.modificar_carnet , name="modificar_carnet"),
    path('recargar_carnet/', views.recargar_carnet , name="recargar_carnet"),
    #Parqueaderos:
    
    #Conjunto_celdas:
    
    #Celdas:

    #Ingreso:
    path('registrar_ingreso/', views.registrar_ingreso , name="registrar_ingreso"),

    #Egreso:
    path('registrar_egreso/', views.registrar_egreso , name="registrar_egreso"), 

    #Factura:
    path('generar_factura', views.generar_factura, name="generar_factura"), #Aquí se genera factura y se cobra parqueadero al carnet """