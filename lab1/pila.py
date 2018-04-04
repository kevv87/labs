import time
llamadas = 0  # Contador para llamadas recursivas


# E: Un numero n.
# S: La n posicion en la sucesion de fibonacci.
# R: N debe ser entero positivo
def fib(n):
    if isinstance(n, int) and n >= 0:
        return fib_aux(n)
    else:
        return 'Err'


def fib_aux(n):
    global llamadas
    if n == 0:  # Caso base 1
        return 0
    elif n <= 2:  # Caso base 2
        return 1
    else:  # Llamadas recursivas
        llamadas += 2
        return fib(n-1) + fib(n-2)


start = time.clock()  # Iniciando el cronometro
print("Resultado: "+str(fib(35)))
end = time.clock()  # Parando el cronometro

print("Llamadas recursivas realizadas:"+str(llamadas))
print("Tiempo de ejecucion: "+str(end-start)+" segundos")
