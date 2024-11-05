
 # Conversor de Horas a Minutos

def convertir_a_minutos(horas):
    return horas * 60

horas = float(input("Ingresa la cantidad de horas: "))
minutos = convertir_a_minutos(horas)
print(f"{horas} horas son {minutos} minutos.")
