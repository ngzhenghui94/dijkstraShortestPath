import sys 
  
from collections import defaultdict 

#define graph.
class Graph: 
    # A utility function to find the  
    # vertex with minimum dist value, from 
    # the set of vertices still in queue 
    def minDistance(self,dist,queue): 
        # Initialize min value and min_index as -1 
        minimum = float("Inf") 
        min_index = -1
        # from the dist array,pick one which 
        # has min value and is till in queue 
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 
  
  
    # Function to print path (shortest)
    def printPath(self, parent, j): 
        #Base Case : If j is source 
        if parent[j] == -1 :  
            path.append(gNodes[j])
            return
        self.printPath(parent , parent[j]) 
        path.append(gNodes[j])
          
  
    # A utility function to print 
    # the constructed distance 
    # array 
    def printSolution(self, dist, parent): 
        for i in range(0, len(dist)): 
            if i == Eid:
                print("Finding route from:\n%s --> %s\nShortest distance: %d" % (gNodes[Sid], gNodes[i], dist[i]), "km\nRouting:"), 
                self.printPath(parent,i)
                print(path)

    def dijkstra(self, graph, src): 
  
        row = len(graph) 
        col = len(graph[0]) 
  
        # The output array. dist[i] will hold 
        # the shortest distance from src to i 
        # Initialize all distances as INFINITE  
        dist = [float("Inf")] * row 
  
        #Parent array to store  
        # shortest path tree 
        parent = [-1] * row 
  
        # Distance of source vertex  
        # from itself is always 0 
        dist[src] = 0
      
        # Add all vertices in queue 
        queue = [] 
        for i in range(row): 
            queue.append(i) 
              
        #Find shortest path for all vertices 
        while queue: 
  
            # Pick the minimum dist vertex  
            # from the set of vertices 
            # still in queue 
            u = self.minDistance(dist,queue)  
  
            # remove min element      
            queue.remove(u) 
  
            # Update dist value and parent  
            # index of the adjacent vertices of 
            # the picked vertex. Consider only  
            # those vertices which are still in 
            # queue 
            for i in range(col): 
                '''Update dist[i] only if it is in queue, there is 
                an edge from u to i, and total weight of path from 
                src to i through u is smaller than current value of 
                dist[i]'''
                if graph[u][i] and i in queue: 
                    if dist[u] + graph[u][i] < dist[i]: 
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 
  
  
        # print the constructed distance array 
        self.printSolution(dist,parent) 
  
# Driver program 
g  = Graph() 
graph = [
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
#print(graph)
path = []

#define the adjacency matrix labels. i.e index 0 of adj matrix = sembawang
gNodes = ["Sembawang","Woodlands","Nee Soon","Ang Mo Kio","Punggol","Changi","Tampines","Bedok","Serangoon","Toa Payoh","Marina Bay","Outram","Sentosa","Pasir Panjang","Clementi","Queenstown","Bukit Timah","Bukit Panjang","Bukit Batok","Jurong","Tuas","Choa Chu Kang","Mandai","Upper Thomson"]
 
start = input("Where are you?\n")
end = input("Where do you want to go\n")
print("\n")
Sid = gNodes.index(start)
Eid = gNodes.index(end)
g.dijkstra(graph, Sid);

