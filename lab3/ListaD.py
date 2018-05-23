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
        print('[', end='')
        while nodo != None and nodo != self.head:
            print(nodo.valor, end=', ')
            nodo = nodo.prev
        if nodo != None:
            print(nodo.valor, end='')
        print(']')

    def toList(self):
        nodo = self.head
        listaPy = []
        while nodo!= None:
            listaPy.append(nodo.valor)
            nodo = nodo.next
        return listaPy

    def norm(self):
        nodo = self.head
        nodo.prev = None
        while nodo.next != None:
            nodo.next.prev = nodo
            nodo = nodo.next

    def dele(self, ele):
        nodo = self.head
        cont = 0
        while nodo != None and cont == 0:
            if nodo.valor == ele and nodo == self.head:
                self.head = nodo.next
                self.largo -= 1
                cont += 1
            elif nodo.next.valor == ele and nodo.next == self.tail:
                self.largo -= 1
                self.tail = nodo
                nodo.next = None
                cont += 1
            elif nodo.next.valor == ele:
                nodo.next = nodo.next.next
                cont += 1
            nodo = nodo.next

def prueba():
    lista = ListaDoble()
    empty = ListaDoble()
    for i in range(10):
        lista.appe(i)
    lista.appe(7)
    lista.printL()
    lista.reve()
    lista.printL()
    lista.dele(7)
    lista.dele(0)
    lista.dele(5)
    empty.dele(1)
    print(lista.toList())

prueba()