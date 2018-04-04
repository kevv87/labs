import time  # Modulo necesario para tomar el tiempo

llamadas = 0  # Contador para llamadas recursivas


# E: Un numero n.
# S: La n posicion en la sucesion de fibonacci.
# R: N debe ser entero positivo
def fib(n):
    if isinstance(n, int):
        return fib_aux(n, 0, 1)
    else:
        return "Error"


def fib_aux(n, a,  b):
    global llamadas
    llamadas = llamadas + 1
    if n == 0:  # Caso base 1
        return a
    elif n == 1:  # Caso base 2
        return b
    return fib_aux(n-1, b, a+b)


start = time.clock()  # Iniciando el cronometro
print("Resultado: "+str(fib(35)))
end = time.clock()  # Deteniendo el cronometro

print("Llamadas recursivas: "+str(llamadas))
print("Tiempo de ejecucion: "+str(end-start)+" segundos")
