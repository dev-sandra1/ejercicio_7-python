
#Generador de Contraseñas Aleatorias


import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Ingresa la longitud de la contraseña: "))
password = generate_password(length)

print(f'Tu contraseña aleatoria es: {password}')
