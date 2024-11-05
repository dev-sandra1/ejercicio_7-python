
#Conversor de Temperatura (Celsius, Fahrenheit, Kelvin)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

print("Seleccione la conversión:")
print("1: Celsius a Fahrenheit")
print("2: Fahrenheit a Celsius")
print("3: Celsius a Kelvin")
print("4: Kelvin a Celsius")

choice = int(input("Ingrese su elección (1-4): "))
temp = float(input("Ingrese la temperatura: "))

if choice == 1:
    print(f'{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F')
elif choice == 2:
    print(f'{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C')
elif choice == 3:
    print(f'{temp}°C = {celsius_to_kelvin(temp):.2f}K')
elif choice == 4:
    print(f'{temp}K = {kelvin_to_celsius(temp):.2f}°C')
else:
    print("Opción no válida.")
