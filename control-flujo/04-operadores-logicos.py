# and  or  not
gas = int(
    input("ingere 1 si el auto tiene gas o ingrese 2 si el auto no tiene gas: "))
encendido = int(
    input("ingere 1 si el auto esta encendido o ingrese 2 si no esta encendido: "))
gas = True if gas == 1 else False
encendido = True if encendido == 1 else False

if gas and encendido:
    print("Puede avenzar")

else:
    print("No puede avanzar")
