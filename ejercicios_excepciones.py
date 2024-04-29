while True:
    ejercicio = input('Elegir el ejercicio a ejecutar (1 a 5): ')
    if ejercicio == '1':
        # Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
        while True:
            try:
                numero1 = float(input('Ingrese el primer numero: '))
                numero2 = float(input('Ingrese el primer numero: '))
                break
            except ValueError:
                print('El valor ingresado no es valido, intentar nuevamente')
        try:
            resultado = numero1 / numero2
        except ZeroDivisionError:
            print('El primer numero ingresado no puede ser dividido por cero')
        else:
            print(f'El resultado es {resultado}')
        finally:
            break
    
    if ejercicio == '2':
        #Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
        while True:
            try:
                numero = float(input('Ingrese un numero: '))
                cadena = input('Ingrese una cadena de caracteres: ')
                break
            except ValueError:
                print('El valor ingresado no es valido, intentar nuevamente')
                
        try:
            resultado = numero + cadena
        except TypeError:
            print('No es posible sumar un numero con una cadena de caracteres')
        else:
            print(f'El resultado es {resultado}')
        finally:
            break
    
    if ejercicio == '3':
        #Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
        diccionario = {'nombre': 'Ramiro',
                           'apellido': 'Garcia',
                           'edad': 27
                           }
        resultado = input('Escribe una clave de diccionario: ')
        try:
            print(f'El valor de la clave "{resultado}" es: {diccionario[resultado]}')
        except KeyError:
            print('El valor ingresado no es una clave')
        finally:
            break
    
    if ejercicio == '4':
        #Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepcion FileNotFoundError, captura la excepcion y muestra un mensaje de error al usuario. Sin embargo, tambien intenta crear el archivo si no existe.
        path_archivo = input('Escribir el nombre del archivo a abrir: ')
        try:
            open(path_archivo)
        except FileNotFoundError:
            print('El archivo no se logro encontrar')
        finally:
            break
    
    if ejercicio == '5':
        # Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
        try:
            numero1 = float(input('Escribir el primer numero: '))
            numero2 = float(input('Escribir el segundo numero: '))
            resultado = numero1 / numero2
        except ValueError:
            print('El numero proporcionado no es valido')
        except ZeroDivisionError:
            print('El segundo numero proporcionado es cero, no se puede ejecutar la operacion')
        else:
            print(f'El resultado es de {round(resultado, 2)}')
        finally:
            break