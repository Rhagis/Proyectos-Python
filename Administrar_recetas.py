# Paso 1: importar librerias(cumplido)
from pathlib import Path
import os
from os import listdir, system

directorio = Path("D:/Descargas/Recetas/Recetas")
def contar_recetas(directorio):
    contador = 0
    for txt in directorio.glob("**/*.txt"):
        contador += 1
    return contador

def inicio(directorio):
    print("*" * 49)
    print("*" * 10 + "  Bienvenido a tu recetario  " + "*" *10)
    print("*" * 49)
    print(f"Tus recetas se encuentran en {directorio}")
    print(f"Tienes un total de {contar_recetas(directorio)} recetas")
    opcion_correcta = "x"
    while not opcion_correcta.isnumeric() or int(opcion_correcta) not in range(1,7):
        print("Elige una opcion: ")
        print('''
                [1] - Ver recetas
                [2] - Crear receta
                [3] - Crear categoria
                [4] - Eliminar receta
                [5] - Eliminar categoria
                [6] - Finalizar programa''')
        opcion_correcta = input()
    return int(opcion_correcta)

def mostrar_categoria(directorio):
    print("Tus categorias son:")
    ruta = Path(directorio)
    contador = 1
    lista_categorias = []
    for carpeta in ruta.iterdir():
        print(f"[{contador}] - {carpeta.name}")
        contador += 1
        lista_categorias.append(carpeta)
    return lista_categorias

def elegir_categoria(lista):
    lista_categorias = lista
    opcion_correcta = "x"
    print("Elija una opcion: ")
    while not opcion_correcta.isnumeric() or int(opcion_correcta) not in range(1, len(lista_categorias)+1):
        opcion_correcta = input()
    return lista_categorias[int(opcion_correcta) - 1]


def mostrar_recetas(ruta):
    ruta = Path(ruta)
    lista_recetas = []
    contador = 1
    for txt in ruta.glob("**/*.txt"):
        print(f"[{contador}] - {txt.stem}")
        contador += 1
        lista_recetas.append(txt)
    return lista_recetas


def elegir_receta(lista):
    lista_recetas = lista
    opcion_correcta = "x"
    print("Elige tu receta: ")
    while not opcion_correcta.isnumeric() or int(opcion_correcta) not in range(1, len(lista_recetas)+1):
        opcion_correcta = input()
    return lista_recetas[int(opcion_correcta)-1]

def leer_receta(ruta):
    ruta = Path(ruta)
    print(ruta.read_text())

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe tu nueva receta: ")
        nombre = input() + ".txt"
        print("Escribe el contenido de la receta: ")
        contenido = input()
        ruta_nueva = Path(ruta / nombre)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido)
            print("Creacion exitosa")
            existe = True
        else:
            print("Tu receta ya existe")

def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Elije el nombre de tu categoria: ")
        nombre = input()
        ruta_nueva = Path(ruta / nombre)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print("Creacion exitosa")
            existe = True
        else:
            print("Tu categoria ya existe")


def eliminar_receta(ruta):
    Path.unlink(ruta)

def eliminar_categoria(ruta):
    Path.rmdir(ruta)
    print("Tu categoria fue eliminada con exito.")

def volver_inicio():
    opcion_correcta="X"
    while opcion_correcta.lower() != "v":
        print("presiona V para volver a inicio")
        opcion_correcta = input()



finalizar_programa = False

while not finalizar_programa:
    menu = inicio(directorio)

    if menu == 1:
        mis_categoria = mostrar_categoria(directorio)
        mi_eleccion = elegir_categoria(mis_categoria)
        mis_recetas = mostrar_recetas(mi_eleccion)
        if len(mis_recetas) < 1:
            print("No hay recetas")
        else:
            receta_elegida = elegir_receta(mis_recetas)
            leer_receta(receta_elegida)
        volver_inicio()
    elif menu == 2:
        mis_categoria = mostrar_categoria(directorio)
        mi_eleccion = elegir_categoria(mis_categoria)
        crear_receta(mi_eleccion)
        volver_inicio()

    elif menu == 3:
        crear_categoria(directorio)
        volver_inicio()

    elif menu == 4:
        mis_categoria = mostrar_categoria(directorio)
        mi_eleccion = elegir_categoria(mis_categoria)
        mis_recetas = mostrar_recetas(mi_eleccion)
        if len(mis_recetas) < 1:
            print("No hay recetas")
        else:
            receta_elegida = elegir_receta(mis_recetas)
            leer_receta(receta_elegida)
        volver_inicio()
1

    elif menu == 5:
        mis_categoria = mostrar_categoria(directorio)
        mi_eleccion = elegir_categoria(mis_categoria)
        eliminar_categoria(mi_eleccion)
        volver_inicio()

    elif menu == 6:
        finalizar_programa = True

