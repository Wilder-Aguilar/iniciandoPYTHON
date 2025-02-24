def suma(a, b):
    return a+b

print (suma(2,3))

def en_pantalla(frase1, frase2):
    print (frase1, frase2)

en_pantalla("Hola", "Mundo")

print (suma(2.7,4.0))
print (suma('Me gusta', 'Python'))

def f1(a):
    print (a)
    b=300
    def f2(x):
        print (x)
    f2('Mundo')
f1('Hola')

#RECURSIVIDAD
def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1

print (factorial(5))

def maxmin(lista):
    return max(lista), min(lista)

lista = [5,4,3,2,1,0,13]
maximo, minimo = maxmin(lista)
print (maximo, minimo, sep=' ')

def log(*args):
  """
  Imprime los argumentos que se le pasan por pantalla en una misma
  línea, con el prefijo 'LOG: '.
  """

  print('LOG:', *args)