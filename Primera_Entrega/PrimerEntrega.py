class Nodo:
    def __init__(self, nombre, piso, tipo):
        self.data = {
            "nombre": nombre,
            "piso": piso,
            "tipo": tipo
        }
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None
    
    def AgregarElemento(self, nombre, piso, tipo):
        nuevoNodo = Nodo(nombre, piso, tipo)
        if self.cabeza == None:
            self.cabeza = nuevoNodo
        else:
            nuevoNodo.siguiente = self.cabeza
            self.cabeza = nuevoNodo


    def verificacion_de_contenido(self):
        if self.cabeza == None:
            print("La lista está vacía")
        else: 
            print("La lista NO está vacía")

    def cantidad_elementos(self):
        cantidad = 0
        nodoActual = self.cabeza
        while nodoActual != None:
            cantidad+=1
            nodoActual = nodoActual.siguiente
        return cantidad

    def imprimirLista(self):
        if self.cabeza == None:
            print("No se puede imprimir nada porque la lista está vacía")
        else: 
            nodoActual = self.cabeza
            while nodoActual != None:
                lugar = nodoActual.data
                print(f"Lugar: {lugar['nombre']} | Piso: {lugar['piso']} | Tipo: {lugar['tipo']}")
                nodoActual = nodoActual.siguiente

    def odenamiento(self):
        if self.cabeza == None:
            return
        temp = True 
        while temp:
            temp = False
            nodoActual = self.cabeza
            while nodoActual.siguiente:
                if (nodoActual.data["nombre"]) > (nodoActual.siguiente.data["nombre"]):
                    nodoActual.data, nodoActual.siguiente.data  = nodoActual.siguiente.data, nodoActual.data
                    temp = True
                nodoActual = nodoActual.siguiente 
    
    def busqueda(self, valor):
        self.odenamiento()
        nodoActual = self.cabeza
        posicion = 0
        while nodoActual:
            if nodoActual.data["nombre"] == valor:
                return f"El lugar '{valor}' se encontró en la posición {posicion}"
            nodoActual = nodoActual.siguiente
            posicion +=1
        return f"El lugar '{valor}' NO se encontró en la lista"

    def eliminar(self, valor):
        if self.cabeza is None:
            return f"La lista está vacía, no se puede eliminar '{valor}'"

        #El nodo a elminar esta en la cabeza
        if self.cabeza.data["nombre"] == valor:
            self.cabeza = self.cabeza.siguiente
            return f"Se eliminó el lugar '{valor}'"

        # Recorrer para encontrar el nodo
        nodoActual = self.cabeza
        while nodoActual.siguiente:
            if nodoActual.siguiente.data["nombre"] == valor:
                nodoActual.siguiente = nodoActual.siguiente.siguiente
                return f"Se eliminó el lugar '{valor}'"
            nodoActual = nodoActual.siguiente

        return f"El lugar '{valor}' NO existe en la lista"
    
#=====================================
#ejemplo

lista = Lista()
lista.AgregarElemento("D1", 2, "Tienda")
lista.AgregarElemento("Pasillo_P2", 2, "Pasillo")
lista.AgregarElemento("Escalera_Norte", 1, "Escalera")
lista.AgregarElemento("Nike", 1, "Tienda")
lista.AgregarElemento("Ascensor_Central", 3, "Ascensor")

lista.verificacion_de_contenido()
print("\nCantidad de lugares en la lista:", lista.cantidad_elementos())

print("\nLista de lugares en el centro comercial:")
lista.imprimirLista()

lista.eliminar("Nike")
print("\nEliminando tienda Nike:")
lista.imprimirLista()
lista.odenamiento()

print("\nBúsqueda de lugares:")
print(lista.busqueda("Escalera_Norte"))
print(lista.busqueda("Adidas"))


