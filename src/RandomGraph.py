from Graph import *
from math import sqrt
from random import randrange as rr

def distance(p1, p2):
	return sqrt(pow(p2[0]-p1[0], 2) + pow(p2[1]-p1[1], 2))

def RandomGraph(space, size, neighborhood):
	vertices = []
	positions = []
	arcs = []
	for i in range(size):
		vertices.append(dict())
		positions.append([rr(space[0]), rr(space[1])])

	for i in range(len(vertices)):
		for j in range(i, len(vertices)):
			if i != j:
				if distance(positions[i], positions[j]) <= neighborhood:
					arcs.append([i, j])

	G = Graph(vertices, arcs)
	G['positions'] = positions
	return G

# V = 10
# N = 5
# S = [25, 25]
# G = RandomGraph(S, V, N)
# space = [[None for i in range(S[0])] for j in range(S[1])]

# positions = G['positions']
# for i in range(len(positions)):
# 	x,y = positions[i]
# 	if space[y][x] == None:
# 		space[y][x] = [i]
# 	else:
# 		space[y][x].append(i)

# for row in space:
# 	string = ''
# 	for v in row:
# 		if v != None:
# 			string += str(v)
# 		else:
# 			string += ' '
# 	print(string)