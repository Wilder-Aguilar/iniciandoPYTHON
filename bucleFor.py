for s in ['Me', 'gusta', 'Python!']:
    print(s, end=" ")

a=0
for x in [1,2,3,4,5]:
    a += x
print (a)

for c in 'Me gusta Python!':
    print (c, end=" ")


keys = ['nombre', 'apellidos', 'edad']
values = ['Juan', 'Perez', 30]

d = dict(zip(keys, values))

for k in d:
    info = '{}:{}'.format(k,d[k])
    print(info)


a, b = (3,4)
print (a, b)

t=[(1,2),(3,4),(5,6)]
for x, y in t:
    print (x+y, end=" ")

a = [10,20,30,40]
b = [5,25,50,10]
for a,b in zip(a,b):
    m=max(a,b)
    print (m, end=" ")

keys = ['nombre', 'apellidos', 'edad']
values = ['Juan', 'Perez', 30]

d = dict(zip(keys, values))

for k,v in d.items():
    print('{}:{}'.format(k,v))