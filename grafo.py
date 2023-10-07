import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import heapq as hq

def generar_matriz(n, manual):
    matriz = np.zeros((n, n))

    if not manual:
        for i in range(1, n):
            for j in range(i):
                # se determina si existirá una arista entre ambos nodos
                tiene_arista = np.random.randint(0, 2)
                if tiene_arista:
                    # generará un peso/distancia de 1 hasta 9
                    matriz[i][j] = matriz[j][i] = np.random.randint(1, 10)
                else:
                    matriz[i][j] = matriz[j][i] = 0
    else:
        print("En caso desee que no haya una arista entre dos nodos, puede ingresar 0.")
        for i in range(1, n):
            for j in range(i):
                while True:
                    # pedirá el valor del peso/distancia
                    valor = input(f"Ingrese el valor de la arista ({i}, {j}) = ({j}, {i}): ")
                    try:
                        valor = float(valor)
                        if valor >= 0:
                            break
                    except:
                        print("ERROR: Valor no válido. Ingrese nuevamente.")
                
                matriz[i][j] = matriz[j][i] = valor
                
    return matriz

class Nodo:
    def __init__(self, indice, valor):
        self.valor=valor
        self.indice = indice
        self.vecinos = []
        self.visitado = False


class Arista:
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

class Grafo:

    def __init__(self, matriz, valores_nodos):
        #pa comprobar
        self.matriz = matriz
        self.grafo = nx.Graph()
        self.tamano = len(matriz[0]) # cantidad de nodos

        for i in range(matriz.shape[0]):
            self.grafo.add_node(valores_nodos[0])
            for j in range(i):
                if matriz[i][j] != 0:
                    self.grafo.add_edge(valores_nodos[i], valores_nodos[j], weight=matriz[i][j])
        
        self.nodos = [Nodo(i, valores_nodos[i]) for i in range(matriz.shape[0])]
        self.aristas = []

        for i in range(matriz.shape[0]):
            for j in range(i):
                if matriz[i][j] != 0:
                    self.nodos[i].vecinos.append(j)
                    self.nodos[j].vecinos.append(i)

                    arista = Arista(i, j, matriz[i][j])
                    self.aristas.append(arista)
    
    def obtenerNodoIndice(self, valor):
        for i in range(self.tamano):
            if self.nodos[i].valor == valor:
                return i

    def obtenerNodoValor(self, indice):
        return self.nodos[indice].valor

    def mostrar_grafo(self, camino=None):
        posiciones = nx.spring_layout(self.grafo)
        nx.draw_networkx_nodes(self.grafo, posiciones)
        nx.draw_networkx_edges(self.grafo, posiciones)
        if camino:
            nx.draw_networkx_edges(self.grafo, posiciones, edgelist=camino, edge_color='blue', width=2)
        etiquetas = {nodo: nodo for nodo in self.grafo.nodes()}
        nx.draw_networkx_labels(self.grafo, posiciones, etiquetas)
        etiquetas_aristas = nx.get_edge_attributes(self.grafo, 'weight')
        nx.draw_networkx_edge_labels(self.grafo, posiciones, edge_labels=etiquetas_aristas)
        
        plt.axis('off')
        plt.show()

    def dijkstra(self, i, f):
        # obtener los indices de los nodos
        inicio = self.obtenerNodoIndice(i)
        fin = self.obtenerNodoIndice(f)

        # definicion de variables
        n = self.tamano # cantidad de nodos
        distancias = [float('inf')] * n # lista que almacena las distancias y se inicializan en infinito
        distancias[inicio] = 0 # se inicializa la distancia del nodo inicial en 0
        visitados = [False] * n # lista para marcar si los nodos han sido visitados
        anterior = [None] * n # lista para rastrear el nodo padre/anterior a un nodo en el camino
        pqueue = [(0, inicio)] # se utilizará como la cola de prioridad para ir sacando el nodo con la mínima distancia

        while pqueue:
            # se hace pop de la cola de prioridad y se extrae la distancia minima con el nodo
            dist, nodo_actual = hq.heappop(pqueue)

            # si el nodo actual ya fue visitado, se continua con el siguiente
            if visitados[nodo_actual]: continue
            
            # se marca el nodo actual como visitado
            visitados[nodo_actual] = True

            for vecino in range(n):
                # se obtiene la distancia/peso del nodo actual hacia el vecino
                distancia = self.matriz[nodo_actual][vecino]

                # verifica que la distancia sea mayor a cero para determinar si existe una arista
                # y si el vecino aun no ha sido visitado
                if distancia > 0 and not visitados[vecino]:
                    # se calcula la distancia sumando la distancia acumulada en el nodo actual
                    # con la distancia de la arista del nodo actual hacia el vecino
                    nueva_distancia = dist + distancia

                    # se verifica si la nueva distancia es menor a la que ya había para el vecino
                    if nueva_distancia < distancias[vecino]:
                        # se reemplaza la nueva distancia al ser la mínima
                        distancias[vecino] = nueva_distancia
                        # se agrega como nodo padre/anterior del vecino al nodo actual
                        anterior[vecino] = nodo_actual
                        # se agrega tuple de la distancia con el vecino a la cola de prioridad
                        hq.heappush(pqueue, (nueva_distancia, vecino))

        # en caso la distancia del nodo final siga siendo infinito, es porque no existe un camino
        if distancias[fin] == float('inf'):
            return None

        # una vez se termino de identificar todas las distancias mínimas
        # hacia todos los nodos desde el nodo inicial
        # se empieza a construir el camino, con una lista vacía
        # y se empieza desde el nodo final hasta el inicio
        camino = []
        nodo_actual = fin

        while nodo_actual is not None:
            # se inserta el nodo actual en el camino en la primera posicion
            # para que se añada en orden de inicio a fin
            camino.insert(0, self.obtenerNodoValor(nodo_actual))

            # se retrocede al nodo padre/anterior del nodo actual
            # con la lista de anteriores que creamos anteriormente
            nodo_actual = anterior[nodo_actual]

            # se hacen estos dos pasos hasta llegar al nodo inicial
            # en el cual ya no habrá nodo anterior y terminará el bucle
        
        # retorna el camino con la distancia total que es la que se almacena
        # en la lista de distancias en la posicion del nodo final
        return camino, distancias[fin]
