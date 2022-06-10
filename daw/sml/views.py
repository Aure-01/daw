from django.shortcuts import render
import xml.etree.cElementTree as ET

def creacion(request): 
    Nombre = request.POST['name']
    nacionalidad=  request.POST['Nacionalidad']
    Edad=  request.POST['edad']
    Direccion=  request.POST['direccion']
    Telefono=  request.POST['telefono']

    if name == '':
        else if Nacionalidad == '':
            else if edad == '':
                else if direccion == '':
                    else if telefono == '':
                    ruta = "/Users/omar_/Desktop/daw/daw/sml/xml/" 
                    root = ET.Element("root")
                    doc = ET.SubElement(root, "doc")

                    nodo1 = ET.SubElement(doc, "nodo1", name="datos generales")
                    nodo1.text = "Datos de la persona"

                    ET.SubElement(doc, "nodo1", atributo="name").text = Nombre
                    ET.SubElement(doc, "nodo1", atributo="Nacionalidad").text = nacionalidad
                    ET.SubElement(doc, "nodo1", atributo="edad").text = Edad
                    ET.SubElement(doc, "nodo1", atributo="direccion").text = Direccion
                    ET.SubElement(doc, "nodo1", atributo="telefono").text = Telefono
                    
                    arbol = ET.ElementTree(root)
                    arbol.write(ruta+ "prueba.xml")
                    print('Nombre')
        
    return render (request, 'xml.html')

def lectura(request):
    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")
    ET.SubElement(doc, "nodo1", atributo="name").text = nombres
    ET.SubElement(doc, "nodo1", atributo="Nacionalidad").text = Nacionalidades
    ET.SubElement(doc, "nodo1", atributo="edad").text = edades
    ET.SubElement(doc, "nodo1", atributo="direccion").text = direcciones
    ET.SubElement(doc, "nodo1", atributo="telefono").text = telefonos
   
    context={
        'nombres' : nombres,
        'Nacionalidades' : Nacionalidades,
        'edades' : edades,
        'direcciones' : direcciones,
        'telefonos' : telefonos,
    }

    return render(request, 'xml.html', context)