from random import randrange as rr
from math import floor 

def Average(X):
	return sum(X) / len(X)

def MSE(a, b):
	return pow(a-b, 2)

class Searcher:

	def __init__(self, function, position, threshold, rate, factor=1):
		self.function = function
		self.position = position
		self.threshold = threshold
		self.factor = factor
		self.rate = rate

	def compute(self, neighbors):
		utilities = []
		for i in range(len(neighbors)):
			utilities.append(self.function(neighbors[i]))
		return utilities

	def select(self, utilities):
		optimum = utilities.index(max(utilities))
		if utilities[optimum] < self.threshold:
			selection = rr(len(utilities))
		else:
			selection = optimum
		return selection

	def __call__(self, state, neighbors):
		utilities = self.compute(neighbors)
		selection = self.select(utilities)
		self.train(utilities[selection])
		return selection

	def train(self, utility):
		self.threshold += self.rate * (self.factor * utility - self.threshold)