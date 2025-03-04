import pickle
from pathlib import Path

d= dict ()

file_name = input ("Introduce el nombre del archivo con los datos:")

# Comprobamos que existe
path = Path(file_name)
if path.is_file():
    input_file = open(file_name, "rb")
    d = pickle.load(input_file)
    input_file.close()
else:
    print ("El archivo no existe, creamos diccionario vacio")

document_number = input ("Introduce el numero de documento:")
if document_number in d:
    print ("La edad de " + document_number + " es " + str(d[document_number]))
else:
    age = input("Documento no encontrado, ingrese la edad:")
    if age.isnumeric():
        num = int(age)
        d[document_number] = num
        print ("Añadido al diccionario")

output_file = open(file_name, "wb")
pickle.dump(d, output_file)
output_file.close()