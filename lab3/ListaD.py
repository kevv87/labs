class Nodo:
    def __init__(self, valor):
        self.next = None
        self.prev = None
        self.valor = valor


class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None
        self.largo = 0

    def appe(self, valor):
        nodo = self.head
        if nodo == None:
            nodo = Nodo(valor)
            self.head = nodo
        else:
            while nodo.next != None:
                nodo = nodo.next
            nodo.next = Nodo(valor)
            nodo.next.prev = nodo
            self.tail = nodo.next

    def printL(self):
        nodo = self.head
        print('[', end='')
        while nodo != None and nodo != self.tail:
            print(nodo.valor, end=', ')
            nodo = nodo.next
        if nodo != None:
            print(nodo.valor, end='')
        print(']')

    def reve(self):
        nodo = self.tail
        while nodo != None:
            print('in')
            save = nodo.next
            nodo.next = nodo.prev
            nodo.prev = save
            nodo = nodo.next


def prueba():
    lista = ListaDoble()
    lista.appe(12)
    lista.appe(15)
    lista.appe(13)
    lista.printL()
    lista.reve()
    lista.printL()
    print(lista.tail.prev)

prueba()