
# Trabajo Colaborativo: "Mini Agenda de Contactos"
# Objetivo:
# Desarrollar una pequeña aplicación de consola en Python que funcione como una agenda de contactos. El objetivo es aplicar los conocimientos de programación estructurada (variables, constantes, tipos de datos, estructuras de control, funciones, etc.) y prácticas básicas de trabajo colaborativo con Git y GitHub.
# ________________________________________
# Requisitos del Proyecto
# La aplicación debe permitir al usuario:
# 1.	Agregar un contacto: nombre, teléfono, email.
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.
# ________________________________________
# Organización del Trabajo
# •	El repositorio debe ser creado por uno de los integrantes del grupo y compartido con los otros.
# •	Todos deben clonar el repositorio en su computadora local.
# •	Cada alumno trabajará en una rama propia (ejemplo: rama-juan, rama-maria, rama-carlos).
# •	Cada uno será responsable de una parte del programa:
# o	Alumno 1: Función para agregar y mostrar contactos.
# o	Alumno 2: Función para buscar y eliminar contactos.
# o	Alumno 3: Estructura del menú principal y control de flujo del programa.

import os,sys,time
def contador(x,b,c):

  contador0 = x

  while contador > b:

    for i in range(1,4):

      sys.stdout.write("\r")

      sys.stdout.write(f"\rEn {x} {c}{'.' * i}")

      sys.stdout.flush()

      time.sleep(1)

      contador0 -= 1 

def menu():

  print(" 1. Agregar un contacto")

  print(" 2. Listar contactos")

  print(" 3. Buscar un contacto por nombre.")

  print(" 4. Eliminar un contacto.")

  print(" 5. Salir del programa.")

  while True:

    menu1 = input("\ningrese la ocpion que desee\n")

    return menu1

def add_contacts():
  while True:

    name = input("ingrese el nombre del contacto\n")

    if len(name) < 3:

      os.system("cls")

      print("Nombre no puede ser meno a 3 caracteres.")

    else:
      os.system("cls")
      print("Nombre registrado exitosamente!")

      time.sleep(1)

      return name,number,email
    
    while True:

      number0 = input("Ingresa tu numero de telefono\n")

      number = "+ 56 9 " + number0

      if len(number0) != 9:

        os.system("cls")

        print("El numero no puede contener menos o mas de 9 numeros")

      else:

        os.system("cls")

        print("Numero registrado exitosamente!")

        time.sleep(1)

        return name,number,email
      
      while True:

        email = input("Ingresa tu correo electronico\n")

        if len(email) < 3:

          os.system("cls")

          print("Correo no puede contener menos de 3 letras")

        elif "@" not in email:

          os.system("cls")

          print("Correo no es valido porfavor intente denuevo.")

        else:

          os.system("cls")

          print("Correo registrado exitosamente!\n")

          print(f"Nombre:{name}")

          print(f"Numero:{number}")

          print(f"Correo:{email}")

          contador(x=5,b=0,c="volvera al menu.")

          os.system("pause")
          
          return name,number,email
add_contacts()