usuarios = [["lucas", 4],
            ["Pedro", 5],
            ["Martin", 1]]


# con este for podemos sacar una lista de nombres
# Conocido como map
# nombres = [usuario[0] for usuario in usuarios]
# print(nombres)

# Filtar una lista
# Conocido como filter
# nombres2 = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombres2)

# map
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# filter
nombre2 = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombre2)
