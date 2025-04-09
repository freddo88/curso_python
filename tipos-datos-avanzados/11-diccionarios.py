# Un diccionario es una estructura de datos que almacena pares clave-valor.
# Es como un diccionario real: buscas una palabra (clave) y obtienes su significado (valor).

usuario = {
    "nombre": "Fred",
    "edad": 35,
    "ciudad": "Bogota"
}

# Las claves (keys) son únicas.
# Los valores (values) pueden ser de cualquier tipo: string, int, lista, otro diccionario, etc.
print(usuario["nombre"])  # Imprime "Fred"

usuario["edad"] = 31  # Modificamos la edad
usuario["profesion"] = "Ingeniero"  # agregamios una nueva clave

del usuario["ciudad"]  # Eliminamos un elemento

for clave, valor in usuario.items():  # Recorremos un diccionario
    print(clave, ":", valor)
