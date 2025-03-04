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
    print ("El archivo no existe")