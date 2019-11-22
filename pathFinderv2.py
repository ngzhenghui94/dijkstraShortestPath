import sys
from collections import defaultdict
from heapq import *
import re

from collections import defaultdict, deque

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

if __name__ == '__main__':
    allPaths= []
    firstNode = []
    nextNode = []
    distBtw = []
    noOfPaths = 0
    f = open("mapData.dat","r")
    line = f.readline()
    while line:
        if line.startswith('"'):
            line = line.rstrip()
            line = re.sub('"','',line)
            allPaths.append(line)
            fields = line.split(",")
            firstNode.append(fields[0])
            nextNode.append(fields[1])
            distBtw.append(fields[2])
            noOfPaths = noOfPaths + 1
        line=f.readline()
    f.close()
        
    g = Graph()
    for i in range(0,len(firstNode)):
        g.add_node(str(firstNode[i]))
        g.add_edge(str(firstNode[i]),str(nextNode[i]),int(distBtw[i]))

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
            print("Shortest Dist: ",shortest_path(g, start, end))
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
        print("Shortest Dist: ",shortest_path(g, start, end))
    print(g)