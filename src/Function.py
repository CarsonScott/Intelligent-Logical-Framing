def Function(input, operation, type):
	return {'input':input, 'operation':operation, 'type':type}

def Input(function):
	return function['input']

def Operation(function):
	return function['operation']

def Type(function):
	return function['type']

def Compute(F, X):
	I = Input(F)
	T = Type(F)

	y = None
	o = Operation(F)
	if T == 'comparative':
		a = X[0][I[0]]
		b = X[1][I[1]]
		y = o(a, b)
	elif T == 'atomic':
		if I[0] in list(X.keys()):
			x = X[I[0]]
			y = o(x)
		else:
			y = False
	return y
