from random import choice

errores = []
aciertos = []
def pedir_letra():
    letra = "2"
    es_valido = False
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    while letra not in abecedario:
        letra = input("Elije una letra: ")
        if len(letra)==1:
            es_valido=True
        else:
            print("no has elegido bien")

    return letra

def palabra_secreta():
    palabras = ["holaa","adiios","saludos","mmeta"]
    return choice(palabras).lower()

def mostrar_tablero(palabra):
    lista_oculta = []
    for l in palabra:
        if l in aciertos:
            lista_oculta.append(l)
        elif l in aciertos and l in lista_oculta:
            print("Elige otra letra")
        else:
            lista_oculta.append("-")
    print(" ".join(lista_oculta))
def ahorcado():
    palabra = palabra_secreta()
    vidas = 6
    cantidad_letras = 0
    while vidas >0:
        mostrar_tablero(palabra)
        letra = pedir_letra()
        if letra in palabra:
            if letra not in aciertos:
                aciertos.append(letra)
                cantidad_letras = cantidad_letras + palabra.count(letra)
            else:
                pass
            print(aciertos,errores)
            print(f"Te quedan {vidas} vidas")
            print(cantidad_letras)
        else:
            vidas = vidas -1
            errores.append(letra)
            print(aciertos)
            print(errores)
            print(f"Te quedan {vidas} vidas")
        if cantidad_letras == (len(palabra)):
            print("Felicidades, has ganado!!!")
            break

    if vidas == 0:
        return print(f"Lo lamento, has perdido. La palabra era {palabra}")

ahorcado()