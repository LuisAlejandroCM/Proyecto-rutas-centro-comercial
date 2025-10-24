class Nodo:
    def __init__(self,nombre, piso, tipo):
        self.data = {
            "nombre": nombre,
            "piso": piso,
            "tipo": tipo
        }
        self.derecha = None
        self.izquierda = None 
        self.altura = 1

class AVL:
    def __init__(self):
        self.raiz = None

    def altura(self, Node):
        if Node is None:
            return 0
        else:
            return Node.altura

    
    def _balance(self, Node):
        if Node is None:
            return 0
        else:
            return self.altura(Node.izquierda) - self.altura(Node.derecha)

    def valorMinimoNodo(self, Node):
        if Node is None or Node.izquierda is None:
            return Node
        else:
            return self.valorMinimoNodo(Node.izquierda)
        
    def _rotacionDerecha(self, Node):
        a = Node.izquierda
        b = a.derecha
        a.derecha = Node
        Node.izquierda = b
        Node.altura = 1 + max(self.altura(Node.izquierda), self.altura(Node.derecha))
        a.altura = 1 + max(self.altura(a.izquierda), self.altura(a.derecha))
        return a

    def _rotacionIzquierda(self, Node):
        a = Node.derecha
        b = a.izquierda
        a.izquierda = Node
        Node.derecha = b
        Node.altura = 1 + max(self.altura(Node.izquierda), self.altura(Node.derecha))
        a.altura = 1 + max(self.altura(a.izquierda), self.altura(a.derecha))
        return a

    def _insertar(self, nodo, nombre, piso, tipo):
        if not nodo:
            return Nodo(nombre, piso, tipo)
        elif nombre < nodo.data["nombre"]:
            nodo.izquierda = self._insertar(nodo.izquierda, nombre, piso, tipo)
        elif nombre > nodo.data["nombre"]:
            nodo.derecha = self._insertar(nodo.derecha, nombre, piso, tipo)
        else:
            return nodo  

        
        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))
        balance = self._balance(nodo)

        if balance > 1 and nombre < nodo.izquierda.data["nombre"]:
            return self._rotacionDerecha(nodo)
        if balance < -1 and nombre > nodo.derecha.data["nombre"]:
            return self._rotacionIzquierda(nodo)
        if balance > 1 and nombre > nodo.izquierda.data["nombre"]:
            nodo.izquierda = self._rotacionIzquierda(nodo.izquierda)
            return self._rotacionDerecha(nodo)
        if balance < -1 and nombre < nodo.derecha.data["nombre"]:
            nodo.derecha = self._rotacionDerecha(nodo.derecha)
            return self._rotacionIzquierda(nodo)

        return nodo
    
    def AgregarElemento(self, nombre, piso, tipo):
        self.raiz = self._insertar(self.raiz, nombre, piso, tipo)



    def _buscar(self, nodo, nombre):
        if nodo is None:
            return None
        if nombre == nodo.data["nombre"]:
            return nodo
        elif nombre < nodo.data["nombre"]:
            return self._buscar(nodo.izquierda, nombre)
        else:
            return self._buscar(nodo.derecha, nombre)

    def buscar(self, nombre):
        nodo = self._buscar(self.raiz, nombre)
        return nodo.data if nodo else None
        
    def _inorder(self, nodo, lista):
        if nodo:
            self._inorder(nodo.izquierda, lista)
            lista.append(nodo.data)
            self._inorder(nodo.derecha, lista)

    def inorder(self):
        lista = []
        self._inorder(self.raiz, lista)
        return lista

    def imprimir_inorder(self):
        X = self.inorder()
        if not X:
            print("El árbol está vacío")
            return
        for d in X:
            print(f"Lugar: {d['nombre']} | Piso: {d['piso']} | Tipo: {d['tipo']}")

    def _conteo(self, nodo):
        if not nodo:
            return 0
        return 1 + self._conteo(nodo.izquierda) + self._conteo(nodo.derecha)

    def cantidad_elementos(self):
        return self._conteo(self.raiz)
    





if __name__ == "__main__":
    arbol = AVL()
    arbol.AgregarElemento("D1", 2, "Tienda")
    arbol.AgregarElemento("Pasillo_P2", 2, "Pasillo")
    arbol.AgregarElemento("Escalera_Norte", 1, "Escalera")
    arbol.AgregarElemento("Nike", 1, "Tienda")
    arbol.AgregarElemento("Ascensor_Central", 3, "Ascensor")

    print("Cantidad de lugares en el arbol:", arbol.cantidad_elementos())
    print("\nLugares (ordenados por nombre):")
    arbol.imprimir_inorder()

    print("\nBusqueda:")
    buscado = "D1"
    res = arbol.buscar(buscado)
    print(res if res else f"No se encontró '{buscado}'")
    