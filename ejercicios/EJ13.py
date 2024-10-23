# variable de control
seguir = True

# Bucle para mostrar el eco de lo que el usuario introduce
while seguir:
    entrada = input("Introduce algo (escribe 'salir' para terminar): ")
    if entrada.lower() == "salir":  
        seguir = False  
    else:
        print(f"Eco: {entrada}")  

# Mensaje de despedida
print("Saliendo del programa...")
