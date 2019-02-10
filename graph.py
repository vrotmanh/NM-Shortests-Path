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

def shortest_path(G, i, j):
	visited = [i]
	queue = []
	root = i
	paths = {root: 0}
	queue.insert(0, root)
	while(len(queue)>0):
		current = queue.pop()
		if(current == j):
			return paths[current]

		neighbors = g.get_neighbors(current)
		for neighbor in neighbors:
			if neighbor in visited:
				continue
			if neighbor not in queue:
				queue.insert(0, neighbor)
				if (neighbor not in paths) or (paths[neighbor]>paths[current]+1):
					paths[neighbor] = paths[current]+1

		visited.append(current)
	return float("inf")


# avg = 0
# for i in range(10000):
# 	g = create_graph(20,0.2)
# 	avg+=g.edges_count()
# print(avg/10000)

g = create_graph(5,0.5)
g.print_graph()
print(shortest_path(g, 0, 3))


