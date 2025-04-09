# Un pequeño programa que permite guardar y buscar contactos usando un diccionario.
# Funcionalidades:
# Agregar un contacto (nombre, teléfono)
# Buscar un contacto por nombre
# Mostrar todos los contactos

def mostrar_menu():
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")


def main():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            telefono = input("Número de teléfono: ")
            agenda[nombre] = telefono
            print(f"Contacto {nombre} agregado.")

        elif opcion == "2":
            nombre = input("Nombre del contacto a buscar: ")
            if nombre in agenda:
                print(f"{nombre}: {agenda[nombre]}")
            else:
                print("Contacto no encontrado.")

        elif opcion == "3":
            if agenda:
                print("\n--- Lista de contactos ---")
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("No hay contactos aún.")

        elif opcion == "4":
            print("Saliendo de la agenda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


main()
