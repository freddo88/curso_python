nombre_curso = "Ultimate Python"
descripcion_curso = """
En este curso contemplamos todos 
lo que se necesita saber para encontar
un trabajo en python"""  # para escribir strings de varias lineas
print(nombre_curso, descripcion_curso)
# funcion len devuelve el tamaño de los caracteres
print(len(descripcion_curso))
print(nombre_curso[0])  # indice de la letra que queremos encontrar
print(nombre_curso[0:8])  # cortar una cadene con los indices de donde a donde
# le pasamos el valor incial y el llega hasta el final de la cadena
print(nombre_curso[9:])
print(nombre_curso[:9])  # similar a lo anterior pero inicia desde cero
print(nombre_curso[:])  # devuelde desde el indice inial hasta el final
