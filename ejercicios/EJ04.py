# número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# almacenar la cuenta atrás
resultado = ""

# Recorrer los números desde el número ingresado hasta 0
for i in range(numero, -1, -1):
    # Agregar el número a la cadena, seguido de una coma
    resultado += str(i) + ", "

# Eliminar última coma y espacio sobrante
if resultado:
    resultado = resultado[:-2]

# cuenta atrás
print(resultado)
