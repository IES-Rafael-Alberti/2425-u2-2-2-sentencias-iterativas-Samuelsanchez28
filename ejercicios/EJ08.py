# número entero para la altura del triángulo
altura = int(input("Introduce un número entero para la altura del triángulo: "))

# triángulo rectángulo
for i in range(altura):
    # Calcular los números 
    fila = []
    for j in range(i + 1):
        numero = (2 * (i + 1)) - (2 * j) - 1  
        
        # números en orden decreciente
        fila.append(str(numero))
    
    # Unir los números de la fila en una cadena y mostrarla
    print(" ".join(fila))
