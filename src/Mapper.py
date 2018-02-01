from random import randrange as rr

def sort(X):
	I = []
	for i in range(len(X)):
		I.append(i)
	done = False
	while not done:
		done = True
		for i in range(len(X)-1):
			if X[i] > X[i+1]:
				v = X[i]
				X[i] = X[i+1]
				X[i+1] = v

				z = I[i]
				I[i] = I[i+1]
				I[i+1] = z
				done = False
	return I

def utility(options, constraints):
	table = []
	for i in range(len(constraints)):
		table.append([])
		for j in range(len(options)):
			table[i].append(constraints[i](options[j]))
	return table

def validity(utilities, thresholds):
	table = []
	for i in range(len(utilities)):
		table.append([])
		for j in range(len(utilities[i])):
			table[i].append(utilities[i][j] >= thresholds[i])
	return table

def ordered_domains(validities, urgencies):
	domains = []
	for i in range(len(validities)):
		u = []
		d = []
		for j in range(len(validities[i])):
			if validities[i][j]:
				u.append(urgencies[j])
				d.append(j)

		order = sort(u)
		domains.append([])
		for j in order:
			domains[i].append(d[j])
	return domains

def intersection(a, b):
	y = []
	for i in range(len(a)):
		if a[i] in b: y.append(a[i])
	return y

def union(x):
	y = []
	for i in range(len(x)):
		for j in range(len(x[i])):
			if x[i][j] not in y:
				y.append(x[i][j])
	return y

def frequency(domains, values):
	y = []
	for i in range(len(values)):
		y.append([])
		for j in range(len(domains)):
			if values[i] in domains[j]:
				y[i].append(j)
	return y

def urgency(domains):
	y = []
	values = union(domains)
	overlap = frequency(domains, values)
	for i in range(len(values)):
		y.append(0)
		for j in range(len(overlap[i])):
			d = overlap[i][j]
			y[i] += 1
	return y

def rank(domains, values):
	y = []
	values = union(domains)
	for i in range(len(domains)):
		d = len(domains[i])
		s = len(values)
		y.append((1 - d / s))
	return y

def importance(domains):
	y = []
	values = union(domains)
	urgencies = urgency(domains)
	ranks = rank(domains, values)
	for i in range(len(ranks)):
		y.append([])
		for j in range(len(domains[i])):
			x = values.index(domains[i][j])
			r = ranks[i] * urgencies[x]
			y[i].append(r)
	return y

def confliction(domains, variable, option):
	y = []
	values = union(domains)
	index = values.index(option)
	variables = frequency(domains, values)[index]

	for i in range(len(variables)):
		v = variables[i]
		d = len(domains[v])
		if d == 1:
			y.append(v)
	return y

def revision(domains, option):
	y = domains
	for i in range(len(domains)):
		if option in domains[i]:
			del y[i][y[i].index(option)]
	return y

def selection(domains):
	variable = None
	for i in range(len(domains)):
		if variable == None or len(domains[i]) < len(domains[variable]):
			if len(domains[i]) > 0:
				variable = i
	return variable

def computation(constraints, values, thresholds):
	y = []
	for i in range(len(constraints)):
		y.append([])
		for j in range(len(values)):
			if constraints[i](values[j]) >= thresholds[i]:
				y[i].append(values[j])
	return y


def assignment(domains, variable, assignments):
	D = domains
	V = variable
	Y = assignments

	if variable != None and Y[variable] == None:
		domain = D[variable]
		if len(domain) > 0:
			V = None
			A = None
			index = rr(len(domain))
			option = domain[index]

			V = variable
			A = option		

			if Y[V] != None: 
				return D,V,Y

			C = confliction(D, V, A)
			if len(C) > 0:
				D = revision(D,A)
				V = C[rr(len(C))]
				D,V,Y = assignment(D, V, Y)
				Y[V] = A
			else:
				D = revision(D, A)
				Y[V] = A

		return D,V,Y
	

def F(x):
	return x == 'red'
def G(x):
	return x != 'blue'
def H(x):
	return x == 'red' or x == 'green'

c = [F,G,H]
t = [1,1,1]
x = ['green', 'blue', 'red', 'orange']

y = []
for i in range(len(c)):
	y.append(None)

d = computation(c, x, t)
s = selection(d)
A = []
for i in range(100):
	A = assignment(d, s, y)
	if A == None:break
	y = A[2]
	print(y)
	
	d = revision(d, A[1])
	s = selection(d)
# 	# y[A[0]] = A[1]

	# print(a)
	# if a != None:
	# 	for j in range(len(a[0])):
	# 		var = a[0][j]
	# 		val = a[1][j]
	# 		y[var] = val
	# 		d = revision(d, val)
	# 	s = selection(d)
# class System:
# 	def __init__(self):
# 		self.objects = []
# 		self.overlap = []
# 		self.domains = []
# 		self.weights = []

# def F(x):
# 	return x >= 5
# def G(x):
# 	return x == 5
# def H(x):
# 	return x <= 5

# x = [1, 6, 5]
# c = [F, G, H]
# t = [1, 1, 1]


# V = validity(utility(x,c),t)
# U = urgency(V)

# for i in range(len(V)):
# 	u = 0
# 	c = 0
# 	for j in range(len(V[i])):
# 		if V[i][j]:
# 			u += U[j] 
# 			c += 1

# 	print(c, u)

# domains = ordered_domains(V, U)
# print(domains)