import random

def generar(n, i, lista):
    if i == n:
        return lista
    else:
        lista = lista + [random.randint(1, 10000)]
        return generar(n, i+1, lista)


print(generar(100, 0, []))