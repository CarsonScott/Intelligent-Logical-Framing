def Graph(vertices, arcs):
	return {'vertices':vertices, 'arcs':arcs}

def Vertices(graph):
	return graph['vertices']

def Arcs(graph):
	return graph['arcs']

def Neighbors(graph, vertex):
	neighbors = []
	arcs = Arcs(graph)
	for arc in arcs:
		if vertex in arc:
			i = arc.index(vertex)
			n = arc[0]
			if n == vertex:
				n = arc[1]
			neighbors.append(n)
	return neighbors