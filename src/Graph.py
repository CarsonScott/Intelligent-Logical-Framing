def Graph(vertices, arcs, ordered=False):
	G = {'vertices':vertices, 'arcs':arcs}
	N = []
	for i in range(len(vertices)):
		N.append([])
	for i in range(len(arcs)):
		a,b = arcs[i]
		if b not in N[a]:
			N[a].append(b)
		if not ordered:
			if a not in N[b]:
				N[b].append(a)
	G['neighbors'] = N
	return G

def UnionGraph(graph1, graph2):
	V1 = Vertices(graph1)
	V2 = Vertices(graph2)
	V = V1 + V2

	A1 = Arcs(graph1)
	A2 = Arcs(graph2)
	for i in range(len(A2)):
		A2[i][0] += len(V1)
		A2[i][1] += len(V1)
	A = A1 + A2
	return Graph(V, A)

def Vertices(graph):
	return graph['vertices']

def Arcs(graph):
	return graph['arcs']

def Neighbors(graph, i):
	return graph['neighbors'][i]

def Join(G, i, j):
	A = Arcs(G)
	V = Vertices(G)
	del V[j]
	for k in range(len(A)):
		a = A[k]
		for l in range(len(a)):
			v = a[l]
			if v == j: v = i
			if v > j: v -= 1
			a[l] = v
		A[k] = a	
	return Graph(V, A)
