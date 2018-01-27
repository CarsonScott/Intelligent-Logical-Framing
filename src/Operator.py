def Operator(symbol, left, right, types=None):
	if types == None: types = ['index', 'index']
	return {'symbol':symbol, 'left':left, 'right':right, 'types':types}

def Symbol(operator):
	return operator['symbol']

def Left(operator):
	return operator['left']

def Right(operator):
	return operator['right']

def Types(operator):
	return operator['types']

def SetTypes(operator, types):
	operator['types'] = types