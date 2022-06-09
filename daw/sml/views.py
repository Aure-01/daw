from django.shortcuts import render
from django.http import HttpResponse
import xml.etree.cElementTree as ET

def vistazo(request):
    template_to_return = 'xml.html'
    mi_lista_nombres = 'Juan ''Pedro ''Laura ''Carmen ''Susana'
    mi_lista_apellidos = 'Gonzalez ''Martinez ''Gomez ''Peralta ''Ahumada '
    mi_lista_sexo = 'Masculino ''Femenino ''Otros '
    mi_lista_mascota = 'Gato ''Perro ''Perico ''Tortuga ''Peces ''Tiburon '
    mi_lista_correos = 'omaraurelio1@gmail.com ''omar_aurelio@hotmail.com '

    ruta = "/Users/omar_/Desktop/daw/daw/sml/xml/" 
    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")
    ET.SubElement(doc,"nodo1", mi_lista_nombres = 'mi_lista_nombres').text= mi_lista_nombres
    ET.SubElement(doc,"nodo2", mi_lista_apellidos = 'mi_lista_apellidos').text=  mi_lista_apellidos
    ET.SubElement(doc,"nodo3", mi_lista_sexo = 'mi_lista_sexo').text= mi_lista_sexo
    ET.SubElement(doc,"nodo4", mi_lista_mascota = ' mi_lista_mascota').text= mi_lista_mascota
    ET.SubElement(doc,"nodo5", mi_lista_correos = 'mi_lista_correos').text= mi_lista_correos
    archivo = ET.ElementTree(root)
    archivo.write(ruta+ "ejemplo.xml")
    
    context = {
        'mi_lista_nombres': mi_lista_nombres,
        'mi_lista_apellidos': mi_lista_apellidos,
        'mi_lista_sexo': mi_lista_sexo,
        'mi_lista_mascota': mi_lista_mascota,
        'mi_lista_correos': mi_lista_correos
    }
    return render (request, template_to_return, context)

