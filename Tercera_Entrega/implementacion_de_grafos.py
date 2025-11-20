
"""Implementacion de grafos.ipynb
Original file is located at
    https://colab.research.google.com/drive/1VOOOuTOYj_XC8sPFVv7jGtROUd4J8HVB
"""
"""
Sistema de navegación para centro comercial
Implementa un grafo ponderado para encontrar rutas entre locales
"""

class Nodo:
    """Representa un lugar del centro comercial, como las tiendas o restaurantes"""

    def __init__(self, nombre, piso, tipo):
        self.nombre = nombre
        self.piso = piso
        self.tipo = tipo

    def __repr__(self):
        # Así se ve cuando lo vamos a primir, el (nombre de el sitio)p(numero del piso)
        return f"{self.nombre}(p{self.piso})"

    def __eq__(self, otro):
        # compara dos nodos, solo importan nombre y piso
        return isinstance(otro, Nodo) and self.nombre == otro.nombre and self.piso == otro.piso

    def __hash__(self):
        # Necesario para usar nodos como llaves en diccionarios, le da un identificador a cada nodo
        return hash((self.nombre, self.piso))


class GrafoPonderado():
    """Grafo que representa las conexiones entre lugares del centro comercial"""

    def __init__(self, grafo=None):
        if grafo is None:
            grafo = {}
        self.grafo = grafo

    def __repr__(self):
        # Muestro todos los nodos y sus conexiones
        nodos = ''
        for nodo, aristas in self.grafo.items():
            nodos += f'{nodo}: {aristas}\n'
        return nodos

    def __iter__(self):
      # Itera al grafo
        self.iter_obj = iter(self.grafo)
        return self.iter_obj

    def nodos(self):
        # Regresa una lista con todos los nodos
        return list(self.grafo.keys())

    def aristas(self, nodo=None):
        # Si le paso un nodo, solo sus conexiones con otros nodos; si no, todas
        if nodo:
            if self.existeNodo(nodo):
                return [(nodo, a) for a in self.grafo[nodo]]
            else:
                return []
        else:
            return [(n, a) for n in self.grafo.keys() for a in self.grafo[n]]

    def nodosAislados(self):
        # Lugares sin conexiones 
        return [nodo for nodo in self.grafo if not self.grafo[nodo]]

    def orden(self):
        #  Numero de nodos
        return len(self.grafo)

    def tamaño(self):
        # Calcula el numero total de aristas (conexiones unicas) presentes en el grafo
        arcos = []
        for nodo, aristas in self.grafo.items():
            for arista, p in aristas:
                # Ordeno para evitar duplicados (porque es un grafo no dirigido, entonces contaria cada arista 2 veces)
                # Asi en lugar de que (A-B Y B-A) sean iguales lo diferenciamos porque hacemos una tupla ordenada
                arista_ordenada = tuple(sorted([nodo, arista], key=lambda x: x.nombre))
                if arista_ordenada not in arcos:
                    arcos.append(arista_ordenada)
        return len(arcos)

    def agregarNodo(self, nodo):
        # Agrego un lugar nuevo sin conexiones
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def eliminarNodo(self, nodo):
        # Borro el lugar y todas sus conexiones
        if nodo in self.grafo:
            aristas = list(self.grafo[nodo])
            for arista, p in aristas:
                self.eliminarArista((nodo, arista))
            self.grafo.pop(nodo)

    def agregarArista(self, arista, peso):
        # Conecto dos lugares en ambas direcciones con un tiempo estimado
        n1, n2 = tuple(arista)
        for n, a in [(n1, n2), (n2, n1)]:
            if n in self.grafo:
                # Solo agrego si no existe ya
                if a not in [destino for destino, _ in self.grafo[n]]:
                    self.grafo[n].append((a, peso))
            else:
                self.grafo[n] = [(a, peso)]

    def eliminarArista(self, arista):
        # Borro la conexión en ambas direcciones
        n1, n2 = tuple(arista)
        for n, a in [(n1, n2), (n2, n1)]:
            if n in self.grafo:
                for nodo, peso in self.grafo[n]:
                    if nodo == a:
                        self.grafo[n].remove((nodo, peso))
                        break

def encontrarRutas(self, inicio, fin, ruta=[]):
    # Verifico que los nodos existan
    if inicio not in self.grafo or fin not in self.grafo:
        return []
    
    ruta = ruta + [inicio]  # Agrego el nodo actual a la ruta
    
    # Caso base: llegué al destino
    if inicio == fin:
        return [ruta]
    
    rutas = []
    # Exploro cada vecino
    for nodo, _ in self.grafo[inicio]:
        if nodo not in ruta:  # Evito volver a lugares ya visitados
            # RECURSIÓN: busco rutas desde el vecino hasta el fin
            nuevas_rutas = self.encontrarRutas(nodo, fin, ruta)
            for subruta in nuevas_rutas:
                rutas.append(subruta)
    
    return rutas

def rutaMasCorta(self, inicio, fin): # Usamos el algoritmo de dijkstra
    INF = float('inf')  # Infinito para distancias desconocidas
    
    # Inicializo: todos los nodos con distancia infinita
    no_visitados = {nodo: INF for nodo in self.grafo.keys()}
    predecesor = {nodo: None for nodo in self.grafo.keys()}  # De dónde vengo
    visitados = {}
    
    actual = inicio
    peso_actual = 0
    no_visitados[actual] = 0  # El inicio tiene distancia 0
    
    while no_visitados:
        # Actualizo distancias de los vecinos del nodo actual
        for nodo, peso in self.grafo[actual]:
            if nodo in no_visitados:
                nuevo_peso = peso_actual + peso
                # Si encontré una ruta más corta
                if no_visitados[nodo] > nuevo_peso:
                    no_visitados[nodo] = nuevo_peso
                    predecesor[nodo] = actual  # Guardo de dónde vine
        
        # Marco como visitado
        visitados[actual] = peso_actual
        no_visitados.pop(actual)
        
        if not no_visitados:
            break
        
        # Elijo el siguiente nodo: el no visitado con menor distancia
        actual, peso_actual = min(no_visitados.items(), key=lambda x: x[1])
    
    # Reconstruyo la ruta desde el final hacia atrás
    ruta = []
    nodo = fin
    while nodo is not None:
        ruta.append(nodo)
        nodo = predecesor[nodo]  # Retrocedo
    
    return (ruta[::-1], visitados[fin])  # La volteo y devuelvo con el tiempo

    def estaVacio(self):
        # Verifico si hay lugares en el grafo
        return self.grafo == {}

    def existeNodo(self, nodo):
        # Chequeo si existe un lugar específico
        return nodo in self.grafo.keys()

    def existeArista(self, arista):
        # Verifico si hay conexión entre dos lugares
        n1, n2 = tuple(arista)
        return any(destino == n2 for destino, _ in self.grafo[n1]) or \
               any(destino == n1 for destino, _ in self.grafo[n2])

    def filtrar(self, tipo=None, piso=None):
        # Busco lugares según tipo y/o piso
        resultados = []
        for nodo in self.grafo.keys():
            cumple_tipo = (tipo is None or nodo.tipo == tipo)
            cumple_piso = (piso is None or nodo.piso == piso)
            if cumple_tipo and cumple_piso:
                resultados.append(nodo)
        return resultados


# ===================== DATOS DE EJEMPLO =====================
# Piso 1
entrada = Nodo("entrada", 1, "entrada")
addidas = Nodo("addidas", 1, "tienda")
juanvaldez = Nodo("Juan valdez", 1, "restaurante")
nike = Nodo("nike", 1, "tienda")
baño1 = Nodo("baño 1", 1, "baño")
reebok = Nodo("Reebok", 1, "tienda")
popsy = Nodo("popsy", 1, "restaurante")
kfc = Nodo("kfc", 1, "restaurante")

# Piso 2
d1 = Nodo("d1", 2, "tienda")
koaj = Nodo("koaj", 2, "tienda")
dolarcity = Nodo("dolarcity", 2, "tienda")
baño2 = Nodo("baño 2 ", 2, "baño")
hym = Nodo("HyM", 2, "tienda")

# Piso 3
mattelsa = Nodo("mattelsa", 3, "tienda")
mercagan = Nodo("mercagan", 3, "restaurante")
baño3 = Nodo("baño 3", 3, "baño")
cinecolombia = Nodo("Cine colombia", 3, "entretenimiento")
casino = Nodo("Casino brodway", 3, "entretenimiento")

# Conexiones verticales
escalera1_2 = Nodo("Escalera 1-2", 0, "escalera")
escalera2_3 = Nodo("Escalera 2-3", 0, "escalera")
ascensor = Nodo("Ascensor", 0, "ascensor")

# Creo el grafo con todas las conexiones y sus tiempos
grafo_dict = {
    entrada: [(addidas, 2), (juanvaldez, 2)],
    addidas: [(entrada, 2), (juanvaldez, 4), (nike, 5)],
    nike: [(baño1, 1), (addidas, 5)],
    baño1: [(nike, 1), (reebok, 1)],
    reebok: [(baño1, 1), (escalera1_2, 2), (kfc, 4), (ascensor, 1)],
    juanvaldez: [(entrada, 2), (addidas, 4), (popsy, 6)],
    popsy: [(juanvaldez, 6), (kfc, 2)],
    kfc: [(popsy, 2), (reebok, 4), (ascensor, 1)],
    ascensor: [(reebok, 1), (kfc, 1), (d1, 1), (hym, 1), (mercagan, 2), (mattelsa, 2)],
    d1: [(ascensor, 1), (escalera1_2, 3), (hym, 4), (koaj, 3)],
    koaj: [(d1, 3), (dolarcity, 4)],
    dolarcity: [(koaj, 4), (baño2, 1), (escalera2_3, 2)],
    baño2: [(dolarcity, 1), (hym, 1)],
    hym: [(ascensor, 1), (d1, 4), (baño2, 1)],
    mercagan: [(ascensor, 2), (mattelsa, 4), (baño3, 2)],
    baño3: [(mercagan, 2), (cinecolombia, 1)],
    cinecolombia: [(baño3, 1), (casino, 4)],
    casino: [(cinecolombia, 4), (mattelsa, 3)],
    mattelsa: [(ascensor, 2), (mercagan, 4), (casino, 3), (escalera2_3, 3)]
}

G = GrafoPonderado(grafo_dict)

# ===================== MENÚ INTERACTIVO =====================
TIPOS_LUGAR = [
    "restaurante",
    "tienda",
    "baño",
    "entretenimiento",
    "escalera",
    "ascensor",
    "entrada",
    "salida"
]

while True:
    print("\n===== MENÚ =====")
    print("1. Ver nodos")
    print("2. Agregar nodo")
    print("3. Eliminar nodo")
    print("4. Filtrar")
    print("5. Hallar ruta más corta")
    print("6. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        # Mostrar todos los lugares
        print("\n--- Lista de nodos ---")
        for nodo in G.nodos():
            print(nodo, f"(tipo={nodo.tipo}, piso={nodo.piso})")

    elif opcion == "2":
        # Crear un nuevo lugar
        try:
            print("\n== Crear nodo ==")
            nombre = input("Nombre del nodo: ")
            piso = int(input("Piso: "))

            # Elegir tipo de lugar
            print("\nTipos de lugar:")
            for i, t in enumerate(TIPOS_LUGAR, start=1):
                print(f"{i}. {t}")
            tnum = int(input("Tipo (número): "))
            tipo = TIPOS_LUGAR[tnum - 1]

            nuevo = Nodo(nombre, piso, tipo)
            G.agregarNodo(nuevo)
            print("Nodo agregado:", nuevo)

            # Conectar con lugares del mismo piso
            existentes = [n for n in G.nodos() if n != nuevo and n.piso == piso]

            if existentes:
                print("\nConectar con :")
                for i, n in enumerate(existentes, start=1):
                    print(f"{i}. {n}")

                sel = input("Número: ")
                if sel != "":
                    for idx in sel.split():
                        i = int(idx) - 1
                        destino = existentes[i]
                        peso = int(input(f"Peso entre {nuevo} y {destino}: "))
                        G.agregarArista((nuevo, destino), peso)
                        print("Conectado:", nuevo, "<->", destino)

        except:
            print("Error en la creación del nodo.")

    elif opcion == "3":
        # Eliminar un lugar existente
        try:
            nodos = G.nodos()
            if not nodos:
                print("No hay nodos para eliminar.")
                continue

            print("\n--- Selecciona el nodo a eliminar ---")
            for i, n in enumerate(nodos, start=1):
                print(f"{i}. {n} (tipo={n.tipo}, piso={n.piso})")

            sel = int(input("Número: ")) - 1

            if sel < 0 or sel >= len(nodos):
                print("Selección inválida.")
                continue

            elegido = nodos[sel]
            G.eliminarNodo(elegido)
            print("Nodo eliminado:", elegido)

        except:
            print("Error eliminando nodo.")

    elif opcion == "4":
        # Buscar lugares por tipo y/o piso
        print("\nFiltrar por tipo (0 = ignorar):")
        print("0. Ignorar")
        for i, t in enumerate(TIPOS_LUGAR, start=1):
            print(f"{i}. {t}")
        ft = input("Tipo: ")
        tipo = None
        if ft not in ("", "0"):
            tipo = TIPOS_LUGAR[int(ft) - 1]

        pisos = sorted({n.piso for n in G.nodos()})
        print("\nFiltrar por piso (0 = ignorar):")
        for p in pisos:
            print("-", p)
        fp = input("Piso: ")
        piso = None
        if fp not in ("", "0"):
            piso = int(fp)

        res = G.filtrar(tipo=tipo, piso=piso)
        print("\n--- Resultados ---")
        for r in res:
            print(r, f"(tipo={r.tipo}, piso={r.piso})")
        if not res:
            print("Nada encontrado.")

    elif opcion == "5":
        # Calcular ruta más rápida entre dos lugares
        print("\n--- Selecciona el nodo de inicio ---")
        nodos = G.nodos()
        for i, n in enumerate(nodos, start=1):
            print(f"{i}. {n}")

        ini = int(input("Inicio: ")) - 1
        fin = int(input("Fin: ")) - 1

        if ini < 0 or ini >= len(nodos) or fin < 0 or fin >= len(nodos):
            print("Selección inválida.")
            continue

        n_inicio = nodos[ini]
        n_fin = nodos[fin]

        ruta, tiempo = G.rutaMasCorta(n_inicio, n_fin)

        print("\n--- Ruta más corta ---")
        print(" → ".join([str(x) for x in ruta]))
        print("Tiempo estimado:", tiempo, "minutos")

    elif opcion == "6":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
