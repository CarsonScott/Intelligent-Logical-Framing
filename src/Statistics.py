def sort(X):
	done = False
	while not done:	
		done = True
		for i in range(len(X)-1):
			if X[i] > X[i+1]:
				v = X[i]
				X[i] = X[i+1]
				X[i+1] = v
				done = False
	return X

def Median(X):
	i = int(len(X)/2)
	m = None
	if len(X) % 2 == 0:
		m = (X[i-1]+X[i])/2
	else: m = X[i]
	return m

def Quartiles(X):
	median = Median(X)

	i = int(len(X) * .25)
	j = int(len(X) * .75)
	Q1 = None
	Q3 = None
	if len(X) % 2 == 0:
		Q1 = (X[i-1]+X[i])/2
		Q3 = (X[j-1]+X[j])/2
	else:
		Q1 = X[i]
		Q3 = X[j]

	return Q1, Q3

def Boundaries(X):
	Q1, Q3 = Quartiles(X) 
	L = Q1 - 1.5 * (Q3 - Q1)
	U = Q3 + 1.5 * (Q3 - Q1)
	return L, U

def Outliers(X):
	Q1, Q3 = Quartiles(X)
	least = Q1 - 1.5 * (Q3 - Q1)
	most = Q3 + 1.5 * (Q3 - Q1)
	outliers = []
	for x in X:
		if x < least or x > most:
			outliers.append(x)
	return outliers
