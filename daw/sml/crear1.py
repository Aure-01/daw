import xml.etree.cElementTree as ET

ruta = "/Users/omar_/Desktop/daw/daw/sml/xml/" 
root = ET.Element("root")
doc = ET.SubElement(root, "doc")
ET.SubElement(doc,"nodo1", mi_lista_nombres = 'mi_lista_nombres').text= 'Juan ''Pedro ''Laura ''Carmen ''Susana'
ET.SubElement(doc,"nodo2", mi_lista_apellidos = 'mi_lista_apellidos').text= 'Gonzalez ''Martinez ''Gomez ''Peralta ''Ahumada '
ET.SubElement(doc,"nodo3", mi_lista_sexo = 'mi_lista_sexo').text= 'Masculino ''Femenino ''Otros '
ET.SubElement(doc,"nodo4", mi_lista_mascota = ' mi_lista_mascota').text= 'Gato ''Perro ''Perico ''Tortuga ''Peces '
ET.SubElement(doc,"nodo5", mi_lista_correos = 'mi_lista_correos').text= 'omaraurelio1@gmail.com ''omar_aurelio@hotmail.com '
archivo = ET.ElementTree(root)
archivo.write(ruta+ "ejemplo.xml")

