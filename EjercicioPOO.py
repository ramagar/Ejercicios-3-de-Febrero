# Se debe modificar la clase CuentaBancaria para que sea abstracta , ademaslos metodos extraer y depositar deben volverse abstractos, tambien se debecrear una clase CuentaAhorro que herede de CuentaBancaria y se leagregue un atributo privado de tasa de interes, el cual tendra un valorestablecido de 0.001 y un metodo que nos calcule el interes.
from abc import ABC, abstractmethod
import os

class CuentaBancaria (ABC):
    def __init__(self, nombre_titular:str, dni:int, fecha_nacimiento:str, saldo:float) -> None:
        self.__nombre_titular:str = nombre_titular
        self.__dni:int = dni
        self.__fecha_nacimiento:str = fecha_nacimiento
        self.__saldo:float = saldo
        
    @abstractmethod
    def depositar(self, deposito:float) -> None:
        pass
    
    @abstractmethod
    def extraer(self, extraccion:float) -> None:
        pass
    
    def get_nombre(self) -> str:
        return self.__nombre_titular
    
    def get_dni(self) -> int:
        return self.__dni
    
    def get_fecha_nacimiento(self) -> str:
        return self.__fecha_nacimiento
    
    def set_saldo(self, saldo:float) -> None:
        self.__saldo = saldo
    
    def get_saldo(self) -> float:
        return self.__saldo
    
    def obtener_saldo(self) -> str:
        os.system("cls")
        return f"La cuenta de {self.get_nombre()} - {self.get_fecha_nacimiento()} - {self.get_dni()}\nPosee un saldo de ${self.get_saldo()}\n"
    
class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular: str, dni: int, fecha_nacimiento: str, saldo: float) -> None:
        super().__init__(nombre_titular, dni, fecha_nacimiento, saldo)
        self.__INTERES:float = 0.001
    
    def depositar(self, deposito:float) -> None:
        nuevo_saldo = self.get_saldo() + deposito
        self.set_saldo(nuevo_saldo)
    
    def extraer(self, extraccion: float) -> None:
        nuevo_saldo = self.get_saldo() - extraccion
        self.set_saldo(nuevo_saldo)
        
    def calcular_interes(self) -> float:
        return self.get_saldo() * self.__INTERES
    
    def obtener_interes(self) -> str:
        return f"El interes es de ${self.calcular_interes()}\n\n"
    

cliente = CuentaAhorro("Ramiro Garcia", 39490812, "11/05/1996", 800)

while True:
    os.system('cls')
    print('Eliga una opcion:\n1) Ver Saldo \n2) Depositar \n3) Extraer')
    opcion = input('Ingrese una opcion (1, 2, 3, 4): ')
    try:
        opcion = int(opcion)
        if opcion not in (1, 2, 3, 4):
            print('No se ingreso una opcion valida')
    except ValueError:
        print('No se ingreso un numero valido')
    else:
        if opcion == 1:
            print(cliente.obtener_saldo())
            print(cliente.obtener_interes())
            input('\n\n\nPulsa ENTER para seguir...')
        elif opcion == 2:
            os.system('cls')
            cliente.depositar(float(input('Ingrese el monto a depositar: ')))
            input('\n\n\nDeposito realizado con exito\nPulsa ENTER para seguir...')
        elif opcion == 3:
            os.system('cls')
            cliente.extraer(float(input('Ingrese el monto a extraer: ')))
            input('\n\n\nExtraccion realizada con exito\nPulsa ENTER para seguir...')
        elif opcion == 4:
            os.system('cls')
            print('Se termino la operacion\n\n')
            input('Pulsa ENTER para finalizar...')
            break
    