from numeros import *


ticket1 = informacion_ticket(numeros_cosmeticos())
ticket2 = informacion_ticket(numeros_perfumeria())
ticket3 = informacion_ticket(numeros_farmacia())
def bienvenida():
    print("""Bienvenido, por favor elija una opcion:
            [1] - Cosmeticos
            [2] - Perfumeria
            [3] - Farmacia
            [4] - Finalizar""")
    error = False
    while not error:
        opcion = input()
        if opcion == "1":
            ticket1()
        elif opcion == "2":
            ticket2()
        elif opcion == "3":
            ticket3()
        elif opcion == "4":
            error = True
        else:
            print("no has elegido un numero correcto")






bienvenida()
