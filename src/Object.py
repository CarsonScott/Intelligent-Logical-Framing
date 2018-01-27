def Keys(F):
# Determine the set of properties of a given object
	return list(F.keys())

def Values(F):
# Determine the set of values of a given object
	return list(F.values())

def Has(F, k):
# Determine whether an object posesses a given property
	return k in Keys(F)

def Size(F):
# Determine the number of properties of a given object
	return len(Keys(F))

def Equal(A, B, k):
# Determine whether two elements have the same value for a given property
	if Has(A, k) and Has(B, k):
		return A[k] == B[k]
	return False

def Shared(A, B):
# Determine the set of shared elements between two given objects
	y = []
	for k in Keys(A):
		if k in Keys(B):
			y.append(k)
	return y

def Matching(A, B):
# Determine the set of equal elements between two given objects
	y = []
	for k in Shared(A, B):
		if Equal(A, B, k):
			y.append(k)
	return y

def Union(A, B):
# Determine the domain for each property possessed by at least of the two given objects
	F = dict()
	keys = Keys(A) + Keys(B)
	for k in keys:
		if not Has(F, k):
			F[k] = []
	keys = Keys(F)
	for k in keys:
		values = [None, None]
		if Has(A, k):
			values[0] = A[k]
		if Has(B, k):
			values[1] = B[k]
		F[k] = values
	return F