# variable para la suma
sumatoria = 0

# variable de control
numero = None  # Inicialmente no hay número

# Bucle para leer números hasta que el usuario ponga 0
while numero != 0:
    numero = int(input("Introduce un número entero (0 para terminar): "))
    sumatoria += numero  # Sumar el número a la sumatoria

# sumatoria de los números ingresados
print(f"La sumatoria de los números ingresados es: {sumatoria}")
