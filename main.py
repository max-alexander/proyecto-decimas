from functions import *
import os, time
os.system("cls")

contactos=[]
while True:
    print("1.	Agregar un contacto: nombre, teléfono, email.")
    print("2.      Listar contactos: mostrar todos los contactos guardados.")
    print("3.	Buscar un contacto por nombre.")
    print("4.	Eliminar un contacto.")
    print("5.	Salir del programa.")
    try:
        opcion = int(input("ingrese la opcion que necesita\n"))
    except:
        print
    
