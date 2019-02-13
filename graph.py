import random
import matplotlib.pyplot as plt

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

# g = create_graph(5,0.5)
# g.print_graph()
# print(shortest_path(g, 0, 3))

# c) avg 1.907
# g = create_graph(1000,0.1)
# avg = 0
# f = open("avg_shortest_path.txt", "a")
# count=0
# for k in range(1000):
# 	i = random.randint(0,999)
# 	j = i
# 	while(j==i):
# 		j = random.randint(0,999)
# 	print(count)
# 	count+=1
# 	path_lenght = shortest_path(g,i,j)
# 	avg+=path_lenght
# 	f.write(str(i)+","+str(j)+","+str(path_lenght)+"\n")
# avg=avg/1000.0
# print("avg", avg)

# d)
# n = 1000
# p = 0.05
# increment = 0.05
# limit = 0.5
# f = open("varying_p.txt", "a")
# count=0
# while(p<=limit):
# 	g = create_graph(n,p)
# 	avg = 0
# 	count = 0
# 	for k in range(400):
# 		i = random.randint(0,n-1)
# 		j = i
# 		while(j==i):
# 			j = random.randint(0,n-1)
# 		path_lenght = shortest_path(g,i,j)
# 		if(path_lenght>0):
# 			avg+=path_lenght
# 			count+=1
# 			print(p, count)
# 	f.write(str(p)+","+str(avg/float(count))+"\n")
# 	p+=increment

# Plot data
# data = open("varying_p.txt", "r")
# probabilities = []
# avgs = []
# for line in data:
# 	aux = [x.strip() for x in line.split(',')]
# 	probabilities.append(float(aux[0]))
# 	avgs.append(float(aux[1]))
# plt.plot(probabilities, avgs)
# plt.show()

# Facebook
# data = open("facebook_combined.txt", "r")
# g = Graph(4039)
# # Parse Data
# for line in data:
# 	aux = [x.strip() for x in line.split(' ')]
# 	g.add_edge(int(aux[0]), int(aux[1]))

# a) Average: 3.701
# avg = 0
# f = open("fb_shortest_path.txt", "a")
# count=0
# for k in range(1000):
# 	i = random.randint(0,4038)
# 	j = i
# 	while(j==i):
# 		j = random.randint(0,4038)
# 	print(count)
# 	count+=1
# 	path_lenght = shortest_path(g,i,j)
# 	avg+=path_lenght
# 	f.write(str(i)+","+str(j)+","+str(path_lenght)+"\n")
# avg=avg/1000.0
# print("avg", avg)
# f.write("Average: "+str(avg))

# b) p = 0.010819963503439287
# edges_count = g.edges_count()
# total_possible_edges = (4039*(4039-1))/2
# probability = edges_count/total_possible_edges
# print(probability)

# c) avg 2.64
# g = create_graph(4039,0.010819963503439287)
# avg = 0
# count=0
# for k in range(1000):
# 	i = random.randint(0,4038)
# 	j = i
# 	while(j==i):
# 		j = random.randint(0,4038)
# 	print(count)
# 	count+=1
# 	path_lenght = shortest_path(g,i,j)
# 	avg+=path_lenght
# avg=avg/1000.0
# print("avg", avg)
