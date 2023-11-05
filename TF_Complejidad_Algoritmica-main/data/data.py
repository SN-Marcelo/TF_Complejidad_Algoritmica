import csv
import sys
sys.path.append('./data/entity')
from entity.movie import Pelicula
from entity.grafo import Grafo

def ReadData():
    movie = []
    
    graph = Grafo()
    
    graph.agregarVertice(Pelicula(1,"Netflix",None,None,None,None,None,None,False,False,False,False))
    graph.agregarVertice(Pelicula(2,"Hulu",None,None,None,None,None,None,False,False,False,False))
    graph.agregarVertice(Pelicula(3,"Prime",None,None,None,None,None,None,False,False,False,False))
    graph.agregarVertice(Pelicula(4,"Disney+",None,None,None,None,None,None,False,False,False,False))


    with open('./data/datos.csv')as data:
        next(data)
        reader=csv.reader(data,delimiter=';')
        for row in reader:
            movie.append(Pelicula(row[0],row[1],row[2],row[3],row[4],row[5],row[6], row[7],bool(row[8]),bool(row[9]),bool(row[10]),bool(row[11])))
            franquicia = movie.getFranquicia()
            categoria = movie.getCategory()
            graph.agregarVertice(movie)
            if(movie.getnetflix()):
                graph.agregarArista(0, id ,movie[row].getPeso())
            elif(movie.gethulu()):
                graph.agregarArista(1, id ,movie[row].getPeso())
            elif(movie.getPrime()):
                graph.agregarArista(2, id ,movie[row].getPeso())
            elif(movie.getDisney()):
                graph.agregarArista(3, id ,movie[row].getPeso())
            
            if franquicia is not None:
                if franquicia not in graph.franquicia:
                    graph.franquicia[franquicia] = []
                else:
                    for j in range(len(graph.franquicia[franquicia])):
                        destino = graph.franquicia[franquicia][j]
                        if destino != movie[row].getName():
                            peso1 = movie[row].getPeso()
                            peso2 = movie[destino].getPeso()
                            if peso1 > peso2:
                                pesoTotal = (peso1 - peso2)
                            elif peso1 < peso2:
                                pesoTotal = (peso2-peso1)
                            else:
                                pesoTotal = 1
                                graph.agregarArista(id,destino,pesoTotal)

                graph.franquicia[franquicia].append(id)

            if categoria is not None:
                if categoria not in graph.categoria:
                    graph.categoria[categoria] = []
                else:
                    destino = graph.categoria[categoria][-1]
                    peso1 = movie[row].getPeso()
                    peso2 = movie[destino].getPeso()

                    if peso1 > peso2:
                        pesoTotal = (peso1 - peso2)
                    elif peso1 < peso2:
                        pesoTotal = (peso2 - peso1)
                    else:
                        pesoTotal = 1

                graph.agregarArista(id,destino,pesoTotal)
            graph.categoria[categoria].append(id)
              
        return graph
    

h = ReadData()