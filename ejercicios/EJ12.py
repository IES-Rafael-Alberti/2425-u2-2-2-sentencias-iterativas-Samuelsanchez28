# frase
frase = input("Introduce una frase: ")

# letra
letra = input("Introduce una letra: ")

# Verificar que se ha introducido una letra
if len(letra) != 1:
    print("Por favor, introduce solo una letra.")
else:
    # Contar el número de veces que aparece la letra en la frase
    contador = frase.count(letra)
    print(f"La letra '{letra}' aparece {contador} veces en la frase.")
