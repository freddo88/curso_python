def suma(*numeros):  # para recibir n numeros de parametros convirtiendolo en iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)
