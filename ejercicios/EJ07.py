# tabla de multiplicar del 1 al 10
for i in range(1, 11):  # Para cada número del 1 al 10
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):  
        
        # Multiplicamos por cada número del 1 al 10
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()  
 
    # una línea en blanco entre tablas
