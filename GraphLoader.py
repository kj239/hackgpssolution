from Graph3 import Graph, dijkstra
from apiPoster import apiPoster

class GraphLoader():

    def __init__(self):
        self.gps = apiPoster()
        self.adjList = self.gps.getadjList()
        self.graph = Graph()
        
        for i in range(0,22500):
            self.graph.addedges(i,self.adjList[i])
        
    def getDict(self):
        return self.graph.dict
    
    def getDijkstra(self, start, end):
        return dijkstra(self.graph.dict, start,end)
         
    def __str__(self):
         return 'Graph loaded!'
