# cantidad a invertir, el interés anual y el número de años
cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés porcentual anual: "))
años = int(input("Introduce el número de años de la inversión: "))

# capital obtenido cada año
for año in range(1, años + 1):
    cantidad *= 1 + interes / 100  # Calcular el capital tras un año
    print(f"Año {año}: Capital obtenido: {cantidad:.2f}")
