# Módulo. Nos devuelve el resto de una división:
n_numerador = 85
n_denominador = 9
n_resto = n_numerador%n_denominador
print("El resto de dividir" , n_numerador
, "entre" , n_denominador , "es" ,
n_resto)
# == Igual que...
# No confundir con el operador de asignación =
# Con = le damos un valor a una variable. Con == comprobamos si dos objetos son iguales.
n_numero1 = 34
s_texto1 = "34"
n_numero1 == s_texto1
n_numero2 = 34
n_numero3 = 34
n_numero2 == n_numero3
# != Diferente que...
n_numero4 = 34
n_numero5 = 34
n_numero4 != n_numero5
# += Suma e incremento
n_numero6 = 34
n_numero6 += 1 #Sería como poner:
n_numero6 = n_numero6 +1
print(n_numero6)

#OPERADORES LOGICOS
a= True
b = False
resultado = a and b
# print(resultado)
resultado = a or b
# print(resultado)
resultado = not a
print(resultado)
#----------------------------------
# Sintaxis simplificada para varios operadores lógicos
edad = int(input('Introduce tu edad: '))
veintes = edad >= 20 and edad < 30
print(veintes)
treintas = edad >= 30 and edad <40
print(treintas)
if ( 20 <= edad < 30) or (30 <= edad<40):
    print('Dentro de rango (20\'s) o (30\'s)')
    if veintes:
        print('Dentro de los 20\'s')
    elif treintas:
        print('Dentro de los 30\'s')
    else:
        print('Fuera de rango')
else:
    print("No está dentro de los 20's ni 30's")

#OBJETOS MUTABLES E IMMUTABLES
# Obtener la dirección de memoria de una variable
a = 65
print("La dirección de memoria es" , id(a))
# Obtener la dirección de memoria de una variable que apunta a otra
miNumero = 65
miNumero2 = miNumero
print("La dirección de memoria es" , id(miNumero))
print("La dirección de memoria es" , id(miNumero2))
# Si cambio la variable, realmente creo una copia en otra dirección de memoria:
a = 65
print("La dirección de memoria es" , id(a))
a+=2
print("La dirección de memoria es" , id(a))
# Obtener la dirección de memoria de una tupla
a = (1, 2, 3, 4, 5)
print("La dirección de memoria es" , id(a))
# Obtener la dirección de memoria de una lista
a = [1, 2, 3, 4, 5]
print("La dirección de memoria es" , id(a))
# Obtener la dirección de memoria de un diccionario
a = {'a': 1, 'b': 2}
print(a)
print("La dirección de memoria es" , id(a))
a["c"] = 3
print(a)
print("La dirección de memoria es" , id(a))