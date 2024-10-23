# contraseña en una variable
contraseña_correcta = "contraseña"  # Puedes cambiar "contraseña" por la que desees

# Variable
contraseña_acertada = False

# Bucle para preguntar por la contraseña hasta que sea correcta
while not contraseña_acertada:
    contraseña_introducida = input("Introduce la contraseña: ")
    if contraseña_introducida == contraseña_correcta:
        print("Contraseña correcta. Acceso concedido.")
        contraseña_acertada = True  # Cambiar la variable de control
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
