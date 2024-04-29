import statistics, math
# Calcular el mayor de dos números ingresados por teclado usando un operadorternario
def es_mayor(numero1:float, numero2:float) -> None:
    print(numero1 if numero1>numero2 else numero2)
    
# Buscar una palabra en una lista ingresada por teclado usando args y un operadorternario
def buscar_palabra (*args:str) -> None:
    for palabra in args:
        print(f'La palabra {palabra} SI se encuentra en la lista' if palabra in ['banana', 'manzana', 'rojo', 'boca', 'Pedro', '100'] else f'La palabra {palabra} NO se encontra en la lista')

#Determinar si un número es par o impar
def es_par_impar(*args:float|int) -> None:
    for numero in args:
        print(f'El numero {numero} es par' if numero%2 == 0 else f'El numero {numero} es impar')

#Calcular el promedio de una lista de números usando args y un operador ternario
def promediar(*args:float|int) -> None:
    print(statistics.mean(list(args)))


#comprobar1 = es_mayor(float(input('Ingresar el primer numero: ')), float(input('Ingresar el segundo numero: ')))
#comprobar2 = buscar_palabra(input('Escribir palabra a buscar en la lista: '), input('Escribir palabra a buscar en la lista: '))
#comprobar3 = es_par_impar(5,3,100,56)
#comprobar4 = promediar(100,50,88.5,5545545, math.pi)
