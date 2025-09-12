class Nodo:

    def __init__(self, data):
        self.data= data
        self.siguiente= None

class Lista:

    def __init__(self):
        self.cabeza = None

    def verificacion_de_contendido(self):
        if self.cabeza == None:
            print("La lista está vacia")
        else: 
            print("La lista NO está vacia")

    def cantidad_elementos(self):
        cantidad = 0
        if(nodoActual):
            nodoActual = self.cabeza
            while nodoActual != None:
                cantidad+=1
                nodoActual = nodoActual.siguiente
            return cantidad
        else: return 0

    def imprimirLista(self):
        if self.cabeza == None:
            print("No se puede imprimir nada porque la lista está vacia")
        else: 
            nodoActual = self.cabeza
            for i in range(self.cantidad_elementos()):
                print(nodoActual.data)
                nodoActual = nodoActual.siguiente
            
    def AgregarElemento(self,data):
        nuevoNodo = Nodo(data)
        if self.cabeza == None:
            self.cabeza = nuevoNodo
        else:
            nuevoNodo.siguiente = self.cabeza
            self.cabeza = nuevoNodo

    def odenamiento(self):
        if self.cabeza == None:
            return
        temp = True 
        while temp:
            temp = False
            nodoActual = self.cabeza
            while nodoActual.siguiente:
                if (nodoActual.data) > (nodoActual.siguiente.data):
                    nodoActual.data,nodoActual.siguiente.data  = nodoActual.siguiente.dato, nodoActual.data
                    temp = True
                nodoActual = nodoActual.siguiente 
    
    def busqueda(self, valor):
        self.odenamiento()
        nodoActual = self.cabeza
        posicion = 0
        while nodoActual:
            if nodoActual ==  valor:
                return f"el valor  {valor} se encontró en la posición {posicion}"
            else:print(f"no se encontró el {valor} en la Lista")    
            nodoActual = nodoActual.siguiente
            posicion +=1

