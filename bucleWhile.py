c=0
while c<10:
    print (c, end=" ")
    c += 1
print (c)
print ("Ya estamos fuera del while")

a = 5
while a:
    print(a, end=" ")
    a -= 1
print("\nFuera del Bucle")
print('Valor de "a": {}'.format(a))

#CONTINUE
a=7
while bool (a):
    a-=1
    if a%2 == 0:
        continue
    print (a, end=" ")
print ('\nFuera del bucle')

#PASS
a=5
while a:
    pass

a=13
b= a//2

while b > 1:
    if a % b == 0:
        print ('{b} es factor de'.format(b,a))
        break
    b -= 1
else:
    print ('{}es primo'.format(a))
print ('\nFuera del bucle')