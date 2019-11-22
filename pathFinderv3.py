import sys 
  
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                      for row in range(vertices)] 
  
    def printSolution(self, dist): 
        for node in range(self.V): 
            if node == Eid:
                print(gNodes[Gid],"to", gNodes[Eid], "shortest distance:" , dist[node], "km")
                
             
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
        # Initilaize minimum distance for next node 
        min = sys.maxsize 
        
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 

                
        return min_index 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src, dst): 
        dist = [sys.maxsize] * self.V 

        dist[src] = 0
        nodeSeen={''}
        sptSet = [False] * self.V 
        for cout in range(self.V): 
            
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
            #print(sptSet[u])
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
            
            
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                    dist[v] = dist[u] + self.graph[u][v] 
                    print(dist[v])
                    
  
        self.printSolution(dist) 
  
# Driver program 
g  = Graph(24) 
g.graph = [
[0,5,5,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,6,99], 
[5,0,9,99,99,99,99,99,99,99,99,99,99,99,99,99,99,11,99,99,99,11,8,99],
[5,9,0,6,99,99,99,99,99,99,99,99,99,99,99,99,99,16,99,99,99,99,3,99],
[99,99,6,0,99,99,99,99,6,99,99,99,99,99,99,99,99,16,18,99,99,99,99,5],
[99,99,99,99,0,99,99,99,8,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
[99,99,99,99,99,0,5,99,16,18,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
[99,99,99,99,99,5,0,5,12,15,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
[99,99,99,99,99,99,5,0,99,13,16,16,99,99,99,99,22,99,99,99,99,99,99,16],
[99,99,99,6,8,16,12,99,0,6,99,99,99,99,99,99,99,99,99,99,99,99,99,8],
[99,99,99,99,99,18,15,13,6,0,10,8,99,99,99,9,10,99,99,99,99,99,99,6],
[99,99,99,99,99,99,99,16,99,10,0,2,99,99,99,99,99,99,99,99,99,99,99,99],
[99,99,99,99,99,99,99,16,99,8,2,0,6,99,99,5,99,99,99,99,99,99,99,99],
[99,99,99,99,99,99,99,99,99,99,99,6,0,8,99,10,99,99,99,99,99,99,99,99],
[99,99,99,99,99,99,99,99,99,99,99,99,8,0,7,6,99,99,99,99,99,99,99,99],
[99,99,99,99,99,99,99,99,99,99,99,99,99,7,0,5,5,99,7,99,99,99,99,99],
[99,99,99,99,99,99,99,99,99,9,99,5,10,6,5,0,9,99,99,99,99,99,99,10],
[99,99,99,99,99,99,99,22,99,10,99,99,99,99,5,9,0,6,5,25,99,99,99,11],
[99,11,16,16,99,99,99,99,99,99,99,99,99,99,99,99,6,0,7,99,99,4,15,14],
[99,99,99,18,99,99,99,99,99,99,99,99,99,99,7,99,5,7,0,19,16,6,99,99],
[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,25,99,19,0,19,22,99,99],
[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,16,19,0,15,99,99],
[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,4,6,22,15,0,99,99],
[6,8,3,99,99,99,99,99,99,99,99,99,99,99,99,99,99,15,99,99,99,99,0,99],
[99,99,99,5,99,99,99,16,8,6,99,99,99,99,99,10,11,14,99,99,99,99,99,0]
]

gNodes = ["Sembawang","Woodlands","Nee Soon","Ang Mo Kio","Punggol","Changi","Tampines","Bedok","Serangoon","Toa Payoh","Marina Bay","Outram","Sentosa","Pasir Panjang","Clementi","Queenstown","Bukit Timah","Bukit Panjang","Bukit Batok","Jurong","Tuas","Choa Chu Kang","Mandai","Upper Thomson"]
 
start = "Changi" #5
end = "Woodlands"  #4
Gid = gNodes.index(start)
Eid = gNodes.index(end)
g.dijkstra(Gid, Eid);

