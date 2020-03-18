from Heap import Heap
from WeightedDigraph import WeightedDigraph
from DirectedEdge import DirectedEdge
class SP(object):
	def __init__(self,G,s):
		self.G=G
		self.s=s
		self.h=Heap(self.G.V())
		for i in range(self.G.V()):
			self.h.insert(i,self.G.adjmat[self.s][i])
		self.adjlist=[[0,0,0] for i in range(self.G.V())]
		self.count=0

	def disttov(self,v):
		adjmat=self.G.adjmat
		n=self.G.V()
		if adjmat[self.s][v]!=-1:
			return adjmat[self.s][v]

		return 100000

	def hasPathtov(self,v):
		dis=self.disttov(v)
		if dis!=100000:
			return True
		return False
	def display(self):
		print("shortest path from source ",self.s)
		for x in self.adjlist:
			print("Vertex: ",x[0]," Distance: ",x[1]," Predecessor: ",x[2])
	def dijkstraSP(self):
		for i in range(self.G.V()):
			vert = self.h.DeleteMin()
			self.adjlist[self.count][0]=vert[0]
			self.adjlist[self.count][1]=vert[1]
			self.relax(vert[0])
			self.count+=1
		self.display()

	def relax(self,v):
		for adjedge in self.G.adj(v):
			if (adjedge.weightv()+self.G.adjmat[self.s][v])<self.G.adjmat[self.s][adjedge.tov()]:
				self.h.DecreaseKey(adjedge.tov(),adjedge.weightv()+self.G.adjmat[self.s][v])	
				self.adjlist[adjedge.tov()][2]=v