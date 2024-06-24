import heapq

class ClassDijkstra:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, vertice1, vertice2, peso):
        self.vertices[vertice1][vertice2] = peso
        self.vertices[vertice2][vertice1] = peso

    def dijkstra(self, inicio, destino):
        distancias = {vertice: float('inf') for vertice in self.vertices}
        camino = {vertice: [] for vertice in self.vertices}
        distancias[inicio] = 0
        cola = [(0, inicio)]

        while cola:
            distancia_actual, vertice_actual = heapq.heappop(cola)

            if vertice_actual == destino:
                break

            for adyacente, peso in self.vertices[vertice_actual].items():
                distancia_nueva = distancia_actual + peso
                if distancia_nueva < distancias[adyacente]:
                    distancias[adyacente] = distancia_nueva
                    camino[adyacente] = camino[vertice_actual] + [(vertice_actual, adyacente, peso)]
                    heapq.heappush(cola, (distancia_nueva, adyacente))

        ruta = camino[destino]
        return ruta, distancias[destino]
