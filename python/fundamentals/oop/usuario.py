class Usuario:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.balance = saldo_inicial

    def hacer_retiro(self, amount):
        if amount > self.balance :
            print("Error: no hay suficiente saldo en la cuenta")
        else:
            self.balance -= amount
            print("Retiro exitoso. Saldo restante:", self.balance)

    def mostrar_balance(self):
        print("tu saldo es :", self.balance)

    def hacer_deposito(self, amount):
        self.balance += amount
        print("Depósito exitoso hacia. Saldo actual:", self.balance)     

    def tranferencia(self, amount,user):
        
        if amount > self.balance :
            print("Error: no hay suficiente saldo en la cuenta")
        else:
            self.balance -= amount
            user.balance += amount
            print("Tu transferencia hacia",user.nombre,"fue exitosa. Tu saldo es :", self.balance)


manuel = Usuario("Manuel", 10000)
maxi = Usuario("maxi", 10000)
luis = Usuario("salvi", 10000)


manuel.mostrar_balance()
maxi.hacer_deposito(100)
maxi.hacer_deposito(100)
maxi.hacer_deposito(100)
maxi.hacer_retiro(400)
maxi.mostrar_balance()
manuel.hacer_deposito(100)
manuel.hacer_deposito(100)
manuel.hacer_retiro(400)
manuel.hacer_retiro(180)
manuel.mostrar_balance()
salvi.hacer_deposito(300)
salvi.hacer_retiro(100)
salvi.hacer_retiro(100)
salvi.mostrar_balance()
manuel.tranferencia(100, salvi)
manuel.mostrar_balance()
manuel.mostrar_balance()
