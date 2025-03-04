# IF
a = 10
b = 10

if a > b:
    print("A es menor que B")
elif a == b:
    print("A es igual a B")
else:
    print("A es mayor que B")

print ("Ya estamos fuera del if")

# OPERADOR TERNARIO
a=10
b=3

x=(20 if a > b else 30) #20
print (x)

#ejemplo

a = input("Ingrese un numero: ")

type(a)
print (a)


# ¿Cómo saber si un texto se corresponde a un número?

l=list()
texto = input("Introduce un numero entero por teclado: ")
if texto.isnumeric():
    num = int(texto)
    l.append(num)
    print("Nùmero " + str(num) + " añadido a la lista")
else:
    print("No has introducido un número entero")



d={"50862634" : 37 , "43394932" : 32}
texto = input ("Introduce un numero de DNI:")
if texto in d:
    print ("La edad de " + texto + " es " + str(d[texto]))
else:
    edad = input("Documento no encontrado, ingrese la edad:")
    if edad.isnumeric():
        num = int(edad)
        d[texto] = num
        print ("Añadido al diccionario")
print (d)