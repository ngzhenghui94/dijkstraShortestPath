from collections import defaultdict
from heapq import *
import re
import sys
allPaths= []
firstNode = []
nextNode = []
distInBtw = []
f = open("mapData.dat","r")
line = f.readline()
while line:
    #read only lines in the file with the path defined.
    if line.startswith('"'): 
        line = line.rstrip() 
        line = re.sub('"','',line)
        #store the information in each line into a list (allPaths)
        allPaths.append(line) 
        #split the line with delimiter ",", for use for processing and input checking.
        fields = line.split(",")
        firstNode.append(fields[0])
        nextNode.append(fields[1])
        distInBtw.append(fields[2])
    line=f.readline()
f.close()

def dijkstra(allPaths, start, end):
    #using defaultdict(list) as it is easy to group a seq of key-value pair into a dictionary of lists/link-list
    #Key : [(Dist, Connected Region),....]
    #i.e 'Sembawang':[(5,'Woodlands'),(5,'Nee Soon'),(6,'Mandai')]
    graph = defaultdict(list) 
    for i in allPaths:
        fields = i.split(",")
        distInBtw = int(fields[2])
        graph[fields[0]].append((distInBtw,fields[1]))
    #define the tuple (tupleA), tupleA[0] is the dist, tupleA[1] refers to the starting Node, tupleA[2] will be used to store the path
    tupleA= [(0, start, ())] 
    nodeSeen = {''} 
    #dist records the min of each node in heappop
    dist = {start:0}
    #check the graph
    #print(graph)
    while tupleA:
        (cost,v1,path) = heappop(tupleA)
        if v1 not in nodeSeen:
            nodeSeen.add(v1)
            path += (v1,)
            #if v1 == t: return print("Shortest distance:", cost, "km", path)
            if v1 == end: return toString(cost, path)
            for distInBtw, v2 in graph.get(v1, ()):
                if v2 in nodeSeen: continue
                next = cost + distInBtw
                heappush(tupleA, (next,v2,path))
    return float("inf")

def toString(cost, path):
    oput = "Shortest Distance to Destination: " + str(cost) + "km\n" + str(path)
    print(oput)

if __name__ == "__main__":
    print("=== Dijkstra ===")
    if len(sys.argv) > 1:
        try:
            start = str(sys.argv[1])
            do = 1
            while do: 
                if start not in firstNode:
                    print("Error please enter a valid start location")
                    start = input("//Where are you?\n")
                elif start in firstNode:
                    do = 0
            end = str(sys.argv[2])
            while do == 0: 
                if end not in firstNode or end == start:
                    print("Error please enter a valid end location")
                    end = input("//Where to?\n")
                elif end in firstNode:
                    do = 1
            print ("Finding route from ", start , " -> " , end)
            dijkstra(allPaths, start, end)
        except ValueError:
            pass
    else:
        start = input("//Where are you?\n")
        do = 1
        while do: 
            if start not in firstNode:
                print("Error please enter a valid start location")
                start = input("//Where are you?\n")
            elif start in firstNode:
                do = 0
        end = input("//Where to?\n")
        while do == 0: 
            if end not in firstNode or end == start:
                print("Error please enter a valid end location")
                end = input("//Where to?\n")
            elif end in firstNode:
                do = 1
        print ("Finding route from ", start , " -> " , end)
        dijkstra(allPaths, start.rstrip(), end.rstrip())
    

