# le  ponemos una valor cuando queremos que tenga un valor por defecto
def hola(nombre, apellido="Feliz"):
    print("Hola Mundo!")
    print("Ultimate Python")
    print(f"Bienvenido {nombre} {apellido}")


n = input("Ingrese su nombre: ")
hola(n)
hola(apellido="solis", nombre="Fred")  # argumentos nombrados
