def Operator(symbol, left, right):
	return {'symbol':symbol, 'left':left, 'right':right}

def Symbol(operator):
	return operator['symbol']

def Left(operator):
	return operator['left']

def Right(operator):
	return operator['right']