from collections import namedtuple
import datetime
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
    print("3.Salir")
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
            fecha_hora = datetime.datetime.now()
            precio_iva = (precio * .16)
            print("El precio con IVA incluido es: ", (precio + precio_iva))
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
                print("Fecha y hora del registro: ",fecha_hora)
                break
        else:
            print("No se encontro el folio solicitado")
        #Opción 2

    elif menu == 3:
        print("Gracias por visitarnos, que tenga un bonito día")
        #Opción 3