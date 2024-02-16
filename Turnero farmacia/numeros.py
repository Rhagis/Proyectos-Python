def numeros_cosmeticos():
    x = 0
    while True:
        x += 1
        yield "C-" + str(x)


def numeros_farmacia():
    x = 0
    while True:
        x += 1
        yield "F-" + str(x)


def numeros_perfumeria():
    x = 0
    while True:
        x += 1
        yield "P-" + str(x)


def informacion_ticket(funcion):


    def ticket():
        print("Su turno es: ")
        print(next(funcion))
        print("Aguarde y sera atendido")
    return ticket




