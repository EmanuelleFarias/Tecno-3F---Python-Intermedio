'''1. Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.'''

try:
    num1 = int(input('Informe el numerador: '))
    num2 = int(input('Informe el denominador: '))

    resultado = num1/num2
    print(f'El resultado de la división es {resultado:.2f}.')
except ZeroDivisionError:
    print('Ha ocurrido un error. No se puede dividir por zero.')


'''2. Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.'''

try:
    num = 10
    texto = 'casa'

    resultado = num + texto
    print(f'El resultado de la soma es {resultado}.')
except TypeError:
    print('Ha ocurrido un error. No se puede sumar un numero y una cadena.')

'''3. Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
un mensaje de error al usuario.'''

diccionario = {"item": "cuaderno", "cantidad": 20}

try:
    print(diccionario["precio"])
except KeyError:
    print('Ha ocurrido un error. La clave informada no existe en el diccionario.')

'''4. Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe.'''

nombre_archivo = 'datos.txt'

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print('Contenido del archivo: ')
        print(contenido)
except FileNotFoundError:
    print(f'Error: El archivo informado no existe.')
    print('Vamos a crear el archivo...')

    with open(nombre_archivo, 'w') as archivo:
        archivo.write('Este es un archivo recién creado.\n')

    print(f"El archivo '{nombre_archivo}' ha sido creado.")