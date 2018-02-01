from Clustering import *
from Grouping import *
from Script import *

def test_clustering(G):
	P,O = create(G)
	for i in range(len(O)):
		print(P[i], '\n')
		D = revise(O[i])
		for k in Keys(O[i]):
			print('	(' + k + ')')
			V = D[k][0]
			F = D[k][1]
			for j in range(len(V)):
				print('	 |  \'' + V[j] + '\' :', F[j])

def test_grouping(G):
	for i in range(len(G)):
		a = significance(G, G[i], 'a')
		b = significance(G, G[i], 'b')
		print('(' + str(i) + ') ', a, b)

def test_interpreter():
	I = Interpreter(['=', '+'], [equal_to, add])
	O = Operator('+', Operator('=', 0, 1), Operator('=', 2, 3))
	SetTypes(O, ['operator', 'operator'])

	S = Script(['a', 'b'], [['a', '-a', 'b', '-b']], [O], {'a':2, 'b':1})
	X = {'a':2, 'b':1}
	print(Exe(I, S, X))

test_interpreter()