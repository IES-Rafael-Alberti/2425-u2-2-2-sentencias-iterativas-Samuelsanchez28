# número entero
numero = int(input("Introduce un número entero: "))

# Función si un número es primo
def es_primo(n):
    if n <= 1:
        return False  
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:  
            return False
    return True  

# Comprobar si el número es primo y mostrar el resultado
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
