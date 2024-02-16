from random import randint
usuario = input("dime tu nombre ")
print(f"Bueno {usuario}, he pensado un numero del 1 al 100, tienes solo ocho intentos para adivinarlo")
numero_pensado = randint(1,101)

intentos = 0
while intentos < 8:
    numero_elegido = input("elije un numero")
    if int(numero_elegido) < 1 or int(numero_elegido) > 100:
        print("tu numero esta fuera de rango")
        intentos = intentos + 1
        if intentos == 8:
            print(f"lo lamento, has perdido. El numero era {numero_pensado}")
    elif int(numero_elegido) < numero_pensado:
        print("tu numero es menor al que he pensado")
        intentos= intentos +1
        if intentos == 8:
            print(f"lo lamento, has perdido. El numero era {numero_pensado}")
    elif int(numero_elegido) > numero_pensado:
        print("tu numero es mayor al que he pensado")
        intentos = intentos + 1
        if intentos == 8:
            print(f"lo lamento, has perdido. El numero era {numero_pensado}")
    else:
        print("has acertado el numero")
        print(intentos)
        break