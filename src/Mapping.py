from Statistics import sort

class ConstraintGraph:
	def __init__(self, functions, pairs, relations):
		self.vertices = []
		self.neighbors = []
		self.functions = []
		self.relations = []
		for i in range(len(functions)):
			self.vertices.append(None)
			self.functions.append(functions[i])
			self.neighbors.append([])
			self.relations.append([])

		for i in range(len(pairs)):
			a,b = pairs[i]
			if b not in self.neighbors[a]:
				self.neighbors[a].append(b)
				self.relations[a].append(relations[i])

	def construct(self, variables):
		spaces = []
		sorted_spaces = []
		index_spaces = []

		for i in range(len(self.vertices)):
			spaces.append([])
			sorted_spaces.append([])
			index_spaces.append([])
			for j in range(len(variables)):
				spaces[i].append(self.functions[i](variables[j]))

		print(spaces)

def F(x): 
	return x==1
def G(x): 
	return x==2 
def H(x):
	return x==3 
def R(a,b):
	return pow(a-b, 2) 

CG = ConstraintGraph([F, H], [[0, 1], [1, 2]], [R, R, R])

V = [1,2,3]
CG.construct(V)