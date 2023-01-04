from collections import defaultdict 
 
class Graph:
    def __init__(self, vertices):
        #Diccionario que contiene la lista de adyaciencia
        self.graph = defaultdict(list) 
        #Número de vértices
        self.V = vertices 
 
    # Función para agregar un grafo
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # Función recursiva utilizada por topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
 
        # Marcamos el nodo como visitado
        visited[v] = True
 
        # Recorremos todos los vértices que tienen conexión con este
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        #Hacemos push al vértice
        stack.append(v)
 
    def topologicalSort(self):
        # Iniicamos todos los vertices como no visitados
        visited = [False]*self.V
        stack = []
 
        # Empezamos a recorrer vértice por vértice
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Imprimimos la pila al revés 
        print(stack[::-1])  