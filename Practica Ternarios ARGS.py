'''Calcular el mayor de dos números ingresados por teclado usando un operador
ternario'''

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))

mayor = num1 if num1 > num2 else num2

print(f' El número mayor es: {mayor}')

print()

'''Buscar una palabra en una lista ingresada por teclado usando args y un operador
ternario'''

def buscar_palabra(palabra_buscada, *args):

    resultado = 'Encontrada' if palabra_buscada in args else 'No encontrada'
    return resultado


lista = input('Ingrese palabras separadas por espacio: ').split()
palabra = input('Ingrese la palabra a buscar: ')


print(buscar_palabra(palabra, *lista))

print()

'''Determinar si un número es par o impar'''


num = int(input('Ingrese un número entero: '))

resultado = ' Par' if num % 2 == 0 else 'Impar'
print(f'El número {num} es {resultado}.')

print()

''' Calcular el promedio de una lista de números usando args y un operador ternario'''

def calcular_promedio(*args):

    promedio = sum(args) / len(args) if len(args) > 0 else 0
    return promedio


numeros = input('Ingrese números separados por espacio: ').split()
numeros = [float(n) for n in numeros]

print(f'El promedio es: {calcular_promedio(*numeros):.2f}')

print()

''' Imprimir un mensaje de error si no se pasan suficientes argumentos '''

def procesar_datos(*args):

    mensaje = 'Datos procesados correctamente.' if len(args) >= 3 else 'Error: se requieren al menos 3 argumentos.'
    print(mensaje)

procesar_datos(1, 20)
procesar_datos(6, 10, 65)