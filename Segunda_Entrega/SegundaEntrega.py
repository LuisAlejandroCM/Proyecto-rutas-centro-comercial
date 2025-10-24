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

    #te da el valor balance
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
        
    #rotacion hacia la derecha     
    
    def _rotacionDerecha(self, Node):
        a = Node.izquierda
        b = a.derecha
        a.derecha = Node
        Node.izquierda = b
        Node.altura = 1 + max(self.altura(Node.izquierda), self.altura(Node.derecha))
        a.altura = 1 + max(self.altura(a.izquierda), self.altura(a.derecha))
        return a
    
    #rotacion hacia la izquierda
    
    def _rotacionIzquierda(self, Node):
        a = Node.derecha
        b = a.izquierda
        a.izquierda = Node
        Node.derecha = b
        Node.altura = 1 + max(self.altura(Node.izquierda), self.altura(Node.derecha))
        a.altura = 1 + max(self.altura(a.izquierda), self.altura(a.derecha))
        return a

    #insertar y que se balancee
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
    
    #agregar elemento, te pide nombre piso y tipo y llama la funcion "_insertar"
    
    def AgregarElemento(self, nombre, piso, tipo):
        self.raiz = self._insertar(self.raiz, nombre, piso, tipo)

    def _eliminar(self, nodo, nombre):
        if nodo is None:
            return None

        if nombre < nodo.data["nombre"]:
            nodo.izquierda = self._eliminar(nodo.izquierda, nombre)
        elif nombre > nodo.data["nombre"]:
            nodo.derecha = self._eliminar(nodo.derecha, nombre)
        else:
      
            if nodo.izquierda is None:
                temp = nodo.derecha
                nodo = None
                return temp
            elif nodo.derecha is None:
                temp = nodo.izquierda
                nodo = None
                return temp
    
            sucesor = self.valorMinimoNodo(nodo.derecha)
            nodo.data = sucesor.data.copy()
            nodo.derecha = self._eliminar(nodo.derecha, sucesor.data["nombre"])

        if nodo is None:
            return None

        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))
        balance = self._balance(nodo)

        
        if balance > 1 and self._balance(nodo.izquierda) >= 0:
            return self._rotacionDerecha(nodo)
        if balance > 1 and self._balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotacionIzquierda(nodo.izquierda)
            return self._rotacionDerecha(nodo)
        if balance < -1 and self._balance(nodo.derecha) <= 0:
            return self._rotacionIzquierda(nodo)
        if balance < -1 and self._balance(nodo.derecha) > 0:
            nodo.derecha = self._rotacionDerecha(nodo.derecha)
            return self._rotacionIzquierda(nodo)

        return nodo
    #eliminar elemento
    def EliminarElemento(self, nombre):
        self.raiz = self._eliminar(self.raiz, nombre)

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
    
        #recorridos
        
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
 
    #peso del árbol avl
    
    def _conteo(self, nodo):
        if not nodo:
            return 0
        return 1 + self._conteo(nodo.izquierda) + self._conteo(nodo.derecha)
    
  
    
    def cantidad_elementos(self):
         return self._conteo(self.raiz)
     
     #filtra tipo y piso y si uno de ellos e None solo toma en cuenta el que tenga cierto valor
    def filtrar(self, tipo=None, piso=None):
       
        resultados = []
        def _rec(nodo):
            if nodo is None:
                return
            _rec(nodo.izquierda)
            d = nodo.data
            if (tipo is None or d["tipo"] == tipo) and (piso is None or d["piso"] == piso):
                resultados.append(d)
            _rec(nodo.derecha)
        _rec(self.raiz)
        return resultados
    
    #recibe tipo y llama a filtral, unicamente llamando a tipo
    
    def filtrar_por_tipo(self, tipo):
        return self.filtrar(tipo=tipo)
    
    #recibe piso y llama a filtral, unicamente llamando a tipo
    
    def filtrar_por_piso(self, piso):
        return self.filtrar(piso=piso)


arbol = AVL()

