def get_product(**datos):
    print(datos)  # imprimimos todos los datos ingresados
    print(datos["name"])  # Buscamos solo el parametro que necesitamos


get_product(id="pd01", name="Fred", apellido="solis")
