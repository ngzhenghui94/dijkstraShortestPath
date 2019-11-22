import sys 
  
from collections import defaultdict 

#define graph.
class Graph: 
    #function to find the  
    #vertex with minimum dist value, from 
    #the set of vertices still in queue 
    def minDistance(self,dist,queue): 
        #init min as float(inf), useful for finding lowest value for calc path route cost when traversing
        minimum = float("Inf") 
        #define min_index at -1
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
        # Initialize all distances as float(inf)  
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
  






listG = []
"""with open("mapMatrixRaw.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
graph.append(content)"""
path = []
with open("mapMatrixRaw.txt") as f:
    for line in f:
        int_list = [int(i) for i in line.split()]
        listG.append(int_list)

#print(listG) print the 2d array

#define the adjacency matrix labels. i.e index 0 of adj matrix = sembawang
gNodes = ["Sembawang","Woodlands","Nee Soon","Ang Mo Kio","Punggol","Changi","Tampines","Bedok","Serangoon","Toa Payoh","Marina Bay","Outram","Sentosa","Pasir Panjang","Clementi","Queenstown","Bukit Timah","Bukit Panjang","Bukit Batok","Jurong","Tuas","Choa Chu Kang","Mandai","Upper Thomson"]
 
 #get input
start = input("Where are you?\n")
end = input("Where do you want to go\n")
print(" ")
#grab the index of the start/end input for mapping
#i.e if start = Changi, Sid will be mapped to 5
Sid = gNodes.index(start)
Eid = gNodes.index(end)
#init
g = Graph() 
#call fn with the graph and starting node as pram. 
g.dijkstra(listG, Sid)
