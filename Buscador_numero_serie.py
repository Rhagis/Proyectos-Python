import shutil
import os
import time
from datetime import date
import re
from pathlib import Path
import math

ruta = Path("D:\\Python\\pythonProject1\\Proyecto9\\Mi_Gran_Directorio")
mi_patron = r"N\D{3}-\d{5}"
fecha = date.strftime(date.today(),"%d/%m/%y")
lista_ruta = []


for carpeta, subcarpeta, archivo in os.walk(ruta):
    lista_ruta.append(carpeta)
cantidad_archivos = 0


lista_archivos = list(ruta.glob("**/*.txt"))

for txt in lista_archivos:
    ruta1 = Path(txt)
    text = Path.read_text(ruta1)
    if re.search(mi_patron, text):
        cantidad_archivos += 1
    else:
        pass



def buscador_numero_serie(ruta):
    print("-" * 50)
    print(f"Fecha de busqueda: [{fecha}]")
    print("-" * 50)
    print("\n")
    print("Archivo\t\t\t\tNro. Serie")
    lista_archivos = list(ruta.glob("**/*.txt"))
    cantidad_archivos = 0
    inicio = time.time()
    for txt in lista_archivos:
        ruta1 = Path(txt)
        text = Path.read_text(ruta1)
        if re.search(mi_patron, text):
            resultado = re.search(mi_patron,text)
            print(f"{txt.name}\t\t{resultado.group()}")
            cantidad_archivos += 1
        else:
            pass
    final = time.time()
    print("\n")
    print(f"Números encontrados: {cantidad_archivos}")
    print(f"Duración de la busqueda: {math.ceil(final - inicio)} segundos")

buscador_numero_serie(ruta)