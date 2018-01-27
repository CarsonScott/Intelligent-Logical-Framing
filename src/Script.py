from Object import *
from Interpreter import *
from Functions import *

def Script(properties, inputs, operators, memory):
	return {'_P':properties, '_O':operators, '_X':inputs, '_M':memory, '_D':list()}

def Pro(S):
	return S['_P']

def Mem(S):
	return S['_M']

def Dat(S):
	return S['_D']

def Op(S):
	return S['_O']

def In(S):
	return S['_X']

def Val(S, X):
	V = []
	for p in Pro(S):
		v = None
		if Has(X, p):
			v = X[p]
		V.append(v)
	return V

def Set(S, X):
	S['_D'] = Val(S, X)

def Out(I, S, i):
	V = []
	M = Mem(S)
	D = Dat(S)
	P = Pro(S)
	
	for p in In(S)[i]:
		v = None
		if p[0] == '-':
			V.append(M[p[1:]])
		else:
			j = P.index(p)
			V.append(D[j])

	O = Op(S)[i]
	return I(O, V)

def Exe(I, S, X):
	Set(S, X)
	O = Op(S)
	
	Y = []
	for i in range(len(O)):
		y = Out(I, S, i)
		Y.append(y)
	return Y