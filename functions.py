def agregar_contacto(contactos):
    while True:
        nombre = input("Ingrese nombre del contacto (mínimo 3 letras): ").strip().lower()
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
