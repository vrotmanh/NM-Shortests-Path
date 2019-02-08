import random

class Graph:
    def __init__(self, nodes):
        self.edges = {}
        self.nodes = nodes
        for i in range(nodes):
        	self.edges[i] = []

    def add_edge(self, i, j):
    	if j not in self.edges[i]:
    		self.edges[i].append(j)
    		self.edges[j].append(i)

    def get_neighbors(self, i):
        return self.edges[i]

    def edges_count(self):
    	edges_count = 0
    	for i in range(self.nodes):
    		edges_count+=len(self.edges[i])
    	return edges_count/2

    def print_graph(self):
    	print(self.edges)

def create_graph(n,p):
	graph = Graph(n)
	for i in range(n):
		for j in range(i+1,n):
			if random.random() < p:
				graph.add_edge(i,j)
	return graph