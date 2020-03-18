class DirectedEdge(object):
	def __init__(self,v,w,weight):
		self.v=v
		self.w=w
		self.weight=weight
	def weightv(self):
		return self.weight
	def fromv(self):
		return self.v
	def tov(self):
		return self.w