import heapq
from sys import stdout

class Graph():
    
    def __init__(self):
        self.dict = {}
        self.num_vertices = 0
        
    ''' edges here is an array of vertices that the vertex points to. Weights are all 1'''        
        
    def addedges(self, vertex, edges):
        newarray = []
        for elem in edges:
            newarray.append((elem,1))
        self.dict[vertex] = newarray
        self.num_vertices += 1

    def numVertices(self):
        return self.num_vertices
    
    def numEdges(self, vertex):
        return len(self.dict[vertex])
    
# Dijkstra's shortest path algorithm. Prints the path from source to target.
'''Source: https://algocoding.wordpress.com/2015/03/28/dijkstras-algorithm-part-4a-python-implementation/''' 

def dijkstra(adj, source, target):
    INF = ((1<<63) - 1)//2
    pred = { x:x for x in adj }
    dist = { x:INF for x in adj }
    dist[ source ] = 0
    PQ = []
    heapq.heappush(PQ, [dist[ source ], source])
 
    while(PQ):
        u = heapq.heappop(PQ)  # u is a tuple [u_dist, u_id]
        u_dist = u[0]
        u_id = u[1]
        if u_dist == dist[u_id]:
            #if u_id == target:
            #    break
            for v in adj[u_id]:
               v_id = v[0]
               w_uv = v[1]
               if dist[u_id] +  w_uv < dist[v_id]:
                   dist[v_id] = dist[u_id] + w_uv
                   heapq.heappush(PQ, [dist[v_id], v_id])
                   pred[v_id] = u_id
                
    if dist[target]==INF:
        stdout.write("There is no path between ", source, "and", target)
    else:
        st = []
        node = target
        while(True):
            st.append(int(node))
            if(node==pred[node]):
                break
            node = pred[node]
        path = st[::-1]
        
    return path