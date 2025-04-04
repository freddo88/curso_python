numeros = [2, 4, 1, 45, 7, 22, 34]


numeros2 = sorted(numeros)  # ordena la lista pero en una nueva lista.
print(numeros2)

numeros.sort()  # ordena la lista de forma ascendente
print(numeros)

numeros.sort(reverse=True)  # ordena la lista de forma desendente
print(numeros)

usuarios = [["lucas", 4], ["Pedro", 5], ["Martin", 1]]

# funcion lambda que ordena la lista por el dato key
usuarios.sort(key=lambda el: el[1])
print(usuarios)
