from Operator import *

class Interpreter(dict):

	def __init__(self, symbols, functions):
		for i in range(len(symbols)):
			self[symbols[i]] = functions[i]

	def __call__(self, operator, inputs):
		S = Symbol(operator)
		L = Left(operator)
		R = Right(operator)
		T = Types(operator)
		X = [L, R]

		for i in range(len(T)):
			if T[i] == 'operator':
				X[i] = self(X[i], inputs)
			elif T[i] == 'index':
				X[i] = inputs[X[i]]
		print(X[i])
		F = self[S]
		return F(X[0], X[1])