from Object import *

def frequency(G, X, k):
# Determine the total number of objects in a group that are equivalent to a given object with respect to a certain property
	y = 0
	for j in range(len(G)):
		y += Equal(X, G[j], k)
	return y * 1 / len(G)



def accordance(G, X):
# Determine the sum of frequencies for all properties of an object within a group
	y = 0
	for k in Keys(X):
		y += frequency(G, X, k)
	return y# * 1 / Size(X)



def significance(G, X, k):
# Determine the relevance of an object with respect to a certain property within a group 
	return frequency(G, X, k) * accordance(G, X)
