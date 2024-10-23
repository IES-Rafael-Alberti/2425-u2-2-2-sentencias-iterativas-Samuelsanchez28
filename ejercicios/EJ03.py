# número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# números impares
resultado = ""

# Recorrer los números desde 1 
for i in range(1, numero + 1):
    if i % 2 != 0:  
# Verificar si el número es impar
# Agregar el número impar a la cadena, seguido de una coma
        resultado += str(i) + ", "

# Eliminar la última coma y espacio sobrante
if resultado:
    resultado = resultado[:-2]

# Mostrar los números impares separados por comas
print(resultado)
