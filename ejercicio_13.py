
#Suma de Números en una Lista

def sumar_numeros(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros = input("Ingresa números separados por espacios: ").split()
numeros = [int(num) for num in numeros]  # Convertir a enteros

resultado = sumar_numeros(numeros)
print(f"La suma de los números es: {resultado}")
