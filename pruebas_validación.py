
            
# Función para validar entrada numérica positiva
def solicitar_valor_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje).replace(',', '.'))
            if valor <= 0:
                print("Error: El valor no puede ser negativo. Intente nuevamente.")
            else:
                            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

VCDi = solicitar_valor_positivo("Ingrese el valor de VCD con la que desea iniciar cada pasaje: ")
cantPasajes = int(solicitar_valor_positivo("Ingrese la cantidad de pasajes que desea efectuar durante la etapa de expansión: "))
diasxpasaje = int(solicitar_valor_positivo("Ingrese la cantidad de días que desea que tenga cada pasaje: "))

print(VCDi)
print(cantPasajes)
print(diasxpasaje)


