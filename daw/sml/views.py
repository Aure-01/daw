from django.shortcuts import render
import array as arr
import xml.etree.cElementTree as ET

def sml_vew(request):
    var1=2312345698710203604
    var2='hola'
    a=[2,4,3,2,1,2,3,4,5,5,4]
    #print(a)
    context={
        'varl': var1,
        'var2': var2,
        'a': a,
    }
    return render(request,'sml.html',context)

def creacion(request): 
    nombre = request.POST['nombre']
    nacionalidad=  request.POST['Nacionalidad']
    edad=  request.POST['edad']
    direccion=  request.POST['direccion']
    telefono=  request.POST['telefono']

    ruta = "/Users/omar_/Desktop/daw/daw/sml/xml/" 
    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")

    nodo1 = ET.SubElement(doc, "nodo1", name="datos generales")
    nodo1.text = "Datos de la persona"

    ET.SubElement(doc, "nodo1", atributo="Nombre").text = nombre
    ET.SubElement(doc, "nodo1", atributo="nacionalidad").text = nacionalidad
    ET.SubElement(doc, "nodo1", atributo="edad").text = edad
    ET.SubElement(doc, "nodo1", atributo="direccion").text = direccion
    ET.SubElement(doc, "nodo1", atributo="telefono").text = telefono
                    
    arbol = ET.ElementTree(root)
    arbol.write(ruta+ "prueba.xml")
        
    return render (request, 'sml.html')

def lectura(request):
    ruta = "/Users/omar_/Desktop/daw/daw/sml/xml/" 
    doc = ET.parse(ruta + "prueba.xml")
    raiz = doc.getroot()
    print(raiz)
    
    nombre=(raiz[0][1].text)
    nacionalidad=(raiz[0][2].text)
    edad=(raiz[0][3].text)
    direccion=(raiz[0][4].text)
    telefono=(raiz[0][5].text)
    print(nombre,nacionalidad,edad,direccion,telefono)
    context={
        'nombre' : nombre,
        'nacionalidad' : nacionalidad,
        'edad' : edad,
        'direccion' : direccion,
        'telefono' : telefono,
    }

    return render(request, 'sml.html', context)