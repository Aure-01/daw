import pandas as pd
from pandas import ExcelWriter

ruta = "/Users/omar_/Desktop/daw/daw/sml/xlsx/" 

datos = pd.DataFrame({
    'id':[1, 2, 3, 4, 5],
    'nombre':['Pedro', 'Raul', 'Maria', 'Pablo', 'Cesar'],
    'apellido':['Mendez', 'Lopez', 'Tito', 'Hernandez', 'Amador']
})

#Formalizamos las filas
datos = datos[['id', 'nombre', 'apellido']]

writer = ExcelWriter(ruta + 'archivo.xlsx')

datos.to_excel(writer, 'Hoja 1', index=False)

writer.save()