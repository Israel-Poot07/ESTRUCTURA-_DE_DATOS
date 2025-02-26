import time

# Solución Recursiva
def factorial_recursivo(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    return n * factorial_recursivo(n - 1)  # Llamada recursiva

# Solución Iterativa
def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Medir tiempo de ejecución
def medir_tiempos(n):
    # Medir tiempo recursivo
    inicio_recursivo = time.time()
    resultado_recursivo = factorial_recursivo(n)
    fin_recursivo = time.time()
    
    # Medir tiempo iterativo
    inicio_iterativo = time.time()
    resultado_iterativo = factorial_iterativo(n)
    fin_iterativo = time.time()
    
    # Mostrar resultados
    print(f"Factorial de {n} (Recursivo): {resultado_recursivo}")
    print(f"Tiempo Recursivo: {fin_recursivo - inicio_recursivo:.10f} segundos")
    
    print(f"Factorial de {n} (Iterativo): {resultado_iterativo}")
    print(f"Tiempo Iterativo: {fin_iterativo - inicio_iterativo:.10f} segundos")

# Prueba con un número
n = int(input("Ingresa un número para calcular su factorial: "))
medir_tiempos(n)
