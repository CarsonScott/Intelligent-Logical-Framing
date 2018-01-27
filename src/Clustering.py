from Object import *
from Network import *
from Functions import *

def resemblance(A, B):
# Determine the fraction of shared properties between two given objects that are equal
	if len(Shared(A, B)) != 0:
		return len(Matching(A, B)) / len(Shared(A, B))
	return 0

def correspondence(A, B):
# Determine the ratio of equality to inequality with respect to the properties of two given objects 
	size = (Size(A) + Size(B)) / 2
	return resemblance(A, B) * len(Shared(A, B)) / size

def connect(G):
# Determine the topology for a network to represent the similarity between objects in a group
	L = []
	C = []
	for i in range(len(G)):
	
		for j in range(i, len(G)):
			if i != j:
				A = G[i]
				B = G[j]
				Y = correspondence(A, B)

				if Y != 0:
					L.append([i,j])
					C.append(Y)

	return LabeledNetwork(G,L, [None,C])

def cluster(N):
# Determine the set of unordered pairs to represent the greatest correspondence between objects in a group 
	Y = []
	for i in range(len(Nodes(N))):
		R = Relevant(N, i)
		C = LinkLabels(N)
		L = Links(N)

		m = None
		for j in R:
			if m == None: 
				m = j
			nearest = C[m]
			current = C[j]
			if current > nearest: 
				m = j
		
		if m != None:
			if src(L[m]) == i:
				n = dst(L[m])
			else: n = src(L[m])
			Y.append([i, n])
	return Y

def combine(G):
# Determine the set of objects resulting from the combination of two paired objects  
	N = connect(G)
	P = cluster(N)
	O = []
	
	for i in range(len(P)):
		p = P[i]
		Y = None
	
		if len(p) == 2:
			A = G[p[0]]
			B = G[p[1]]
			Y = Union(A,B)
		O.append(Y)
	
	return [P, O]

def create(G):
# Determine the non-reduntant set of combined objects
	P,O = combine(G)
	for i in range(len(P)):
		for j in range(i, len(P)):
			if i != j:
				A = P[i]
				B = P[j]	
	
				if equal_pair(A, B):
						del P[j]
						del O[j]
						break
	return P,O

def revise(X):
# Determine the frequency distribution over the domain of each property 
	Y = dict()
	K = Keys(X)
	
	for k in K:
		y = dict()
		for i in range(len(X[k])):
			v = str(X[k][i])
	
			if Has(y, v):
				y[v] += 1 / len(X[k])
			else: y[v] = 1 / len(X[k])
		Y[k] = Keys(y), Values(y)
	
	return Y
