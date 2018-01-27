from Operator import *

class Interpreter(dict):

	def __init__(self, symbols, functions):
		for i in range(len(symbols)):
			self[symbols[i]] = functions[i]

	def __call__(self, operator, inputs):
		S = Symbol(operator)
		L = Left(operator)
		R = Right(operator)

		A = inputs[L]
		B = inputs[R]
		F = self[S]
		return F(A,B)