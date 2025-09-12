'''1. Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.'''

try:
    num1 = int(input('Informe el numerador: '))
    num2 = int(input('Informe el denominador: '))

    resultado = num1/num2
    print(f'El resultado de la división es {resultado:.2f}.')
except ZeroDivisionError:
    print('Ha ocurrido un error. No se puede dividir por zero.')