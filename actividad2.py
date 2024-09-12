sexo = str(input("Ingrese su sexo(femenino o masculino): "))
nombre = str(input("Ingrese su nombre: "))
if  sexo  == "femenino" and nombre[0] < "M":
    print("Sos del grupo A")
elif sexo == "masculino" and nombre[0] >"N":
    print("Sos del grupo A")
else:
    print("Sos del grupo B")