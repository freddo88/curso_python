nombres = ["Carlos", "Jose", "Juan", "Manuel", "Jose", "Santiago", "Felipe"]

# inserta un elemento en la posicion del indice indicado
nombres.insert(2, "Raul")
print(nombres)

nombres.append("Mario")  # inserta iun elemento al final de la lista
print(nombres)

nombres.remove("Jose")  # eleimina el elemnto indicado
nombres.pop(1)  # Elimina el elemento por su indice
del nombres[0]  # Elimina un elemnto por el indice
