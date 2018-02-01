class Constraint:

	def __init__(self):
		self.variables = dict()
		self.operators = list()
		self.domains = list()

	def create(self, function, variables):
		self.operators.append({'f':function, 'v':variables})

	def compute(self, operator):
		f = operator['f']
		v = operator['v']
		x = []
		for i in v:
			x.append(self.domains[i[0]][i[1]])
		return f(x)

	def __call__(self, objects):
		self.domains = objects
		y = []
		for i in range(len(self.operators)):
			y.append(self.compute(self.operators[i]))
		return y

def Pointer(domain, key):
	return [domain, key]

def F(x):
	return sum(x)

c = Constraint()
c.create(F, [Pointer(0, 'x'), Pointer(0, 'y')])

x = {'x':1, 'y':1}
print(c([x]))