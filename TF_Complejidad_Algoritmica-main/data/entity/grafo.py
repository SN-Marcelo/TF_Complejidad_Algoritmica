class Grafo:
    def __init__(self):
        self.movies = {}  # Un diccionario para almacenar las películas por su ID
        self.aristas = {} #Un diccionario para almacenar los pesos de las aristas
        self.franquicia = {}
        self.categoria = {}

    def agregarVertice(self, movie):
        if movie.getID() not in self.movies:
            self.movies[movie.getID()] = movie
            self.aristas[movie.getID()] = {}

    def agregarArista(self, movie_id_1, movie_id_2, peso):
        if movie_id_1 in self.movies and movie_id_2 in self.movies:
            movie1 = self.movies[movie_id_1]
            movie2 = self.movies[movie_id_2]
            self.aristas[movie_id_1][movie_id_2] = peso
            self.aristas[movie_id_2][movie_id_1] = peso
            return True
        return False

    def getPeso(self, movie_id_1, movie_id_2):
        if movie_id_1 in self.aristas and movie_id_2 in self.aristas[movie_id_1]:
            return self.aristas[movie_id_1][movie_id_2]
        return None

    def get_movie(self, movie_id):
        return self.movies.get(movie_id)

# Función para implementar el algoritmo de Kruskal y encontrar el Minimum Spanning Tree
    def kruskal(self):
        
        def find(parent, node):
            if parent[node] == node:
                return node
            return find(parent, parent[node])

        def union(parent, rank, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
                rank[root_y] += 1

        edges = []
        for movie_id_1 in self.aristas:
            for movie_id_2, peso in self.aristas[movie_id_1].items():
                edges.append((movie_id_1, movie_id_2, peso))

        edges.sort(key=lambda edge: edge[2])  # Ordenar las aristas por peso

        parent = {}
        rank = {}

        for movie_id in self.movies:
            parent[movie_id] = movie_id
            rank[movie_id] = 0

        minimum_spanning_tree = []

        for edge in edges:
            movie_id_1, movie_id_2, peso = edge
            root_1 = find(parent, movie_id_1)
            root_2 = find(parent, movie_id_2)

            if root_1 != root_2:
                minimum_spanning_tree.append((movie_id_1, movie_id_2, peso))
                union(parent, rank, root_1, root_2)

        return minimum_spanning_tree