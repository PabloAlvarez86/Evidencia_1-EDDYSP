from collections import namedtuple
from datetime import date
from datetime import datetime
import pandas as pd
#Se importan las librerías correspondientes

ciclo = True
registro_hecho = []
Registro = namedtuple("Registro",("folio_registrado","descripcion","cantidad","precio"))
#Se crea el diccionario vacio

while ciclo:
    print("\n---Bienvenido/a a nuestra tienda---")
    print("Seleccione que opción quiere desplegar")
    print("1.Registrar una venta")
    print("2.Consultar una venta")
    print("3.Consultar una venta a partir de una fecha")
    print("4.Salir")
    menu = int(input())
    #Menú de navegación

    if menu == 1:
        print("\n **Agregar**")
        cant = int(input("¿Cuántas ventas desea registrar? "))
        l = 1
        while (l <= cant):
            folio_registrado = int(input("Registre su folio, cabe aclarar que este debe ser único e irrepetible "))
            descripcion = input("Ingrese una descripción del artículo: ")
            cantidad = int(input("¿Cuántas piezas se van a vender? "))
            precio = int(input("Ingrese el precio: "))
            venta_registrada = Registro(folio_registrado,descripcion, cantidad, precio)
            registro_hecho.append(venta_registrada)
            fecha = date.today()
            precio_iva = (precio * .16)
            print("El precio con IVA incluido es: ", (precio + precio_iva))
            print(fecha)
            break
        #Opción 1

    elif menu == 2:
        print("\n***Consultar venta***")
        folio = int(input("Ingrese el folio el cual quiere buscar: "))
        for r in registro_hecho:
            if (r.folio_registrado == folio_registrado):
                print("Folio: ",r.folio_registrado)
                print("Descripcion: ",r.descripcion)
                print("Cantidad: ",r.cantidad)
                print("Precio: ",(precio + precio_iva))
                print("Fecha y hora del registro: ",fecha)
                break
        else:
            print("No se encontro el folio solicitado")
        #Opción 2

    elif menu == 3:
        print("Ingrese la fecha de las ventas que quiere ver: ")
        fecha_ver = input('Ingrese fecha (aaaa-mm-dd): ')
        df_registro = pd.DataFrame(registro_hecho)
        print(df_registro)
        df_registro.to_csv(r'registro.csv',index=True, header=True)
        #Opción 3

    elif menu == 4:
        print("Gracias por visitarnos, que tenga un bonito día")
        #Opción 4

