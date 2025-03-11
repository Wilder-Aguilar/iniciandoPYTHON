#Escribe un programa que pregunte al usuario su edad y muestre si es mayor de edad
edad = int (input("Ingresa tu edad: "))
if edad > 18:
    print ("Eres mayor de edad")
else:
    print ("Eres menor de edad")

# Solicia dos numeros al usuario y determina cual de los dos es mayor o si son iguales
numero1 = int (input("Ingresa el primer numero: " ))
numero2 = int (input("Ingresa el segundo numero: " ))

if numero1 > numero2:
    print ("El primer numero es mayor")
elif numero1 == numero2:
    print ("Los numeros son iguales")
else:
    print ("El segundo numero es mayor")

# escribe script que solicite una calificaicon al usuario

calificación = int (input("Ingresa la calificacion (0-100): "))
if calificación >= 90:
    print ("Excelente")
elif calificación >= 70:
    print ("Bueno")
elif calificación >= 50:
    print ("Suficiente")
else:
    print ("Insuficiente")

while True:
    try:
        calificación = int(input("Ingresa la calificación (0-100): "))
        if 0 <= calificación <= 100:
            break  # La calificación es válida, salimos del bucle
        else:
            print("Error: La calificación debe estar entre 0 y 100.")
    except ValueError:
        print("Error: Ingresa un número entero válido.")

if calificación >= 90:
    print("Excelente")
elif calificación >= 70:
    print("Bueno")
elif calificación >= 50:
    print("Suficiente")
else:
    print("Insuficiente")

# Un almacen da un descuento de 15% si la compra supera los 100 euros, pedir eltotal de la compra y calcular el descuento si aplica y el total a pagar

total = float (input ("Ingresa el total de la compra: "))

if total > 100:
    descuento = total * 15 / 100
    descuento_redondeado = round (descuento, 2)
    print (f"El descuento es de ${descuento_redondeado} euros")
    totalFinal = total - descuento_redondeado
    totalFinal = round (totalFinal, 2)
    print ("El total final es de " + str(totalFinal) + " euros")
else:
    print ("No hay descuento")
    totalCompra_redondeada = round (total, 2)
    print ("El total de la compra es de " + str(totalCompra_redondeada) + " euros")

# Pida nuemro al usuario del 1 al 7 y muestre el dia de la semana correspondeitne , caso contrario invalido

dia = int ( input("Ingresa un numero: "))

if dia >= 1 and dia <= 7:
    if dia == 1:
        print ("Lunes")
    elif dia == 2:
        print ("Martes")
    elif dia == 3:
        print ("Miércoles")
    elif dia == 4:
        print ("Jueves")
    elif dia == 5:
        print ("Viernes")
    elif dia == 6:
        print ("Sábado")
    elif dia == 7:
        print ("Domingo")
else:
    print ("Error: El dia ingresado no es valido")

# Programam que pida la edad del usuario y clasificar, niños menores de 13, adolescentes de 13 a 19, adulto de 20 a 64 y adulto mayor de 65 0 mas

edad = int(input("Ingresa tu edad: "))
if edad < 13:
    print ("Niño")
else: 
    if edad < 20:
        print ("Adolescente")
    else:
        if edad < 65:
            print ("Adulto")
        else:
            print ("Adulto mayor")


