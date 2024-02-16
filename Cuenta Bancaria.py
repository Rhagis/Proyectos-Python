class Persona:

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        Persona.__init__(self,nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"El cliente {self.apellido} {self.nombre} es dueño de la cuenta {self.numero_cuenta} y posee un balance de ${self.balance}"

    def depositar(self):
        deposito = int(input("Cuanto dinero quieres ingresar: "))
        self.balance = self.balance + deposito
        return self.balance

    def retirar(self):
        retiro = int(input("Cuanto dinero quieres retirar: "))
        if self.balance >= retiro:
            self.balance = self.balance - retiro
        else:
            print("No tienes suficiente saldo")
        return self.balance




def crear_cliente():
    nombre = input("Dime tu nombre: ")
    apellido = input("Dime tu apellido: ")
    numero_cuenta = int(input("Dime tu numero de cuenta: "))
    balance = input("Dime tu balance: ")
    cliente = Cliente(nombre,apellido,numero_cuenta,balance)
    return cliente

def cuenta_bancaria():
    cliente = crear_cliente()
    finalizar = False

    while not finalizar:
        print(f"""Bienvenido Sr. {cliente.apellido} al administrador de su cuenta bancaria.
                Su menu es el siguiente:
                [1] - Ver estado
                [2] - Depositar dinero
                [3] - Retirar dinero
                [4] - Finalizar programa
                
                Que opcion desea elegir: """)
        opcion = input()
        if opcion == "1":
            print(cliente)

        elif opcion == "2":
            cliente.depositar()

        elif opcion == "3":
            cliente.retirar()

        elif opcion == "4":
            finalizar = True

        else:
            print(("no has elegido la opcion correcta"))




cuenta_bancaria()