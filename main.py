from functions import *
import os
import time
os.system("cls")

contactos = []
while True:
    print("1.	Agregar un contacto: nombre, teléfono, email.")
    print("2.      Listar contactos: mostrar todos los contactos guardados.")
    print("3.	Buscar un contacto por nombre.")
    print("4.	Eliminar un contacto.")
    print("5.	Salir del programa.")
    try:
        opcion = int(input("ingrese la opcion que necesita\n"))

        if opcion == 1:
            print("1.	Agregar un contacto: nombre, teléfono, email.")
            contactos = agregar_contacto(contactos)
            time.sleep(3)
            os.system("cls")

        elif opcion == 2:
            os.system("cls")
            print("2.   Listar contactos: mostrar todos los contactos guardados.")
            listar_contactos(contactos)
        elif opcion == 3:
            os.system("cls")
            print("3.	Buscar un contacto por nombre.")
            buscar_contacto(contactos)

            
        elif opcion == 4:
            os.system("cls")
            print("4.	Eliminar un contacto.")
            contactos = eliminar_contacto(contactos)
            
            
        elif opcion == 5:
            os.system("cls")
            print("5.	Salir del programa.")
            break
            
        else:
            print("ingrese una opcion dentro de las disponibles 1 al 5")

    except:
        print("Intentalo nuevamente")
