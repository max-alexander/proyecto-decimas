def agregar_contacto(contactos):
    while True:
        nombre = input(
            "Ingrese nombre del contacto (mínimo 3 letras): ").strip().lower()
        if len(nombre) < 3:
            print(" Nombre muy corto.")
            continue

        telefono = input("Ingrese teléfono (ej: 946252436): ").strip()
        if not telefono.isdigit() or len(telefono) < 9:
            print(" Teléfono inválido.")
            continue

        email = input("Ingrese email (ej: correo@gmail.com): ").strip()
        if "@" not in email or "." not in email:
            print(" Email inválido.")
            continue

        contacto = [nombre, telefono, email]
        contactos.append(contacto)
        print(" Contacto agregado exitosamente.\n")
        return contactos


def listar_contactos(contactos):
    if not contactos:
        print(" No existen contactos guardados.\n")
    else:
        print("\n Lista de contactos:")
        for i, x in enumerate(contactos, start=1):
            print(f"{i}. Nombre: {x[0]}, Teléfono: {x[1]}, Email: {x[2]}")
    print()


def buscar_contacto(contactos):
    nombre_contacto = input(
        "Ingrese el nombre del contacto que desea buscar: ").strip().lower()
    encontrados = [x for x in contactos if x[0].lower() == nombre_contacto]

    if encontrados:
        for x in encontrados:
            print(f" Nombre: {x[0]}, Teléfono: {x[1]}, Email: {x[2]}")
    else:
        print(" Contacto no encontrado.")
    print()
