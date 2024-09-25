from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Vehiculo,Ingreso,Egreso
from . import helpers
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

def parkingadmin(request):
    return render(request,'parkingadmin.html')


def ingreso_vehiculo(request):
    #Si ingresan una imagen 
    if request.method == 'POST' and request.FILES['image']:
        #Se obtiene imagen vehiculo desde templates:
        imagen_vehiculo = request.FILES['image']

        #Subir imagen a /media:
        fs = FileSystemStorage(location='media') #Especifíca ubicación
        nombre_imagen_vehiculo = fs.save(imagen_vehiculo.name, imagen_vehiculo) #Guarda imagen y almacena nombre archivo
        url_imagen_vehiculo = fs.url(nombre_imagen_vehiculo) #Obtiene la url del archivo para poder acceder a él


        #Se extrae placa vehiculo con visión artificial:
        resultados_procesamiento = helpers.procesar_placa(ruta_imagen = 'media/'+nombre_imagen_vehiculo, nombre_imagen_vehiculo = imagen_vehiculo.name)
        
        #Se valida si se obtuvo la placa correctamente
        if isinstance(resultados_procesamiento,tuple):#Si se detecto una placa
            placa_vhc_ingreso,url_imagen_recorte_placa = resultados_procesamiento
        else:
            placa_vhc_ingreso = resultados_procesamiento

        #Se valida si dicho vehículo existe:
        try:
            vehiculo = Vehiculo.objects.get(vhc_placa = placa_vhc_ingreso)
            vehiculo_existe = True
        except ObjectDoesNotExist:
            vehiculo_existe = False
        
        #Se crea el ingreso:
        #ingreso = Ingreso(ing_vehiculo_id = vehiculo.vhc_id, ing_placa_vehiculo = vehiculo.vhc_placa, ing_fecha_hora=timezone.now(), ing_imagen_vehiculo = 'imagenes_vehiculos/'+nombre_imagen_vehiculo)
        #ingreso.save()

        #Se renderiza nuevo template con respectivo contexto sobre nuevo ingreso
        context = {"vehiculo_existe":vehiculo_existe,"url_imagen_vehiculo":url_imagen_vehiculo,"url_imagen_recorte_placa":url_imagen_recorte_placa,"placa_vehiculo":placa_vhc_ingreso}
        return render(request,'ingreso_vehiculo.html',context=context)

    #Si no han ingresado imagen
    elif request.method == 'GET':
        return render(request,'ingreso_vehiculo.html')



