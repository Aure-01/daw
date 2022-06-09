import xlrd

ruta = "/Users/omar_/Desktop/daw/daw/sml/xlsx/" 

documento = xlrd.open_workbook(ruta+'archivo.xlsx')

datos = documento.sheet_by_index(0)

for i in range(datos.nrows):
    if i>=1:
        print(f"ID={repr(datos.cell_values(i, 0))} | Nombre: {repr(datos.cell_values(i, 1))} | Apellido: {repr(datos.cell_values(i, 3))}")