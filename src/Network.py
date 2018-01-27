def Network(nodes, links, ordered=False, labeled=False):
	return {'nodes':nodes, 'links':links, 'ordered':ordered, 'labeled':labeled}

def OrderedNetwork(nodes, links):
	network = Network(nodes, links, labeled)
	return network

def LabeledNetwork(nodes, links, labels):
	network = Network(nodes, links, labeled=True)
	network['labels'] = labels
	return network



def Nodes(network):
	return network['nodes']

def Links(network):
	return network['links']

def Ordered(network):
	return network['ordered']

def Labeled(network):
	return network['labeled']

def Labels(network):
	return network['labels']

def NodeLabels(network):
	if Labeled(network):
		return Labels(network)[0]

def LinkLabels(network):
	if Labeled(network):
		return Labels(network)[1]

def src(link):
	return link[0]

def dst(link):
	return link[1]

def Relevant(network, node):
	relevant = []
	links = Links(network)
	for i in range(len(links)):
		if node in links[i]:
			relevant.append(i)
	return relevant

def Neighbors(network, node):
	neighbors = []
	relevant = Relevant(network, node)
	links = Links(network)
	for i in relevant:
		link = links[i]
		if src(link) == node:
			neighbors.append(dst(link))
		elif dst(link) == node and not Ordered(network):
			neighbors.append(src(link))
	return neighbors