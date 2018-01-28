from Graph import *
from random import randrange as rr

def Walker(template, position, ground):
	return {'template':template, 'position':position, 'ground':ground}

def Position(walker):
	return walker['position']

def Ground(walker):
	g = walker['ground']
	return Vertices(walker['template'])[g]

def Move(walker, position):
	walker['position'] = position

def Observation(graph, walker):
	P = Position(walker)
	N = Neighbors(graph, P)
	V = Vertices(graph)
	Y = []
	for n in N: 
		Y.append(V[n])
	return Y

def Calculation(walker, neighbors):
	Y = []
	G = Ground(walker)
	for i in range(len(neighbors)):
		x = neighbors[i]
		if G(x):
			Y.append(i)
	return Y

def Selection(walker, neighbors):
	G = Ground(walker)
	C = Calculation(walker, neighbors)
	Y = rr(len(neighbors))
	if len(C) > 0: 
		Y = C[rr(len(C))]
	return Y

def Update(graph, walker):
	X = Observation(graph, walker)
	P = Position(walker)
	N = Neighbors(graph, P)
	Y = Selection(walker, X)
	Move(walker, N[Y])
