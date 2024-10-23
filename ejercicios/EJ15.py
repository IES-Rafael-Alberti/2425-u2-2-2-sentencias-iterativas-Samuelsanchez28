# variable para la suma
sumatoria_positivos = 0

# variable de control
numero = None  # Inicialmente no hay número

# Bucle para leer números hasta que el usuario ponga 0
while numero != 0:
    numero = int(input("Introduce un número entero (0 para terminar): "))
    if numero > 0:  
        sumatoria_positivos += numero

# sumatoria de los números positivos ingresados
print(f"La sumatoria de los números positivos ingresados es: {sumatoria_positivos}")
