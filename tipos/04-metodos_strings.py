animal = " chanchito feliz "
print(animal.upper())  # metodo  que convierte todo en mayusculas
print(animal.lower())  # metodo que convierte to a  minuscula
print(animal.capitalize())  # metodo que convierte la primera letra a mayuscula
# metodo que convierte la primera letra de cada palabra a mayuscula
print(animal.title())
# elimina espacios en blanco al inicio y al final del string
print(animal.strip())
# podemos encadenar estos metodos
print(animal.strip().capitalize())
print(animal.rstrip())  # elimina espacios solo a la derecha
print(animal.lstrip())  # elimina espacios ¿solo ala izquierda
print(animal.find("ch"))  # devuelve el indice de la cadena que le pasamos
print(animal.replace("ch", "j"))  # remplaza la cadena por un nuevo argumento
print("ch" in animal)  # nos devuelve true o false si ch esta en la cadena
